Thursday January 22 Day 022 week 4 of 2026

## 1.TodoList
1. 今晚早点回大水坑，先洗衣服，然后晾起来，晚上9点带黑芝麻糊回九华山
2. 回九华山后喝黑芝麻糊，并领夜宵
3. 然后整理房间和行囊，准备明天赶火车，带身份证，衣服，红包，眼镜，背包，背包里放水杯
4.


## 2.WindowsStartScript

```shell
:: start BurpSuite
C:\Java\jdk-21.0.9+10\bin\java.exe -jar D:\800000CyberSecurity\burpsuite_pro_v2025.11.2\BurpLoaderKeygen_v1.17.jar


::start IDEA
start C:\"Program Files"\JetBrains\"IntelliJ IDEA 2025.2.5"\bin\idea64.exe  D:\750000APIGateway\apigw\service
start C:\"Program Files"\JetBrains\"IntelliJ IDEA 2025.2.5"\bin\idea64.exe  D:\750000APIGateway\apic-public\service
start C:\"Program Files"\JetBrains\"IntelliJ IDEA 2025.2.5"\bin\idea64.exe  D:\750000APIGateway\API-Ops\service

::start IDEA Community
start C:\"Program Files"\JetBrains\"IntelliJ IDEA Community Edition 2025.2.5"\bin\idea64.exe D:\900000GuanHaoEncyclopedia\PersonalKnowledgeManagement
start C:\"Program Files"\JetBrains\"IntelliJ IDEA Community Edition 2025.2.5"\bin\idea64.exe D:\900000GuanHaoEncyclopedia\DeveloperNotes

:: start VSCode
start C:\"Program Files"\VSCode-huawei\VSCode-huawei.exe D:\750000APIGateway\apigw\ui\admin
start C:\"Program Files"\VSCode-huawei\VSCode-huawei.exe D:\750000APIGateway\apigw\ui\portal
:: start Navicat
start C:\"Program Files"\PremiumSoft\"Navicat Premium 17"\navicat.exe

:: start Obsidian
start C:\"Program Files"\Obsidian\Obsidian.exe D:\900000GuanHaoEncyclopedia\DeveloperNotes

:: start FastStone Capture
start C:\"Program Files (x86)"\"FastStone Capture"\FSCapture.exe

:: start GitHubDesktop
start C:\Users\m30026548\AppData\Local\GitHubDesktop\GitHubDesktop.exe

::normal work
start C:\"Program Files (x86)"\YINWANGWeLink\YINWANGWeLink.exe

::normal work
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Default" https://w3.huawei.com/next/indexa.html

::yinwang op  Dinosaur 
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 3" https://console.ywit-op.yinwang.com/
::yinwang tenant Elephant
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 4" https://console.ywit.yinwang.com/home/#/index
::yinwang test op Pandan
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 8" https://console.ywit-op-beta.yinwang.com/

::yinwang test tenant Fox
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 5" https://console.ywit-beta.yinwang.com/home/#/index

::common user Rabbit
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 6" https://console.ywit-beta.yinwang.com/home/#/index

::common user Penguin
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 7" https://console.ywit-beta.yinwang.com/home/#/index

```

## 3.刘涛 wx1381159
刘涛 wx1381159 2026-01-20 19:37
你好，YWbeta新环境MQS平台消息，毛工，你这边可以看么？

![84461967-4EA3-4125-A2EF-46CA0CCD11B1.png](pic20260120/84461967-4EA3-4125-A2EF-46CA0CCD11B1.png)

System error occurred: Unable to execute unmarshal.

消息id是3f75e4d9a4c14cc7bc2bcd3cece14221，7c98125c57584ad198144afc2ef283f2


### 3.1 T_ARM_Iright_Group_message_ywbeta有两个应用
T_ARM_Iright_Group_message_ywbeta

![2026-01-22_092245.png](pic20260122/2026-01-22_092245.png)

e533cdc810864e298644caf88e3ce47e

00000000000000000000000000000676


### 3.2
昨天9点16发送了一个消息
![2026-01-22_092814.png](pic20260122/2026-01-22_092814.png)
消息ID:
de5cc12e14a245608567f157bc6308bd

consumerGroup
"5d2a27c83b774a23a43dd8c2f53c2f56_T_ARM_Iright_Group_message_ywbeta_PdmPublicService_his_bom_ywbeta_PDM_master_region"

