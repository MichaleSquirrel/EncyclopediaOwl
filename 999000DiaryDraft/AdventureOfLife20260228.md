Saturday February 28 Day 059 week 9 of 2026

## 1.TodoList


## 2.


## 3.修改密码
3.14159265358979323846264338 3279502884 1971693993751058209749445923078164062862089986280348253421170679


生产环境旧密码  Guan@3279502884Song
生产环境新密码  Guan@1971693993Song

测试环境旧密码  pai@264338
测试环境新密码  Nine@7530U9Bot


CRONTABJOB="* * * * * /bin/sh /data01/ump/mqs-prod/tomcat-mqs-web/bin/scan.sh >> /dev/null"
task_count=$(crontab -l|grep "${CRONTABJOB}"|wc -l)
if [ $task_count -ne 0 ];then
echo "Crontab task is exist."
else
(crontab -l | grep -v "${CRONTABJOB}"; echo "${CRONTABJOB}" ) | crontab -
echo "Crontab task add."
fi

CRONTABJOB="* * * * * /bin/sh /data01/ump/mqs-prod/mqs-rest-api/tomcat-mqs-web/bin/scan.sh >> /dev/null"
task_count=$(crontab -l|grep "${CRONTABJOB}"|wc -l)
if [ $task_count -ne 0 ];then
echo "Crontab task is exist."
else
(crontab -l | grep -v "${CRONTABJOB}"; echo "${CRONTABJOB}" ) | crontab -
echo "Crontab task add."
fi


## 4.


[root@mqs-web00-fromxac classes]# pwd
cd /data01/ump/mqs-prod/tomcat-mqs-web/webapps/mqs/WEB-INF/classes


## 5.


org.apache.jasper.servlet.TldScanner.scanJars At least one JAR was scanned for TLDs yet contained no TLDs.





## 6
![96972236-AA7D-40C1-B92D-3E2CB277395D.png](pic20260228/96972236-AA7D-40C1-B92D-3E2CB277395D.png)

```text
2026-02-27 16:49:36.316 [pro] WebContainer : [60*677][]-2000005546-549b88cc7-29133-T:DFT-lb2dad75-702a-4fb2-a27c-d6cfe8d9bd5c-Td:8c8b823898bae7f80198bb20e3590002] WARN c.h.i.t.b.i.u.IntegrationDataProcessorUtil: ||handleDataList processingClass is null.
2026-02-27 16:49:36.365 [pro] WebContainer : [60*677][]-2000005546-549b88cc7-29133-T:DFT-lb2dad75-702a-4fb2-a27c-d6cfe8d9bd5c-Td:8c8b823898bae7f80198bb20e3590002] WARN c.h.i.t.c.m.MqUtil: ||start MQS producer:[serverAddr]:mq-umpnamesrv00-beta.iywang.com:9776;mq-umpnamesrv01-beta.iywang.com:9776,[topic]:T_TTC_TAX_STAMP_DUTY_MAPPING_YWBETA
2026-02-27 16:49:36.872 [kafka-producer-network-thread | producer-2] INFO o.a.k.c.NetworkClient: [Producer clientId=producer-2] Disconnecting from node -1 due to socket connection setup timeout. The timeout value is 26541 ms.
2026-02-27 16:49:36.872 [kafka-producer-network-thread | producer-2] WARN o.a.k.c.NetworkClient: [Producer clientId=producer-2] Bootstrap broker 7.226.167.125:9092 (id: -1 rack: null) disconnected
2026-02-27 16:49:39.414 [pro] WebContainer : [60*677][]-2000005546-549b88cc7-29133-T:DFT-lb2dad75-702a-4fb2-a27c-d6cfe8d9bd5c-Td:8c8b823898bae7f80198bb20e3590002] ERROR UmpClient: ||Upload large body httpFsClient exception, http p://fts-beta.iywit-beta.iywang.com/file?sha256=85ala959dd3d2e7e5507be591c8d8b7cdf5baee4c5d21c710db3e64ac94f2ee90 com.huawei.his.mqs.client.httpFsException: IOException
at com.huawei.his.mqs.client.httpFsClient.upload(HttpFsClient.java:517) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.his.mqs.client.httpFsClient.upload(HttpFsClient.java:472) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.his.mqs.client.producer.Producer.tryUpload(Producer.java:154) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.his.mqs.client.producer.Producer.processMessageBeforeSend(Producer.java:231) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.his.mqs.client.producer.Producer.send_aroundBody0(Producer.java:335) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.his.mqs.client.producer.Producer$AjcClosure1.run(Producer.java:1) ~[mqs-sdk-3.5.6.0.jar!/:?]
at org.aspectj.runtime.reflect.JoinPointImpl.proceed(JoinPointImpl.java:167) ~[aspectjweaver-1.9.7.jar:3944279131153723455.jar!/:?]
at com.huawei.fin.findi.tpcollector.client.aspect.mqs.TPMqsProducerAspecter.sendAround(TPMqsProducerAspecter.java:54) ~[tplineage-collector-1.5.18.jar!/:?]
at com.huawei.his.mqs.client.producer.Producer.send(Producer.java:327) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.his.mqs.client.producer.Producer.send(Producer.java:301) ~[mqs-sdk-3.5.6.0.jar!/:?]
at com.huawei.it.trc.common.mqs.MqsUtil.sendMessage(MqsUtil.java:199) ~[TaxRuleCommon-core-5.0.1-saas-SNAPSHOT.jar!/:?]
at com.huawei.it.trc.common.mqs.MqsUtil.sendMessage(MqsUtil.java:182) ~[TaxRuleCommon-core-5.0.1-saas-SNAPSHOT.jar!/:?]
at com.huawei.it.tactical.comm.mqs.service.MqsProducerManageService.startProducerAndSendMessage(MqsProducerManageService.java:135) ~[Taxflow-service-impl-5.0.1-saas-SNAPSHOT.jar!/:?]
at com.huawei.it.tactical.comm.mqs.service.MqsProducerManageService.sendMessage(MqsProducerManageService.java:90) ~[Taxflow-service-impl-5.0.1-saas-SNAPSHOT.jar!/:?]
at com.huawei.it.tactical.comm.mqs.service.MqsProducerManageService$$FastClassBySpringCGLIB$$63766a07.invoke(<generated>) ~[Taxflow-service-impl-5.0.1-saas-SNAPSHOT.jar!/:?]
at org.springframework.cglib.proxy.MethodProxy.invoke(MethodProxy.java:218) ~[spring-core-5.3.9-h7.jar!/:5.3.9-h7]
```
curl -H "Content-Type: application/json" -H "appid:b995709d9d0343b2830ba09dbc317f32" -H "token:2RBH8zNegCldqhSd/SowMT2Wg1cZRs/A6rtz1UWn" -H "account:b995709d9d0343b2830ba09dbc317f32" -H "enterprise:8c8b823898bae7f80198bb20e3590002" -X POST -d 'hello' "http://fts-beta.ywit-beta.yinwang.com/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


