Thursday May 14 Day 134 week 20 of 2026

## 1.TodoList
5. 周日去图书馆借书  
6. 以后不要这样太盲目的借书，要有计划，有目标的借  
7. RocketMQ 5.5 发布  
8. AI要学习，RocketMQ也要深入学习  
9. 每天工作内容审视  
10. 制定到周日的工作计划  
11. 制定科目四学习计划  
12. 制动长期学习计划  
13. 总结周日要借的书  
14. 生产环境批量重发消息邮件模板



## 2.MCA课程学习进度

2026年05月14号学习进展：
1. 学习《UML面向对象分析与设计》  
   大概用时：4小时


## 3.

## 4.耿蕊 00603057  
  
新产业、新机会、新空间！销售收入450.18亿元，同比增长72.1%！欢迎来做战友！

## 6.UML 学习资源  
  
  
  
https://www.bilibili.com/video/BV1fq4y1q7KP/?spm_id_from=333.337.search-card.all.click&vd_source=dd94464bac13f791ea6a2e385d28295a  
UML面向对象分析与设计  
![2026-05-14_153623.png](resource20260514/2026-05-14_153623.png)  
  
  
https://www.bilibili.com/video/BV1oy4y1x7hF/?spm_id_from=333.337.search-card.all.click&vd_source=dd94464bac13f791ea6a2e385d28295a  
UML基础班课程分享【梁梠计划】  
  
![2026-05-14_153719.png](resource20260514/2026-05-14_153719.png)  
  
  
https://www.icourse163.org/course/ZZU-1207213802?from=searchPage&outVendor=zw_mooc_pcssjg_  
面向对象方法学  
  
  
UML 2面向对象分析与设计  
作 者 :  谭火彬编著  
ISBN :  978-7-302-50698-0  
出版信息 : 北京:清华大学出版社,2019  
页 数 :  13,353页  
价 格 : CNY59.50  
分类号 :  TP312  
关键词 : UML 　面向对象语言-程序设计-高等学校-教材  
丛书名 :  
  
深圳图书馆  
04400512792656  TP312/1501=2   深图中文图书借阅区3楼    在馆 0  中文图书外借 三楼1区10巷A面6架1层  
  
04400512792657  TP312/1501=2   深图北馆立体书库（预借图书） 在馆 0  中文图书外借 0  
需要预借登记，周六完成，周日去取书  
  
  
UML 2面向对象分析与设计  
作 者 :  谭火彬编著  
ISBN :  978-7-302-30788-4  
出版信息 : 北京:清华大学出版社,2013  
页 数 :  326页  
价 格 : CNY35.00  
分类号 :  TP312UM  
关键词 : UML语言-程序设计 　面向对象语言-程序设计  
  
F4401001023967  TP312UM/84 大学城中文图书    在馆 0  大学城中文图书    (二楼)中文图书094排B面02架06层  
  
## 7.科目四学习计划  
  
1. 科目四官方资料PPT等-->markdown  
2. 内网W3各种题目-->markdown  
3. 学会自己画UML图  
4. 设计模式要根据图自己实现代码

## 8.RocketMQ源码学习  
### 8.1 实际遇到的问题  
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
  
### 8.2 客户问的问题  
5月8号 杨福 60049205的问题总结，杨开虎 wx1383663解答的非常好。  
  
参考资料  
  
https://12345.huawei.com/unidesk/portal/#/case_details?caseId=KT00390547  
  
### 8.3 客户问的问题  
于生 00694738  
吴少明 30056023  
  
5月13号 Topic扩容，扩容会不会导致消费重复？ 如果消息都消费完了，会不会引起重复消费？？？？  
于生 00694738 2026-05-14 09:10  
当前16台机器（生产12台，灰度4台），高并发计算时，实际只用了8台机器  
  
  
【MQS优化】：  
问题：当前12台机器，高并发计算时，实际只用了6台机器，想优化下把其余机器也进行MQS消息消费，提升性能。  
对应告警：5月份年终奖计算任务全员计算，消费者重试量（30分钟内新增）超过3000，触发告警（连续10次真实值:(9433.22 Counts,8905.42 Counts,7365.76 Counts......)）  
参数优化：当前MQS参数？能否根据我们的业务场景，给出建议值？参数修改后是否需要重启机器生效？  
  
  
  
