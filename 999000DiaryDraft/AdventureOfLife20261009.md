Friday October 9 Day 282 week 41 of 2026

## 1.TodoList
1. 学习使用LLM wiki
2. 如何在内网使用Cherry Studio？
3. 内网本地使用Claude code


## 2.MCA课程学习进度

2026年10月9号学习进展：
1. 复习《》
2. 阅读
   大概用时：小时

## 3.在内网使用Cherry Studio

https://3ms.huawei.com/km/blogs/details/22267752


## 4.C盘空间清理

1. WeLink聊天记录迁移



## 5.内网Claude Code安装

https://clouddevops.huawei.com/domains/1475/wiki/8/WIKI2026011400302








## 8.OpenCode 添加mcp_server_mysql 
mcp_server_mysql 




## 9.




```text
写一个关于“2026年AI技术突破”的技术报告提纲，
并使用文件系统工具将完成的报告提纲文本内容保存到文件中。

1. 生成内容要求
   - 涵盖LLM、AI Agent、MCP三大领域

2. 文件保存要求：
   - 保存文件名：D:\\637267AgentGatewayAndMCPGateway\\APIG-JavaScript\\2026.md
   - 操作要求：文件夹如不存在要先创建，文件已存在则覆盖
   - 核对要求：检查文件是否生成
```


```text
如何运行
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter05\server-stdio.py


```

使用uv run mcp dev server-stdio.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter05\server-stdio.py
使用uv启动server-stdio.py，并可以使用MCP Inspector进行调试




uv run mcp dev server-resources.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter06\server-resources.py
使用uv启动server-resources.py，并可以使用MCP Inspector进行调试


uv run mcp dev server-tools.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter06\server-tools.py
使用uv启动server-tools.py，并可以使用MCP Inspector进行调试


CherryStudio 添加如下MCP 报错

```json
{
  "mcpServers": {
    "server-tools": {
      "command": "uv",
      "args": [
        "--directory",
        "D:\\637267AgentGatewayAndMCPGateway\\APIG-JavaScript\\chapter06",
        "run",
        "--with",
        "mcp",
        "mcp",
        "run",
        "server-tools.py"
      ],
      "env": {}
    }
  }
}
```

MCP error -32000: Connection closed


MCP标准分别是20250618和20260728发布的，这两个数字相乘会有什么奇妙的结果？

在计算这两个数字相乘时有没有用到server-tools  MCP？



### 8.2

uv run mcp dev server-propmts.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter06\server-propmts.py
使用uv启动server-propmts.py，并可以使用MCP Inspector进行调试

```json
{
  "mcpServers": {
    "server-propmts": {
      "command": "uv",
      "args": [
        "--directory",
        "D:\\637267AgentGatewayAndMCPGateway\\APIG-JavaScript\\chapter06",
        "run",
        "--with",
        "mcp",
        "mcp",
        "run",
        "server-propmts.py"
      ],
      "env": {}
    }
  }
}
```

大语言模型的参数量极其巨大


### 8.3

uv run mcp dev server-sampling.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter06\server-sampling.py
使用uv启动server-sampling.py，并可以使用MCP Inspector进行调试


### 8.4 

# 1、运行Streamable LLM Server
uv run python server-context.py
# 2、运行客户端（在另一个命令行中）
uv run python client-context.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter06\
使用uv启动server-context.py，和client-context.py



## 9.


uv run python mcp_server_gradio.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter07\mcp_server_gradio.py
使用uv启动mcp_server_gradio.py
# 大语言模型和大型语言模型是不是一个意思？用工具计算一下相似度



## 10

## 9.


uv run python mcp_server_gradio.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter07\mcp_server_gradio.py
使用uv启动mcp_server_gradio.py
# 大语言模型和大型语言模型是不是一个意思？用工具计算一下相似度




uv run python mcp_server_fastapi.py
D:\637267AgentGatewayAndMCPGateway\APIG-JavaScript\chapter07\mcp_server_fastapi.py
使用uv启动mcp_server_fastapi.py



https://github.com/microsoft/playwright-mcp

https://github.com/langflow-ai/langflow

https://github.com/langflow-ai/langflow



