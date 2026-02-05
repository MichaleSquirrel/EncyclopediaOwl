Wednesday January 28 Day 028 week 5 of 2026

## 1.TodoList
1. 为什么会耳背
2. 两个截图软件
3. 黄金鉴定工具

## 2.总结发大文件失败的问题处理过程

录屏文件
[Video_2026-01-27_215754.wmv](../../VideoRecoder/Video_2026-01-27_215754.wmv)

### 2.1 去生产环境查看日志

收件人:lishengpei<lishengpei1@huawei.com>;lishuangping<lishuangping1@h-partners.com>;lifengting (A)<lifengting9@h-partners.com>;jiangheming (A)<jiangheming1@h-partners.com>;likangxing (A)<likangxing3@h-partners.com>;yangzhenglong<yangzhenglong1@h-partners.com>
抄送:Dengchunping(Ken,IASBU)<dengchunping@huawei.com>;Xuqinwen<xuqinwen@huawei.com>;liyingdong<liyingdong8@huawei-partners.com>;liufan (G)<liufan137@h-partners.com>;yangzhongyan<yangzhongyan2@h-partners.com>;huangxinyuan (D)<huangxinyuan3@h-partners.com>;wuliuxin<wuliuxin@h-partners.com>;chenlin (CI)<chenlin248@h-partners.com>;zhangkai (ET)<zhangkai454@h-partners.com>;sangrui (A)<sangrui2@h-partners.com>

主题:【资源与连接】【融合联接】【MQS】IT生产账号口令申请
【资源与连接】【MQS】IT生产账号口令申请
事件单申请口令仅能用于事件定位查询类操作，禁止使用口令进行增删改类的变更操作，请审批人关注；
IM26012700277
FTS服务上传文件失败，需要查看日志定位问题
操作内容列清晰，1、查看服务器日志（kweshcsitd01130、kweshcsitd01128）
毛关松 30026548

截图如下:
![PixPin_2026-01-28_11-44-20.png](pic20260128/PixPin_2026-01-28_11-44-20.png)


20:55 李胜沛回九华山，办公电脑接入会议

### 2.2  PAM生成生产环境账号

Privileged Access Management

![PixPin_2026-01-28_12-05-58.png](pic20260128/PixPin_2026-01-28_12-05-58.png)

![2026-01-28_120846.png](pic20260128/2026-01-28_120846.png)

![2026-01-28_121237.png](pic20260128/2026-01-28_121237.png)


### 2.3 用户日志