为什么会消费失败


![2026-01-22_093333.png](pic20260122/2026-01-22_093333.png)

订阅端有成功启动，但是消费失败


消费消息的线程卡死了，然后重试了16次还是没消费成功。

![2026-01-22_095121.png](pic20260122/2026-01-22_095121.png)


消费失败 还能查到消息内容吗？？平台为啥查不到消息内容



消息id是3f75e4d9a4c14cc7bc2bcd3cece14221，7c98125c57584ad198144afc2ef283f2


```text
com.huawei.it.roma.liveflow.common.shared.mqs.http.RestException: Call MQS API Failed. resp: {"time":"2026-01-21 09:59:17","source":"API-Gateway","status":403,"message":"Client is Locked in 5 Min"}

	at com.huawei.it.roma.liveflow.common.shared.mqs.http.SimpleClient.execute(SimpleClient.java:228)
	at com.huawei.it.roma.liveflow.common.shared.mqs.http.SimpleClient.post(SimpleClient.java:129)
	at com.huawei.it.roma.liveflow.common.shared.mqs.http.SimpleProducer.send(SimpleProducer.java:93)
	at com.huawei.it.roma.liveflow.common.shared.mqs.http.SimpleProducer.send(SimpleProducer.java:66)
	at com.huawei.it.roma.ruleengine.components.mqs.TbMqsProducerNode.sendMessage(TbMqsProducerNode.java:243)
	at com.huawei.it.roma.ruleengine.components.mqs.TbMqsProducerNode.publishMsg(TbMqsProducerNode.java:235)
	at com.huawei.it.roma.ruleengine.components.mqs.TbMqsProducerNode.lambda$publishMessageAsync$2(TbMqsProducerNode.java:217)
	at com.google.common.util.concurrent.TrustedListenableFutureTask$TrustedFutureInterruptibleTask.runInterruptibly(TrustedListenableFutureTask.java:131)
	at com.google.common.util.concurrent.InterruptibleTask.run(InterruptibleTask.java:75)
	at com.google.common.util.concurrent.TrustedListenableFutureTask.run(TrustedListenableFutureTask.java:82)
	at java.util.concurrent.ForkJoinTask$RunnableExecuteAction.exec(ForkJoinTask.java:1402)
	at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
	at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
	at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
	at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:175)
```
search: Client is Locked in 5 Min




https://12345.huawei.com/unidesk/portal/#/case_details?caseId=KT00354554&source=ITS


## 4.
里面有appkey
林宏 60083227


[root (2).log](pic20260122/root%20%282%29.log)


## 5.
沈图一 EW30045293
人活一口气，得出顺了才舒心。死磕到底，决不放弃！
![266CD89F-D44B-43FB-C82A-708F58051E74.png](pic20260122/266CD89F-D44B-43FB-C82A-708F58051E74.png)
姓名 shentuyi 30045293
账号 s30045293
手机 +86 17611685653(主号)
邮箱 shentuyi1@h-partners.com
服务部门 资源中心(质量与流程IT部)
地址 中国(China)-武汉(Wuhan)-东湖高新区未来智汇城A3
座位 F03-093S
当地时间 12:20（24小时制）
邮编 430000
## 4.op发租户如何配置

![2026-01-22_110836.png](pic20260122/2026-01-22_110836.png)


## 5.关于九华山公寓租赁政策及租金价格通知（2026年2月1日始租金五折）

https://3ms.huawei.com/km/groups/2030849/blogs/details/21821081


https://3ms.huawei.com/km/groups/2030849/home?l=zh-cn&moduleId=1124231638576971776#category=9530578

![758A6934-9707-4861-F496-3D9D2A8FE545.jpg](pic20260122/758A6934-9707-4861-F496-3D9D2A8FE545.jpg)


## 6.春运团体火车票


https://itravel.hwht.com/librabi/content/detail/8dd49891-b491-4c3c-a1dc-1b580e3b1a41?wmcode=htcl_pc_cyhcp_2026


## 7.张建华 租户发OP侧

[Video_2026-01-21_104303.wmv](../../VideoRecoder/Video_2026-01-21_104303.wmv)



## 8.刘涛 wx1381159  OP发租户