T_TTC_TAX_STAMP_DUTY_MAPPING_YWBETA

bb090f26685149b88d4990c9f5edbc7c_T_TTC_TAX_STAMP_DUTY_MAPPING_YWBETA_SteServiceSit

Caused by: redis.clients.jedis.exceptions.JedisDataException: ERR invalid password

grep -C 10 "Caused by: redis.clients.jedis.exceptions.JedisDataException: ERR invalid password" catalina.out
grep "ERR invalid password" catalina.out


```shell
permitFileSuffix=.zip,.xlsx,.xls,.txt

#milsecond
cleanKeeptime=7200000

totalSizeMax=10485760

fileSizeMax=5242880

validatorNow=false

maxKeepInMemory=1048576

charset=utf-8

tempFolder=/data01/ump/uploadTmp

tempFilePrefix=wsf-secure-upload

checkFileType=zip

```

## 8.部署成功的依据

[mqs-web00_fromxac_2026-02-28_20-46-16.log](pic20260228/mqs-web00_fromxac_2026-02-28_20-46-16.log)


```shell
2026-02-28 22:30:32,067 [http-nio-8080-exec-4] INFO HicServiceEnterpriseHttpCallAdapter - getAppsByUser-----------------------out-------------{"data":[{"type":"Application","attributes":{"name":"ROMA底座3.0","exts":{"name_abbr_en":"ROMA底座3.0","name_full_en":"roma foundation 3.0","name_full_cn":"ROMA底座3.0"},"appid":"3bbbb3d0b1c54496b0aa3d6f9288793b"},"id":"3bbbb3d0b1c54496b0aa3d6f9288793b"},{"type":"Application","attributes":{"name":"LiveFlow","exts":{"name_abbr_en":"LiveFlow","name_full_en":"LiveFlow-YW-PRO","name_full_cn":"LiveFlow"},"appid":"3d3d41fe77614c6583d47145e87c61d7"},"id":"3d3d41fe77614c6583d47145e87c61d7"},{"type":"Application","attributes":{"name":"规则引擎LiveRule","exts":{"name_abbr_en":"规则引擎LiveRule","name_full_en":"LiveRule-YW-PRO","name_full_cn":"规则引擎LiveRule"},"appid":"5c3ed6c7447244129ff1df677947a8e3"},"id":"5c3ed6c7447244129ff1df677947a8e3"},{"type":"Application","attributes":{"name":"APIG","exts":{"name_abbr_en":"APIG","name_full_en":"YWIT-SERVICE-APIG","name_full_cn":"APIG"},"appid":"b8846618c8d0485e89bdef35f35e63df"},"id":"b8846618c8d0485e89bdef35f35e63df"},{"type":"Application","attributes":{"name":"消息队列MQS","exts":{"name_abbr_en":"消息队列MQS","name_full_en":"Message Queue Service","name_full_cn":"消息队列MQS"},"appid":"b995709d9d0343b2830ba09dbc317f32"},"id":"b995709d9d0343b2830ba09dbc317f32"}]}
28-Feb-2026 22:30:37.677 INFO [Timer-0] com.huawei.foundation.heds.iam.sdk.log.SdkLog.log [4.1.0] iam service health http status: 200
2026-02-28 22:31:26,399 [http-nio-8080-exec-21] INFO HicServiceEnterpriseHttpCallAdapter - getAppsByUser-----------------------out-------------{"data":[{"type":"Application","attributes":{"name":"ROMA底座3.0","exts":{"name_abbr_en":"ROMA底座3.0","name_full_en":"roma foundation 3.0","name_full_cn":"ROMA底座3.0"},"appid":"3bbbb3d0b1c54496b0aa3d6f9288793b"},"id":"3bbbb3d0b1c54496b0aa3d6f9288793b"},{"type":"Application","attributes":{"name":"LiveFlow","exts":{"name_abbr_en":"LiveFlow","name_full_en":"LiveFlow-YW-PRO","name_full_cn":"LiveFlow"},"appid":"3d3d41fe77614c6583d47145e87c61d7"},"id":"3d3d41fe77614c6583d47145e87c61d7"},{"type":"Application","attributes":{"name":"规则引擎LiveRule","exts":{"name_abbr_en":"规则引擎LiveRule","name_full_en":"LiveRule-YW-PRO","name_full_cn":"规则引擎LiveRule"},"appid":"5c3ed6c7447244129ff1df677947a8e3"},"id":"5c3ed6c7447244129ff1df677947a8e3"},{"type":"Application","attributes":{"name":"APIG","exts":{"name_abbr_en":"APIG","name_full_en":"YWIT-SERVICE-APIG","name_full_cn":"APIG"},"appid":"b8846618c8d0485e89bdef35f35e63df"},"id":"b8846618c8d0485e89bdef35f35e63df"},{"type":"Application","attributes":{"name":"消息队列MQS","exts":{"name_abbr_en":"消息队列MQS","name_full_en":"Message Queue Service","name_full_cn":"消息队列MQS"},"appid":"b995709d9d0343b2830ba09dbc317f32"},"id":"b995709d9d0343b2830ba09dbc317f32"}]}
2026-02-28 22:31:26,439 [http-nio-8080-exec-21] INFO UserSessionCacheServiceImpl$2 - loading cache triggered, getPermListByRoleCode: w3_common ,cost: 8 ms.
2026-02-28 22:31:26,987 [http-nio-8080-exec-20] INFO HicServiceEnterpriseHttpCallAdapter - getAppsByUser-----------------------out-------------{"data":[{"type":"Application","attributes":{"name":"ROMA底座3.0","exts":{"name_abbr_en":"ROMA底座3.0","name_full_en":"roma foundation 3.0","name_full_cn":"ROMA底座3.0"},"appid":"3bbbb3d0b1c54496b0aa3d6f9288793b"},"id":"3bbbb3d0b1c54496b0aa3d6f9288793b"},{"type":"Application","attributes":{"name":"LiveFlow","exts":{"name_abbr_en":"LiveFlow","name_full_en":"LiveFlow-YW-PRO","name_full_cn":"LiveFlow"},"appid":"3d3d41fe77614c6583d47145e87c61d7"},"id":"3d3d41fe77614c6583d47145e87c61d7"},{"type":"Application","attributes":{"name":"规则引擎LiveRule","exts":{"name_abbr_en":"规则引擎LiveRule","name_full_en":"LiveRule-YW-PRO","name_full_cn":"规则引擎LiveRule"},"appid":"5c3ed6c7447244129ff1df677947a8e3"},"id":"5c3ed6c7447244129ff1df677947a8e3"},{"type":"Application","attributes":{"name":"APIG","exts":{"name_abbr_en":"APIG","name_full_en":"YWIT-SERVICE-APIG","name_full_cn":"APIG"},"appid":"b8846618c8d0485e89bdef35f35e63df"},"id":"b8846618c8d0485e89bdef35f35e63df"},{"type":"Application","attributes":{"name":"消息队列MQS","exts":{"name_abbr_en":"消息队列MQS","name_full_en":"Message Queue Service","name_full_cn":"消息队列MQS"},"appid":"b995709d9d0343b2830ba09dbc317f32"},"id":"b995709d9d0343b2830ba09dbc317f32"}]}
2026-02-28 22:31:27,026 [http-nio-8080-exec-20] WARN AuthenticationController - Gets current user profile fail The SSO context object is empty. The possible cause is that the SSO context object fails to be initialized.
2026-02-28 22:31:35,903 [http-nio-8080-exec-28] INFO HicServiceEnterpriseHttpCallAdapter - getAppsByUser-----------------------out-------------{"data":[{"type":"Application","attributes":{"name":"ROMA底座3.0","exts":{"name_abbr_en":"ROMA底座3.0","name_full_en":"roma foundation 3.0","name_full_cn":"ROMA底座3.0"},"appid":"3bbbb3d0b1c54496b0aa3d6f9288793b"},"id":"3bbbb3d0b1c54496b0aa3d6f9288793b"},{"type":"Application","attributes":{"name":"LiveFlow","exts":{"name_abbr_en":"LiveFlow","name_full_en":"LiveFlow-YW-PRO","name_full_cn":"LiveFlow"},"appid":"3d3d41fe77614c6583d47145e87c61d7"},"id":"3d3d41fe77614c6583d47145e87c61d7"},{"type":"Application","attributes":{"name":"规则引擎LiveRule","exts":{"name_abbr_en":"规则引擎LiveRule","name_full_en":"LiveRule-YW-PRO","name_full_cn":"规则引擎LiveRule"},"appid":"5c3ed6c7447244129ff1df677947a8e3"},"id":"5c3ed6c7447244129ff1df677947a8e3"},{"type":"Application","attributes":{"name":"APIG","exts":{"name_abbr_en":"APIG","name_full_en":"YWIT-SERVICE-APIG","name_full_cn":"APIG"},"appid":"b8846618c8d0485e89bdef35f35e63df"},"id":"b8846618c8d0485e89bdef35f35e63df"},{"type":"Application","attributes":{"name":"消息队列MQS","exts":{"name_abbr_en":"消息队列MQS","name_full_en":"Message Queue Service","name_full_cn":"消息队列MQS"},"appid":"b995709d9d0343b2830ba09dbc317f32"},"id":"b995709d9d0343b2830ba09dbc317f32"}]}
2026-02-28 22:31:35,987 [http-nio-8080-exec-4] WARN AuthenticationController - Gets current user profile fail The SSO context object is empty. The possible cause is that the SSO context object fails to be initialized.
2026-02-28 22:31:36,027 [http-nio-8080-exec-16] WARN AuthenticationController - Gets current user profile fail The SSO context object is empty. The possible cause is that the SSO context object fails to be initialized.
2026-02-28 22:31:36,195 [http-nio-8080-exec-25] INFO HicServiceEnterpriseHttpCallAdapter - getAppsByUser-----------------------out-------------{"data":[{"type":"Application","attributes":{"name":"ROMA底座3.0","exts":{"name_abbr_en":"ROMA底座3.0","name_full_en":"roma foundation 3.0","name_full_cn":"ROMA底座3.0"},"appid":"3bbbb3d0b1c54496b0aa3d6f9288793b"},"id":"3bbbb3d0b1c54496b0aa3d6f9288793b"},{"type":"Application","attributes":{"name":"LiveFlow","exts":{"name_abbr_en":"LiveFlow","name_full_en":"LiveFlow-YW-PRO","name_full_cn":"LiveFlow"},"appid":"3d3d41fe77614c6583d47145e87c61d7"},"id":"3d3d41fe77614c6583d47145e87c61d7"},{"type":"Application","attributes":{"name":"规则引擎LiveRule","exts":{"name_abbr_en":"规则引擎LiveRule","name_full_en":"LiveRule-YW-PRO","name_full_cn":"规则引擎LiveRule"},"appid":"5c3ed6c7447244129ff1df677947a8e3"},"id":"5c3ed6c7447244129ff1df677947a8e3"},{"type":"Application","attributes":{"name":"APIG","exts":{"name_abbr_en":"APIG","name_full_en":"YWIT-SERVICE-APIG","name_full_cn":"APIG"},"appid":"b8846618c8d0485e89bdef35f35e63df"},"id":"b8846618c8d0485e89bdef35f35e63df"},{"type":"Application","attributes":{"name":"消息队列MQS","exts":{"name_abbr_en":"消息队列MQS","name_full_en":"Message Queue Service","name_full_cn":"消息队列MQS"},"appid":"b995709d9d0343b2830ba09dbc317f32"},"id":"b995709d9d0343b2830ba09dbc317f32"}]}




```