```shell
2026-01-27 16:10:59,002 [itemVenCapacityConsumerUMPProcessorThread-1] INFO  ItemVendorFinalGrossSupplyProcessor:93 - 发送消息给UMP2026-01-27 16:10:54 to 2026-01-27 16:10:59
2026-01-27 16:10:59,019 [NettyClientSelector@12.11.1.31@7b641e9f7ed047bb92608da655dbd382_T_SDM_ITEM_VENDOR_CAPACITY_G_PP_producer_default_3-5-4-2_1] INFO  RocketmqRemoting:95 - closeChannel: close the connection to remote address[10.19.1.98:20911] result: true
2026-01-27 16:10:59,019 [itemVenCapacityConsumerUMPProcessorThread-1] INFO  AbstractEipUmpService:342 - UMPSend【T_SDM_ITEM_VENDOR_CAPACITY_G_PP】stopSendMessage SUCCESS
2026-01-27 16:10:59,019 [itemVenCapacityConsumerUMPProcessorThread-1] ERROR ExceptionHandler:227 - Code:[JALOR_EX$发送消息给UMP异常.Failed to upload large message body$],User:[930000000000076],[Error:Missed Message[See log for detail]:发送消息给UMP异常.Failed to upload large message body], URI:[/publicservices/sdm/netItemVendorSupplymatching/getEsupplierInputData]
com.huawei.it.jalor5.security.SecurityApplicationException: Missed Message[See log for detail]:发送消息给UMP异常.Failed to upload large message body
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.process(ItemVenCapacityConsumerUMPProcessor.java:90) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor$$FastClassBySpringCGLIB$$68cf58f1.invoke(<generated>) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218) ~[spring-core-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.invokeJoinpoint(CglibAopProxy.java:792) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:163) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:762) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at com.huawei.it.risk.common.interceptor.AsyncMessageProcessorInterceptor.invoke(AsyncMessageProcessorInterceptor.java:70) ~[risk-core-0.0.1-SNAPSHOT.jar!/:?]
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:762) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:97) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.CglibAopProxy$CglibMethodInvocation.proceed(CglibAopProxy.java:762) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at org.springframework.aop.framework.CglibAopProxy$DynamicAdvisedInterceptor.intercept(CglibAopProxy.java:707) ~[spring-aop-5.3.34.jar!/:5.3.34]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor$$EnhancerBySpringCGLIB$$72225305.process(<generated>) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.common.internal.impl.AsyncProceedThread.call$original$lc6iUHzX(AsyncProceedThread.java:51) ~[risk-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.common.internal.impl.AsyncProceedThread.call$original$lc6iUHzX$accessor$iNrmbZWO(AsyncProceedThread.java) ~[risk-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.common.internal.impl.AsyncProceedThread$auxiliary$4nPutMUY.call(Unknown Source) ~[risk-core-0.0.1-SNAPSHOT.jar!/:?]
	at org.apache.skywalking.apm.plugin.jdk.threading.ThreadingMethodInterceptor_internal.intercept(InstanceMethodInterTemplate.java:87) ~[?:?]
	at com.huawei.it.risk.common.internal.impl.AsyncProceedThread.call(AsyncProceedThread.java) ~[risk-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.common.internal.impl.AsyncProceedThread.call(AsyncProceedThread.java:28) ~[risk-core-0.0.1-SNAPSHOT.jar!/:?]
	at java.util.concurrent.FutureTask.run(FutureTask.java:266) ~[?:1.8.0_382]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) ~[?:1.8.0_382]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) ~[?:1.8.0_382]
	at java.lang.Thread.run(Thread.java:750) ~[?:1.8.0_382]
Caused by: com.huawei.his.mqs.common.exception.UmpException: Failed to upload large message body
	at com.huawei.his.mqs.client.producer.Producer.processMessageBeforeSend(Producer.java:198) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.send(Producer.java:278) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.send$original$62xR2XMn(Producer.java:244) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.send$original$62xR2XMn$accessor$3vlGyErw(Producer.java) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer$auxiliary$0UcEY7K6.call(Unknown Source) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at org.apache.skywalking.apm.agent.core.plugin.interceptor.enhance.InstMethodsInter.intercept(InstMethodsInter.java:86) ~[skywalking-agent.jar:8.8.0]
	at com.huawei.his.mqs.client.producer.Producer.send(Producer.java) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.splitSendMsg(ItemVenCapacityConsumerUMPProcessor.java:235) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.sendMsg(ItemVenCapacityConsumerUMPProcessor.java:161) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.process(ItemVenCapacityConsumerUMPProcessor.java:86) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	... 23 more
Caused by: com.huawei.his.mqs.common.exception.UmpException: Upload large body httpFsClient failed, http://fts-kwe.yinwang.com/file?sha256=082e1cfe587a215ceee219afe4d6f4aa76fcc73c8a574c29496e9d245323bb5b
	at com.huawei.his.mqs.client.producer.Producer.tryUpload(Producer.java:147) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.processMessageBeforeSend(Producer.java:190) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.send(Producer.java:278) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.send$original$62xR2XMn(Producer.java:244) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer.send$original$62xR2XMn$accessor$3vlGyErw(Producer.java) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.his.mqs.client.producer.Producer$auxiliary$0UcEY7K6.call(Unknown Source) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at org.apache.skywalking.apm.agent.core.plugin.interceptor.enhance.InstMethodsInter.intercept(InstMethodsInter.java:86) ~[skywalking-agent.jar:8.8.0]
	at com.huawei.his.mqs.client.producer.Producer.send(Producer.java) ~[mqs-sdk-3.5.4.2.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.splitSendMsg(ItemVenCapacityConsumerUMPProcessor.java:235) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.sendMsg(ItemVenCapacityConsumerUMPProcessor.java:161) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	at com.huawei.it.risk.pursdm.itemvendorcapacity.service.impl.ItemVenCapacityConsumerUMPProcessor.process(ItemVenCapacityConsumerUMPProcessor.java:86) ~[risk-purSdm-core-0.0.1-SNAPSHOT.jar!/:?]
	... 23 more

```

