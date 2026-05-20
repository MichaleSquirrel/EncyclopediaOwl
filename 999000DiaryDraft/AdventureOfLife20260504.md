Monday May 4 Day 124 week 19 of 2026

## 1.TodoList
1. broker流量摘除时，Topic发消息正常  
2. 租户侧BrokerCentOS升级  
3. 编写变更实施方案  
4. 优化脚本  
5. Broker如何主从切换



## 2.MCA课程学习进度

2026年05月4号学习进展：
1. 使用优化后的升级脚本，给RocketMQ broker服务器升级  
   大概用时：8小时


## 3.万玉瑾 30080522  
  
新人介绍  
姓名&工号：万玉瑾 30080522  
生日：3月18日  
故乡：河南省信阳市固始县  
毕业学校：南京农业大学  
兴趣爱好：旅游，徒步  
工作地：深圳  
想对大家说的话：在南京学习工作9年，上海工作4年，有什么感兴趣的可以问我。主要负责前端方向，希望和大家合作愉快。新人入职，在工作生活上有什么不足请大家及时指正。

## 7.总结  
  
### 7.1 需要解决的问题  
  
consumequeue和commitlog文件关系，如果硬盘空间不够，保留哪个broker功能可以正常运行？  
  
### 7.2 broker升级的先研究到这里  
  
遇到的问题:  
把2组2从中的一组通过 mqadmin updateBrokerConfig 改为只读，但是master的OutTPS，总是不能归零，有什么办法解决吗？原计划是等全部归零后把服务器关机，把CentOS升级成别的系统。  
  
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
  
2.租户侧服务器只有系统盘，没有数据盘，需要把/data01目录里的数据压缩后复制到堡垒机上，系统升级后再复制回服务器解压。但是压缩包数据量太大导致解压压缩包时空间不够，我是边解压边删除部分大文件才解决了这个问题。  
RocketMQ哪些是核心数据，必须要备份，哪些不是，不用打包，需要深入地了解RocketMQ Broker组件的存储机制。