# MCP SSE 接口 Postman 调用指南

> 适用服务：SpringAISseMcpServer（SSE 传输，默认 `http://127.0.0.1:8989`，EC2 部署后替换为服务器地址）
> 调用方式：原始 JSON-RPC over SSE（mcp-debug 风格，不依赖任何 SDK）

## 1. 协议机制（重要，先读）

SSE 传输下的 MCP 调用分两条通道：

```
┌─ 通道A：GET /sse（长连接，保持不断开）──────────────────┐
│   服务端先推送 endpoint 事件（消息端点 + sessionId）      │
│   之后所有 JSON-RPC 响应都从这条流推送回来（event: message）│
└──────────────────────────────────────────────────────┘
┌─ 通道B：POST /mcp/message?sessionId=xxx ────────────────┐
│   所有 JSON-RPC 请求都 POST 到这里                        │
│   HTTP 返回 200 + 空 body（响应在通道A里，靠 id 配对）     │
└──────────────────────────────────────────────────────┘
```

**三条铁律**：
1. 先发 `GET /sse` 并**保持标签页不断开**，否则 sessionId 失效
2. POST 返回空 body 是**正常的**，去 SSE 标签页看响应
3. 请求与响应靠 JSON-RPC 的 `id` 配对；通知类消息（无 `id`）没有响应

## 2. 请求清单（按顺序调用）

### 请求① 建立 SSE 连接（最先发，保持连接）

| 项 | 值 |
|----|----|
| Method | `GET` |
| URL | `http://127.0.0.1:8989/sse` |
| Headers | `Accept: text/event-stream` |

**返回**（事件流第一段）：

```
event: endpoint
data: /mcp/message?sessionId=dec51889-75ab-4bff-b628-a014137261d5
```

→ **复制 sessionId**，后续所有 POST 使用。

### 请求② initialize（握手）

| 项 | 值 |
|----|----|
| Method | `POST` |
| URL | `http://127.0.0.1:8989/mcp/message?sessionId={{sessionId}}` |
| Headers | `Content-Type: application/json` |

**Body (raw JSON)**：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-06-18",
    "capabilities": {
      "roots": { "listChanged": true }
    },
    "clientInfo": { "name": "mcp-debug", "version": "1.0" }
  }
}
```

**响应**（在请求①的 SSE 标签页，`event: message`）：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "completions": {},
      "logging": {},
      "prompts": { "listChanged": true },
      "resources": { "subscribe": false, "listChanged": true },
      "tools": { "listChanged": true }
    },
    "serverInfo": { "name": "spring-ai-mcp-weather", "version": "1.0.0" }
  }
}
```

> 注：客户端请求 `2025-06-18`，服务端（Spring AI 1.0.0 / MCP Java SDK）协商回 `2024-11-05`，属正常版本协商，按服务端版本继续即可。

### 请求③ notifications/initialized（必须发，无响应）

```json
{ "jsonrpc": "2.0", "method": "notifications/initialized" }
```

POST 返回 HTTP 200 即成功，SSE 流中**不会有**响应（通知类消息无响应）。

### 请求④ tools/list（查看工具清单）

```json
{ "jsonrpc": "2.0", "id": 2, "method": "tools/list" }
```

**响应**（SSE 流，`id: 2`）：

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "getWeather",
        "description": "获取指定城市的当前天气情况，格式化后的天气报告字符串。",
        "inputSchema": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "城市名称，必须是英文格式，比如 London 或 Beijing"
            }
          },
          "required": ["city"],
          "additionalProperties": false
        }
      }
    ]
  }
}
```

### 请求⑤ tools/call（调用天气工具）

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "getWeather",
    "arguments": { "city": "Beijing" }
  }
}
```

**响应**（SSE 流，`id: 3`）：

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "\"城市: Beijing\\n天气描述: 晴\\n当前温度: 20.9°C\\n体感温度: 20.0°C\\n最低温度: 20.9°C\\n最高温度: 20.9°C\\n气压: 1025 hPa\\n湿度: 33%\\n风速: 1.8 m/s\\n\""
      }
    ],
    "isError": false
  }
}
```

### 请求⑥ ping（可选，测试链路活性）

```json
{ "jsonrpc": "2.0", "id": 4, "method": "ping" }
```

**响应**（SSE 流）：

```json
{ "jsonrpc": "2.0", "id": 4, "result": {} }
```

## 3. Postman 使用技巧

1. **环境变量**：建议创建 Postman 环境变量 `baseUrl`（`http://127.0.0.1:8989`）和 `sessionId`，请求 URL 统一写
   `{{baseUrl}}/mcp/message?sessionId={{sessionId}}`，每次重连 SSE 后只更新 `sessionId` 一个变量
2. **顺序不能乱**：① → ② → ③ 之后才能调工具；sessionId 与 SSE 连接绑定，SSE 断开后 sessionId 失效，需从①重来
3. **id 规则**：自增整数即可，响应靠它配对
4. **通知类消息**（无 `id`，如 `notifications/initialized`）没有响应
5. **服务端主动消息**：服务端可能发 `ping` 请求，需要用相同 `id` POST 回 `{"jsonrpc":"2.0","id":<收到的id>,"result":{}}`
6. **EC2 部署后**：把 `baseUrl` 换成服务器地址即可，协议完全一致

## 4. 常见问题

| 现象 | 原因与解决 |
|------|-----------|
| POST 返回 200 但 body 为空 | 正常现象，响应在 `GET /sse` 的事件流里 |
| SSE 流里一直没响应 | 检查 POST 的 URL 是否带了正确的 `sessionId`；sessionId 是否来自当前活跃的 SSE 连接 |
| sessionId 失效 / POST 404 | SSE 连接已断开（标签页关闭/超时），从请求①重新开始 |
| 调用工具报 "session not found" | 同上，重建 SSE 连接获取新 sessionId |
| 想换城市测试 | 只改请求⑤ 的 `arguments.city`：`Beijing`（真实采样数据）、其他城市（Mock 确定性生成）、不存在的城市（返回"未找到该城市"） |
| 批量/自动化调用 | 使用配套脚本 `McpSseDebugClient/mcp_sse_debug.py`（自动处理 SSE 解析、id 配对、ping 应答） |

## 5. 配套资源

| 资源 | 说明 |
|------|------|
| `McpSseDebugClient/mcp_sse_debug.py` | 命令行版调试客户端（纯 Python 标准库），`python mcp_sse_debug.py [baseUrl]` 一键完成①~⑤全流程 |
| Mock 直连测试 | `GET http://127.0.0.1:8989/data/2.5/weather?q=Beijing`、`GET /mock/health`（可不经 MCP 直接验证 Mock） |
| 服务日志 | `D:/data01/mcpServer/log/mcp-weather-stdio-server.log`（EC2 上为 `/data01/mcpServer/log/`） |