通过MQS页面查询，发现别的应用发送大消息都是正常的，
![2026-01-28_122510.png](pic20260128/2026-01-28_122510.png)
![2026-01-28_122248.png](pic20260128/2026-01-28_122248.png)

并查看消息内容，内容也是正常的
![2026-01-28_122719.png](pic20260128/2026-01-28_122719.png)

说明FTS服务正常



考虑是不是有防火墙？
```shell
vim fts.access.log

/12.11.1.31
没有搜索到内容
```
![2026-01-28_141357.png](pic20260128/2026-01-28_141357.png)

```shell
vim error.log

/082e1cfe587a215ceee219afe4d6f4aa76fcc73c8a574c29496e9d245323bb5b
```

![2026-01-28_142459.png](pic20260128/2026-01-28_142459.png)

![2026-01-28_142357.png](pic20260128/2026-01-28_142357.png)
10.16.15.251就是ADS的ip

FTS服务器磁盘没有满，
![2026-01-28_142742.png](pic20260128/2026-01-28_142742.png)

### 2.4 切换到用户服务器排查问题

Topic：T_SDM_ITEM_VENDOR_CAPACITY_G_PP
Appid：7b641e9f7ed047bb92608da655dbd382

{
"a02_application_desc": "采购供给管理服务",
"a02_name_en": "Procurement Supply Management Service",
"a02_application_alias": "7b641e9f7ed047bb92608da655dbd382",
"a02_name_abbreviation": "7b641e9f7ed047bb92608da655dbd382",
"a02_name_cn": "采购供给管理服务"
}



![2026-01-28_143439.png](pic20260128/2026-01-28_143439.png)

![2026-01-28_144614.png](pic20260128/2026-01-28_144614.png)
周秋 30078305

在服务器中执行curl命令
```shell
curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000133" -H "token:秘钥" -H "account:op_rabbitmq" -H "enterprise:88888888888888888888xxxxxxxx" -X POST -d 'hello' "http://7.xx.xx.xx:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
curl -H "Content-Type: application/json" -H "appid:7b641e9f7ed047bb92608da655dbd382" -H "token:yGCHMO8o5XRsCGy6D2Ej00HliQkg/LN1NZLnHAwM" -H "account:7b641e9f7ed047bb92608da655dbd382" -H "enterprise:2c9080e7930105a60193046fc971004f" -X POST -d 'hello' "http://fts-kwe.yinwang.com/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```
![2026-01-28_144839.png](pic20260128/2026-01-28_144839.png)

```text
application/json" -H "appid:7b641e9f7ed047bb92608da655dbd382" -H "token:yGCHMO8o5XRsCGy6D2Ej00HliQkg/LN1NZLnHAwM" -H "account:op_rabbitmq" -H "enterprise:2c9080e7930105a60193046fc971004f" -X POST -d 'hello' "http://7.xx.xx.xx:80/file?sha256=2cf24dba5fb0a30

```
![2026-01-28_145433.png](pic20260128/2026-01-28_145433.png)

成功执行，说明FTS服务正常，没有防火墙，采购供给管理服务服务器与FTS之前访问正常

### 2.5 切换到FTS服务器

MQS版本3.5.4.2

