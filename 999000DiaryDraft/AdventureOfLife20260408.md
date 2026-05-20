Wednesday April 8 Day 098 week 15 of 2026

## 1.TodoList
1. PKM添加Git 相关文档  
2. PKM添加Idea 官网  
3. PKM添加Nginx+lua+OpenResty高性能实践  
4. PKM添加Prometheus目录  
5. 在PKM   630000Project添加 应用编号和应用  
6. PKM  630000 目录整理  
7. 启动脚本要重新写



## 2.MCA课程学习进度

2026年04月8号学习进展：
1. 学习《团队开发和版本控制工具-GIT》  
2. 复习《RocketMQ5新特性与源码分析》  
   大概用时：8小时


## 8.在windows启动RocketMQ  
  
### 8.1 配置ROCKETMQ_HOME  
ROCKETMQ_HOME  
D:\635666RocketMQ\rocketmq-all-5.1.0-bin-release  
  
  
### 8.2 启动mqnamesrv  
start D:\635666RocketMQ\rocketmq-all-5.1.0-bin-release\bin\mqnamesrv.cmd  
![2026-04-08_170913.png](resource20260408/2026-04-08_170913.png)  
  
start D:\635666RocketMQ\rocketmq-all-5.1.0-bin-release\bin\mqbroker.cmd -n localhost:9876   
  
![2026-04-08_171008.png](resource20260408/2026-04-08_171008.png)  
  
```shell  
2026-04-08 17:09:47 INFO main - The broker[DESKTOP-U0TQ3BB, 10.65.13.62:10911] boot success. serializeType=JSON and name server is localhost:9876```  
  
java -jar D:\635666RocketMQ\rocketmq-dashboard-1.0.0.jar  
  
  
  
http://localhost:8089/#/