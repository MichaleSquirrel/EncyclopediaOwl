Thursday October 29 Day 302 week 44 of 2026

## 1.TodoList



## 2.MCA课程学习进度

2026年10月29号学习进展：
1. 复习《》
2. 阅读
   大概用时：小时

## 3.使用Langchain4J框架调用引望内网模型


参考如下代码
D:\700000AI\ModelContextProtocol\agoncal-fascicle-langchain4j

可以阅读D:\637273Langchain里的相关源码

写一个可以在内网调用的有实际功能的项目

代码放在D:\637273Langchain文件夹下，新建一个文件夹


## 4.
DebugChatDrawer







## 8.

http://localhost:8890/api/health

```json
{
   "status": "UP",
   "certInstalled": true,
   "defaultModel": "glm",
   "models": [
      "glm",
      "deepseek",
      "qwen"
   ]
}
```
http://localhost:8890/api/models

```json
[
   {
      "alias": "glm",
      "modelName": "GLM-5.3-Flash",
      "baseUrl": "https://ai-models.rnd.yinwang.com/ai-platform-models-agent/v1",
      "isDefault": true
   },
   {
      "alias": "deepseek",
      "modelName": "DeepSeek-V4-Flash-0731",
      "baseUrl": "https://ai-models.rnd.yinwang.com/ai-platform-models-agent/v1",
      "isDefault": false
   },
   {
      "alias": "qwen",
      "modelName": "Qwen3.8-27B",
      "baseUrl": "https://ai-models.rnd.yinwang.com/ai-platform-models-agent/v1",
      "isDefault": false
   }
]
```


http://localhost:8890/api/chat/multi-turn?userId=m30026548&question=你是谁
http://localhost:8890/api/chat/multi-turn?userId=m30026548&model=qwen&question=你是谁





