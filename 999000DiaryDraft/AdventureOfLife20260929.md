Tuesday September 29 Day 272 week 40 of 2026

## 1.TodoList
1. OpenCode调用Obsidian
2. 创办个人知识管理的公司
3. OpenCode使用google搜索
4. 学习OpenCode的使用
5. 查询GitHUB  MCP   https://github.com/



## 2.MCA课程学习进度

2026年09月29号学习进展：
1. 复习
2. 阅读
   大概用时：小时


## 3.OpenCode调用Obsidian

Agent Skills for use with Obsidian.
https://github.com/kepano/obsidian-skills


https://cloud.tencent.com/developer/article/2646826

https://zhuanlan.zhihu.com/p/1997053691971278101

https://community.obsidian.md/plugins/copsilot

Codex(ClaudeCode、OpenCode)+Obsidian搭建个人AI知识库保姆级教程、零成本AI知识库、卡帕西同款知识库
https://www.bilibili.com/video/BV1Bput6eE3i/?vd_source=dd94464bac13f791ea6a2e385d28295a

在 Obsidian 中使用 opencode，助力AI写作
https://zhuanlan.zhihu.com/p/1994551885298950717

AI 知识库部署指南
https://github.com/zxfccmm4/Obsidian-OpenCode-Knowledge/blob/main/deployment-guide.md

## 5.OpenCode
OpenCode使用google搜索


如何把 OpenCode 从“能用”配置到“高效可用”？我实测了 7 个常用插件
https://cloud.tencent.com/developer/article/2661551


https://github.com/code-yeongyu/oh-my-opencode 还可以安装oh-my-opencode，据说很厉害，我还没用多久



OpenCode 浏览器操作完整指南
https://segmentfault.com/a/1190000047611760



https://zhuanlan.zhihu.com/p/1991464412431794350


如何把 OpenCode 从“能用”配置到“高效可用”？我实测了 7 个常用插件
https://cloud.tencent.com/developer/article/2661551


https://opencode.ai/docs/zh-cn/mcp-servers/


https://opencode.ai/docs/zh-cn/ecosystem/



OpenCode 教程：Skills 与 MCP 从入门到精通

https://mcp.csdn.net/6a2e1981662f9a54cb7e8dbf.html


## 8.

添加GitHub search MCP
https://github.com/



https://github.com/search?q=awesome+mcp&type=repositories



## 9.知识图谱专业

SophX知识图谱支撑专业课程体系改革的探索性案例：国际与公共事务学院行政管理专业
https://news.sjtu.edu.cn/jdyw/20250114/206580.html

人工智能哲学硕士-博士
https://sai.cuhk.edu.cn/zh-hans/node/35

## 11.AMD & CSDN AI 开发者联合活动

AMD & CSDN AI 开发者联合活动
https://builderx.csdn.net/activity-site/project/amd/home

## 14.
从https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture找几个比较复杂的单词作为样例
如：
dedicated
participants
fundamental
把这些单词放在https://www.etymonline.com/中搜索，把搜索的结果放在一个文档中，方便我把etymonline_mcp部署到内网后依然可以响应

szlib_mcp.py
https://www.szlib.org.cn/opac/searchShow?v_index=title&sortfield=ptitle&sorttype=desc&pageNum=10&library=all&v_tablearray=bibliosm,serbibm,apabibibm,mmbibm,&v_value=MCP
可以内置几个关键词，比如MCP、Agent、OpenCode、Nginx等，把获取的响应存放在本地，方便我把szlib_mcp部署到内网后依然可以响应


http://10.41.1.8:8701/mcp
curl http://10.41.1.8:8701/mcp


curl http://10.41.1.8:8701/mcp
{"name": "etymonline-mcp", "title": "Etymonline 词源查询", "version": "1.1.0", "endpoint": "/mcp", "protocol": "Streamable HTTP (JSON-RPC 2.0)", "offline_mode": false, "cache_loaded": true, "cached_words": ["participants", "architecture", "capabilities", "communication", "primitives", "dedicated", "subscription", "discovery", "fundamental", "elicitation"], "tools": ["etymology_fuzzy", "get_etymology_entry", "list_offline_words"]}


nohup python3 szlib_mcp.py --host 0.0.0.0 --offline >> szlib-mcp.log 2>&1 &
nohup python3 etymonline-mcp.py --host 0.0.0.0 --offline >> etymonline-mcp.log 2>&1 &