许跃生说：有可能需要改一个参数  client_body_buffer_size，把这个参数改大一点


小消息也发不了，找个一个小消息进行查看，发现其实也是大消息
http://fts-kwe.yinwang.com/file?sha256=aa6f3c00284cebe9df7542220b815b2585bc8af44ce6057a449bfbfc3b2040d7

![2026-01-28_150404.png](pic20260128/2026-01-28_150404.png)

### 2.6

许跃生说：创建一下这个目录
/data01/ump/copy_file_error.log

![2026-01-28_150650.png](pic20260128/2026-01-28_150650.png)

因申请的是umpadmin账号，无法创建


以前财经也说消息

### 2.7 切换到用户服务器排查问题

在服务器中执行curl命令
```shell
curl -H "Content-Type: application/json" -H "appid:7b641e9f7ed047bb92608da655dbd382" -H "token:yGCHMO8o5XRsCGy6D2Ej00HliQkg/LN1NZLnHAwM" -H "account:7b641e9f7ed047bb92608da655dbd382" -H "enterprise:2c9080e7930105a60193046fc971004f" -X POST --data-binary @/path/to/file.zip "http://fts-kwe.yinwang.com/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
curl -H "Content-Type: application/json" -H "appid:7b641e9f7ed047bb92608da655dbd382" -H "token:yGCHMO8o5XRsCGy6D2Ej00HliQkg/LN1NZLnHAwM" -H "account:7b641e9f7ed047bb92608da655dbd382" -H "enterprise:2c9080e7930105a60193046fc971004f" -X POST --data-binary @/path/to/file.zip "http://fts-kwe.yinwang.com/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
# 以下命令用于计算文件sha256值
sha256sum 文件
```

![2026-01-28_151933.png](pic20260128/2026-01-28_151933.png)

![2026-01-28_152445.png](pic20260128/2026-01-28_152445.png)


```shell
-rw-r--r-- 1 root root 51M 1月 19 17:58 supervisord.log.5
[webadmin@2000003286-648b87bbc6-w58ln applog]$ sha256sum msa-start-stdout.log.1
028ebfdcba64bb2a96623f4c1fb67f4f2438725dad4543d68b84eced7ae55a5c msa-start-stdout.log.1
[webadmin@2000003286-648b87bbc6-w58ln applog]$ pwd
/applog
[webadmin@2000003286-648b87bbc6-w58ln applog]$ curl -H "Content-Type: application/json" -H "appid:7b641e9f7ed047bb92608da655dbd382" -H "token:yGCHM08o5XRsCGy6DZEj00HLiQKg/LNlNZLnHAwM" -H "account:7b641e9f7ed047bb92608da655dbd382" -H "enterprise:2c9080e7930105a60193046fc971004f" -X POST --data-binary @/applog/msa-start-stdout.log.1 "http://fts-kwe.yinwang.com/file?sha256=028ebfdcba64bb2a96623f4c1fb67f4f2438725dad4543d68b84eced7ae55a5c"
Internal Error

```
![2026-01-28_153222.png](pic20260128/2026-01-28_153222.png)

```shell
rw------- 1 root root 11M 1月 19 21:54 supervisord.log.5
[root@2000003286-648b87bbc6-w58ln applog]# sha256sum test.log
f0f36fe6bc1061d7969ba807d1ba7df93f535899e7831aa167b8d87c2ad457d9  test.log
[root@2000003286-648b87bbc6-w58ln applog]# curl -H "Content-Type: application/json" -H "appid:7b641e9f7ed047bb92608da655dbd382" -H "token:yGCHM08o5XRsCGy6DZEj00HLiQKg/LNlNZLnHAwM" -H "account:7b641e9f7ed047bb92608da655dbd382" -H "enterprise:2c9080e7930105a60193046fc971004f" -X POST --data-binary @/applog/test.log "http://fts-kwe.yinwang.com/file?sha256=f0f36fe6bc1061d7969ba807d1ba7df93f535899e7831aa167b8d87c2ad457d9"
2026012701f0f36fe6bc1061d7969ba807d1ba7df93f535899e7831aa167b8d87c2ad457d9
[root@2000003286-648b87bbc6-w58ln applog]#
```