流量没有超过1000/s的都不建议做队列扩容，通常只有Topic流量超过5000/s ，性能瓶颈才会出现在队列上面；  
这个指标在哪里看你知道吗？  
  
### 8.4 RocketMQ 5.5 发布  
  
RocketMQ 5.5 源码学习  
  
  
## 9.AI学习计划  
  
MQS脚本交给AI优化一下。  
  
  
## 10.制定科目四学习计划  
  
  
  
https://www.bilibili.com/video/BV1fq4y1q7KP/?spm_id_from=333.337.search-card.all.click&vd_source=dd94464bac13f791ea6a2e385d28295a  
UML面向对象分析与设计  
![2026-05-14_153623.png](resource20260514/2026-05-14_153623.png)  
  
  
https://www.bilibili.com/video/BV1oy4y1x7hF/?spm_id_from=333.337.search-card.all.click&vd_source=dd94464bac13f791ea6a2e385d28295a  
UML基础班课程分享【梁梠计划】  
  
![2026-05-14_153719.png](resource20260514/2026-05-14_153719.png)  
  
  
https://www.icourse163.org/course/ZZU-1207213802?from=searchPage&outVendor=zw_mooc_pcssjg_  
面向对象方法学  
  
  
https://www.icourse163.org/course/PKU-1003177002  
软件工程  
  
  
孙艳春：女，博士，北京大学计算机学院副教授，博士生导师，于2005 年9 月到 2006 年 9 月去美国耶鲁大学计算机系做访问学者。全国高校计算机专业优秀教师、CCF杰出会员、IEEE SWEBOK(软件工程知识体系) Version 3软件设计领域编委, CCF 服务计算专委会执行委员，CCF软件工程专委会执行委员、CCF教育专委会执行委员。IEEE member、ACM member。  
  
孙艳春副教授主要研究方向包括软件工程、服务计算、大数据分析、智慧教育等，主持和参与国家自然科学基金项目、国家重点研发计划项目等10余项，现已在TOSEM、JSS、ICSE、FSE、ICWS等国内外知名学术期刊和会议发表论文90余篇，11项授权专利（第一发明人）、编著两部，译著三部（第一译者）。获得2015年教育部科技进步一等奖、2022年ICSS Best Paper Award、2023年IEEE-CCF服务计算最佳应用论文奖、2024年IEEE TCSVC服务计算杰出女性奖、2024中国电子学会技术发明奖一等奖。  
  
     孙艳春副教授在北京大学为研究生开设了软件项目管理和方案工程课，为本科生开设了软件工程、软件工程实习、面向对象技术引论等课程。北京大学软件工程课获得2010年国家级精品课，孙艳春副教授是主要建设者，孙艳春副教授主持的软件工程课获得2016年国家级精品资源共享课、2020年国家级一流本科课程。孙艳春副教授主持的软件工程实习课获得2013年教育部产学合作专业综合改革项目－IBM建设课程。孙艳春副教授获得2017北京市高等教育教学成果二等奖（个人排名第一）、获得2012、2017、2021北京大学教学成果一等奖，个人排名均第1。获得2019和2024北京大学教学优秀奖。牵头主编教育部“101计划”软件工程核心教材《软件工程—经典、现代和前沿》，主编十一五国家重点规划教材《软件工程》(第三版），在IEEE CSEET、ACM TURC等国际会议上发表多篇高水平教学论文。  
  
孙艳春副教授担任 IEEE SSE 2024 和 2025 程序委员会主席，IEEE ICWS、SEKE、APSEC、IEEE SCC、IEEE COMPSAC、ICSS 等国际知名软件工程会议的程序委员会委员，任《 Journal of Computer Science and Technology 》、《软件学报》、《计算机学报》、《电子学报》等多个期刊的论文评审人，以及国家自然科学基金评议专家。  
  
1. 科目四官方资料PPT等-->markdown  
2. 内网W3各种题目-->markdown  
3. 学会自己画UML图  
4. 设计模式要根据图自己实现代码