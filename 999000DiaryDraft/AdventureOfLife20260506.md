Wednesday May 6 Day 126 week 19 of 2026

## 1.TodoList
1. 5月4号工作总结  
2. 提交变更计划，准备变更评审  
3. 学习UML教程



## 2.MCA课程学习进度

2026年05月6号学习进展：
1. 学习《UML面向对象分析、建模与设计》  
   大概用时：8小时


## 3.5月4号工作总结  
  
5月4号测试环境租户侧的服务器升级了3台，测试了优化后的脚本，脚本还是挺好用的。  
  
![2026-05-06_084505.png](resource20260506/2026-05-06_084505.png)  
  
遇到的问题:  
1. 把2组2从中的一组通过 mqadmin updateBrokerConfig 改为只读，但是master的OutTPS，总是不能归零。观察了一天，master的OutTPS都没有归零，最后只升级了Slave的CentOS系统。  
不能归零的原因可能是重试队列中往往会有极少量的（1条或几条）消息在不断尝试重新投递，但还有没有其他原因还需要更深入地了解RocketMQ。  
  
#Cluster Name     #Broker Name            #BID  #Addr                  #Version                #InTPS(LOAD)       #OutTPS(LOAD) #PCWait(ms) #Hour #SPACE  
YWBETALogCluster  broker-YWBETA-Log-00    0     10.42.129.196:10911    V4_7_1_MQS_R4           52.80(0,0ms)        52.80(0,0ms)          0 40.69 0.1247  
YWBETALogCluster  broker-YWBETA-Log-01    0     10.42.128.205:10911    V4_7_1_MQS_R4           53.70(0,0ms)        53.70(0,0ms)          0 40.91 0.1387  
YWBETACluster     broker-YWBETA-00        0     10.42.129.102:10911    V4_7_1_MQS_R4            0.00(0,0ms)         2.30(0,0ms)          0 168.12 0.8244  
YWBETACluster     broker-YWBETA-00        1     10.42.129.164:10911    V4_7_1_MQS_R4            0.00(0,0ms)         0.00(0,0ms)          0 84.52 0.8308  
YWBETACluster     broker-YWBETA-01        0     10.42.129.195:10911    V4_7_1_MQS_R4           29.31(0,0ms)        32.10(0,0ms)          0 169.76 0.8489  
YWBETACluster     broker-YWBETA-01        1     10.42.128.138:10911    V4_7_1_MQS_R4           29.23(0,0ms)         0.00(0,0ms)          0 169.76 0.8459  
  
chown -R umpadmin:umpgrp /data01/bro  
  
  
su: warning: cannot change directory to /data01/ump: Permission denied  
-bash: /data01/ump/.bash_profile: Permission denied  
  
观察了一天，master的OutTPS都没有归零，只升级了Slave的CentOS系统  
  
原因可能是重试队列中往往会有极少量的（1条或几条）消息在不断尝试重新投递，但还有没有其他原因还需要更深入地了解RocketMQ。  
  
2. 租户侧服务器只有系统盘，没有数据盘，需要把/data01目录里的数据压缩后复制到堡垒机上，系统升级后再复制回服务器解压。但是压缩包数据量太大导致解压压缩包时空间不够，我是边解压边删除部分大文件才解决了这个问题。  
RocketMQ哪些是核心数据，必须要备份，哪些不是，不用打包，需要深入地了解RocketMQ Broker组件的存储机制。  
  
3. 了解一下如何主备切换，让数据可以在Master和Slave之间互相copy，这样就不需要备份太多数据。
## 6.Enterprise Architect  
  
  
https://sparxsystems.cn/resources/demos/index.html  
  
  
https://sparxsystems.com