![17C6CE40-F32F-42C9-BED4-F83C2B8980B6.png](pic20260128/17C6CE40-F32F-42C9-BED4-F83C2B8980B6.png)
下游是做什么的？

![1EB3CAE8-2D8D-43ED-BFE3-677EDD80D041.png](pic20260128/1EB3CAE8-2D8D-43ED-BFE3-677EDD80D041.png)
![ScreenShot_20260128090815.PNG](pic20260128/ScreenShot_20260128090815.PNG)

IM26012700277事件单号

后面业务在分析为什么不是全量的消息为什么也这么大





## 3.新截图工具

https://pixpin.cn/

![2026-01-28_101235.png](pic20260128/2026-01-28_101235.png)

![2026-01-28_101253.png](pic20260128/2026-01-28_101253.png)

![2026-01-28_101310.png](pic20260128/2026-01-28_101310.png)

![PixPin_2026-01-28_10-18-40.png](pic20260128/PixPin_2026-01-28_10-18-40.png)


![PixPin_2026-01-28_10-20-27.png](pic20260128/PixPin_2026-01-28_10-20-27.png)


> PixPin长截图、滚动截图软件
> https://3ms.huawei.com/km/blogs/details/22098404
>
> Audacity音频软件
> https://3ms.huawei.com/km/blogs/details/22069635?l=zh-cn
>
> ASR声纹识别说话人错误率测评
> https://3ms.huawei.com/km/blogs/details/21769852?l=zh-cn

## 4.

> Clawdbot一夜爆红，首个0员工公司诞生！7×24h永不下班【转载】
> https://jx.huawei.com/community/comgroup/postsDetails?postId=2ab87d84443b475b91037337093c8432&noTop=true&type=freePost&welink_open_uri=aDU6Ly80NzE2NTE3MzE0Nzc5NTcvaHRtbC9pbmRleC5odG1sIy9qeC9kZXRhaWw/aWQ9MmFiODdkODQ0NDNiNDc1YjkxMDM3MzM3MDkzYzg0MzImdHlwZT1mcmVlX3Bvc3QmdXJsPQ==
> Clawdbot一夜爆红，首个0员工公司诞生！7×24h永不下班
> https://www.toutiao.com/article/7599500469068726784/?app=news_article&category_new=__all__&module_name=Android_tt_others&share_did=MS4wLjACAAAAP_PlmevAbQWbSii9EQ0VMaSdzg8oOnVtgEb-rNWgWhy-LWDeDM1bQJIrCuty2mJk&share_token=6f678111-1ee2-4581-8539-e769cd3b084e&share_uid=MS4wLjABAAAAuVVZC3PNnauQ6j2Roq4z2bdR5HW3m0NIWu7zbsLZXFE&timestamp=1769442345&tt_from=sys_share&upstream_biz=Android_others&utm_campaign=client_share&utm_medium=toutiao_android&utm_source=sys_share&source=m_redirect&wid=1769584551951
>
>
> 【5分钟上手Clawdbot + M2.1全流程-哔哩哔哩】 https://b23.tv/Q6yR996
>
>
> 内网大模型应用集成实践
> https://3ms.huawei.com/km/blogs/details/22103513?l=zh-cn