[Video_2026-01-22_104630.wmv](../../VideoRecoder/Video_2026-01-22_104630.wmv)
[Video_2026-01-22_113609.wmv](../../VideoRecoder/Video_2026-01-22_113609.wmv)



在LiveEvent

T_ARM_Iright_Group_message_ywbeta

![2026-01-22_152350.png](pic20260122/2026-01-22_152350.png)

源事件
5d2a27c83b774a23a43dd8c2f53c2f56   BOM服务

![2026-01-22_153012.png](pic20260122/2026-01-22_153012.png)


```text
console.ywit-beta.yinwang.com/event/#/eventLink/edit/22

Live Event

概览
事件管理
跨区跨租场景
个人中心
文档
系统管理

跨区跨租场景

基本信息
* 事件编排名称 T_ARM_Iright_Group_message_ywbeta
企业名称 8c8b823898bae7f80198bb20e3590002
属主项目ID 5d2a27c83b774a23a43dd8c2f53c2f56
动态分发配置
动态分发用于复杂规则的消息过滤，如，可根据属性值过滤renter_id或bizEnvId，分发对应的内容

源事件
* 订阅项目ID 5d2a27c83b774a23a43dd8c2f53c2f56
* 事件名称 ARM_HEDS_Iright_Group_message / T_ARM_HEDS_Iright_Group_message / YWDC / HEDS运维管理企业
来源标签 *
扩展属性 > 扩展属性详情
模型映射 > 模型映射详情

目的事件
* 目的项目ID 5d2a27c83b774a23a43dd8c2f53c2f56
* 事件名称 ARM_HEDS_Iright_Group_message_ywbeta / T_ARM_Iright_Group_message_ywbeta / YWBETA / null ×
目的标签 *
展开∨
```

> 新跨企租用户旅程
> https://wiki.huawei.com/domains/137/wiki/4138/WIKI202505226909521
> 跨企租--op侧发布租户侧消费 用户旅程
> https://wiki.huawei.com/domains/137/wiki/4138/WIKI20230216759694
> 跨企租--租户侧发布op侧消费 用户旅程
> https://wiki.huawei.com/domains/137/wiki/4138/WIKI20230216759512



ARM_HEDS_Iright_Group_message
![2026-01-22_155219.png](pic20260122/2026-01-22_155219.png)

到LiveFlow搜索编排事件


租户侧的流程是有效的

T_ARM_Iright_Group_message_ywbeta

![2026-01-22_162007.png](pic20260122/2026-01-22_162007.png)

之前的流程没有通

![2026-01-22_162126.png](pic20260122/2026-01-22_162126.png)

有可能是API没有授权

部署版本改成V4后流程跑通


op侧也是，部署版本改成V4后流程跑通

![2026-01-22_163146.png](pic20260122/2026-01-22_163146.png)




## 9.

https://edh.tw/articles/xGZj4JT


## 10.

![C1DCCD5D-AE7C-4E18-E9D6-819832AED83E.png](pic20260122/C1DCCD5D-AE7C-4E18-E9D6-819832AED83E.png)



## 7.张建华 租户发OP侧

[Video_2026-01-21_104303.wmv](../../VideoRecoder/Video_2026-01-21_104303.wmv)

![9AF9ED58-1D2E-40B2-99DB-5BF30096E04F.png](pic20260122/9AF9ED58-1D2E-40B2-99DB-5BF30096E04F.png)

```text
跨区跨租场景

基本信息

事件编排名称: T_CTR_MBS_ILLEGAL_SEAL_PRO_YW_TO_OP
企业名称: 引望
属主项目ID: bb1c6f2e9171420b99df9559795734c5
动态分发配置: 动态分发用于复杂规则的消息过滤，如，可根据属性值过滤renter_id或bizEnvId，分发对应的内容
源事件

订阅项目ID: 客户对账/bb1c6f2e9171420b99df9559795734c5
事件名称: MBS_ILLEGAL_SEAL_PRO / YW贵阳 / 引望
来源标签: CtrService
扩展属性: > 扩展属性详情
内容转换: > 内容转换详情
目的事件

目的项目ID: 客户对账/bb1c6f2e9171420b99df9559795734c5
事件名称: CTR_MBS_ILLEGAL_SEAL_PROD / YW贵阳 / 引望
目的标签: 113704385416306&2c9080e7930105a60193046fc971004f
按钮: 保存并启用、保存、返回
```