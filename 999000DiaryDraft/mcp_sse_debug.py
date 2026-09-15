# -*- coding: utf-8 -*-
"""
MCP SSE 原始 JSON-RPC 调试客户端（mcp-debug 风格，不依赖任何 MCP SDK）

交互流程（SSE 传输）:
  1. GET  /sse                建立事件流，收到 endpoint 事件（消息端点 + sessionId）
  2. POST <endpoint>          发送 JSON-RPC 请求（initialize / tools/list / tools/call...）
  3. 响应从 SSE 流推回（event: message），按 id 匹配请求与响应

用法:
  python mcp_sse_debug.py [server-base-url]    # 默认 http://127.0.0.1:8989
"""
import json
import queue
import sys
import threading
import urllib.request

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8989"

events = queue.Queue()          # SSE 流事件队列: (event, data)


def sse_reader(resp):
    """后台线程：逐行解析 SSE 流"""
    event = None
    try:
        for raw in resp:
            line = raw.decode("utf-8").strip()
            if line.startswith("event:"):
                event = line[len("event:"):].strip()
            elif line.startswith("data:"):
                data = line[len("data:"):].strip()
                if event:
                    events.put((event, data))
            elif not line:
                event = None  # 事件结束
    finally:
        events.put(("closed", None))


def wait_response(request_id, timeout=60):
    """等待 SSE 流中与请求 id 匹配的 JSON-RPC 响应；期间自动应答服务端 ping"""
    while True:
        kind, data = events.get(timeout=timeout)
        if kind == "closed":
            raise RuntimeError("SSE 连接已关闭")
        if kind != "message":
            continue
        msg = json.loads(data)
        if msg.get("id") == request_id and ("result" in msg or "error" in msg):
            return msg
        if msg.get("method") == "ping" and "id" in msg:
            post({"jsonrpc": "2.0", "id": msg["id"], "result": {}})  # 应答 ping


def post(payload):
    """POST JSON-RPC 到消息端点（通知类消息无响应，HTTP 返回 200/202）"""
    req = urllib.request.Request(
        message_url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"[POST] {payload.get('method', '')} (id={payload.get('id')}) -> HTTP {r.status}")


def request(payload, timeout=60):
    """发送请求并等待 SSE 流中的对应响应"""
    post(payload)
    return wait_response(payload["id"], timeout)


# ------------------------------------------------------------------
# 1. 建立 SSE 连接，获取消息端点
# ------------------------------------------------------------------
print(f"[SSE] 连接 {BASE}/sse ...")
sse_resp = urllib.request.urlopen(f"{BASE}/sse", timeout=180)
threading.Thread(target=sse_reader, args=(sse_resp,), daemon=True).start()

kind, data = events.get(timeout=10)
assert kind == "endpoint", f"第一个事件应为 endpoint，实际: {kind}"
message_url = BASE + data
print(f"[SSE] 消息端点: {message_url}\n")

# ------------------------------------------------------------------
# 2. initialize（握手）
# ------------------------------------------------------------------
resp = request({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "capabilities": {"roots": {"listChanged": True}},
        "clientInfo": {"name": "mcp-debug", "version": "1.0"},
    },
})
print("<< initialize 响应:")
print(json.dumps(resp, ensure_ascii=False, indent=2))

# ------------------------------------------------------------------
# 3. initialized 通知（无响应）
# ------------------------------------------------------------------
post({"jsonrpc": "2.0", "method": "notifications/initialized"})
print(">> notifications/initialized 已发送\n")

# ------------------------------------------------------------------
# 4. tools/list 查看工具清单
# ------------------------------------------------------------------
resp = request({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
print("<< tools/list 响应:")
print(json.dumps(resp, ensure_ascii=False, indent=2))

# ------------------------------------------------------------------
# 5. tools/call 调用 getWeather
# ------------------------------------------------------------------
resp = request({
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {"name": "getWeather", "arguments": {"city": "Beijing"}},
})
print("<< tools/call(getWeather, Beijing) 响应:")
print(json.dumps(resp, ensure_ascii=False, indent=2))

sse_resp.close()
print("\n完成")