## 5.MQS CentOS 升级
李胜沛 00847799 2026-01-27 12:10
kweshcsitd01407
kweshcsitd01408
kweshcsitd01052
这三台，我看了下没有java和nginx进程，应该是没用的，下周变更关机先吧
李胜沛 00847799 2026-01-27 12:11
op侧的
毛关松 30026548 2026-01-27 12:11
好
李胜沛 00847799 2026-01-27 12:24
@毛关松 你跟仲严一起看下，先排个优先级，对于portal，tracker这些对业务影响小的，可以先安排升级OS
毛关松 30026548 2026-01-27 12:24
好
李胜沛 00847799 2026-01-28 10:34
OP侧的两台FTS，没用流量，升级无风险，也可以放在第一批升OS
毛关松 30026548 2026-01-28 10:36
好
李胜沛 00847799 2026-01-28 10:36
kweshcsitd00260
kweshcsitd00251

![9FB70233-1236-4DDF-83D8-CD63E5B60DE5.png](pic20260128/9FB70233-1236-4DDF-83D8-CD63E5B60DE5.png)
李胜沛 00847799 2026-01-28 10:37
我觉得MQS除了broker，其他的其实我们稳一点应该都能升上去
broker最后搞

李胜沛 00847799 2026-01-28 10:39
我们下周月结结束后，先把MQS没用的那几台删除，把FTS的OS升级
关松你先搞个镜像主机把FTS部署起来
然后到时替换系统盘的时候，直接替换FTS私有镜像
毛关松 30026548 2026-01-28 10:39
好的
李胜沛 00847799 2026-01-28 10:39
私有镜像你搞过吗
毛关松 30026548 2026-01-28 10:40
没有


李胜沛 00847799 2026-01-28 10:40
![19839F13-B833-4ADA-D421-37A76DCE54BC.png](pic20260128/19839F13-B833-4ADA-D421-37A76DCE54BC.png)

你今天研究下
双平搞过
他有经验
毛关松 30026548 2026-01-28 10:40
好
李胜沛 00847799 2026-01-28 10:40
1、申请镜像主机
2、在镜像主机里面部署FTS
3、制作EC2镜像
李胜沛 00847799 2026-01-28 10:41
4、替换系统盘，选择自己制作的私有镜像
前面3步，可以这周搞
第4步变更的时候搞



## 6.自己在测试环境部署一个Elasticsearch



## 7.引望选择直接连接
![2026-01-28_165145.png](pic20260128/2026-01-28_165145.png)



## 8.云上创建私有镜像

> 云上创建私有镜像
> https://3ms.huawei.com/km/blogs/details/13761723
> 制作镜像主机
> https://3ms.huawei.com/km/groups/3958772/blogs/details/21944754
>


### 8.1 申请主机制作镜像
![2026-01-28_174558.png](pic20260128/2026-01-28_174558.png)

### 8.2 替换系统盘


### 8.3 找苏景国从华为云推到私有镜像

苏景国 30079145

然后私有镜像就有了


## 9.如何登录LiveOps平台

生产环境
https://console.ywit-op.yinwang.com/liveops/#/home

测试环境租户侧
https://console.ywit-beta.yinwang.com/liveops/#/home

测试环境op侧
https://console.ywit-op-beta.yinwang.com/liveops/#/home

https://console.ywit-op-beta.yinwang.com/liveops/#/home


LiveOps op侧部署MQS 测试环境



生产环境OP侧 部署FTS


```lua
[root@shapheds04616 lua]# cat config.lua
-- config file

local _M = {}

_M['nodes_ip'] = {
    ['01'] = '10.201.32.169',
    ['02'] = '10.201.32.53'
}

_M['sgov_auth_url'] = 'https://oauth2-op-beta.yinwang.com/umws4login/services/Authentication'

_M['token_expire_seconds'] = 180

_M['his3_iam_auth_url'] = 'https://apig.hieds.net/api/iam/auth/token'

_M['auth_white_list'] = {
    'XXXXXXXXXXXXXXXXXXXXXXXXX'
}

return _M
```

明天问一下李双平
生产环境Op侧这几个参数有知道的吗？
![2026-01-28_204640.png](pic20260128/2026-01-28_204640.png)


![2026-01-28_210521.png](pic20260128/2026-01-28_210521.png)


![2026-01-29_101218.png](pic20260129/2026-01-29_101218.png)

