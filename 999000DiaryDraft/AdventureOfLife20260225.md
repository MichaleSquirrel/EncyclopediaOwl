Wednesday February 25 Day 056 week 9 of 2026

## 1.TodoList
1. 2月25日起，通过个人所得税App，可预约2025年度个人所得税综合所得汇算清缴办理。


##  2.


```shell
 jps -l
 jinfo -flags 19127
 java -version
 
jstat -gc 19127 1000 10
jstat -gc 7882 1000 10


jstat -class 19127 1000 10

jstat -class 7882 1000 10
jstat -class 7882 1000 10

jstack 19127
jstack 7882


jmap -heap 19127
jmap -heap 7882
```

```shell
[root@mqs-web01-fromxac ~]# jps -l
18836 /data01/ump/mqs-prod/mqs-auditor-message/mqs-auditor-message-3.2.1.2.jar
3158 sun.tools.jps.Jps
2394 mqsproxy.jar
10348 org.apache.catalina.startup.Bootstrap
25231 org.apache.catalina.startup.Bootstrap

jmap -heap 18836
jmap -heap 2394
jmap -heap 10348
jmap -heap 25231



jstat -gc 18836 10000 10
jstat -gc 2394 10000 10
jstat -gc 10348 10000 5
jstat -gc 25231 10000 5



jstat -class 18836 10000 4
jstat -class 2394 10000 4
jstat -class 10348 10000 4
jstat -class 25231 10000 4


jstack 18836
jstack 2394
jstack 10348
jstack 25231

jmap -dump:format=b,file=/usr/local/games/heap.hprof 25231
```

```shell
[root@mqs-web01-fromxac ~]# jmap -heap 10348
Attaching to process ID 10348, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 25.352-b08

using thread-local object allocation.
Parallel GC with 4 thread(s)

Heap Configuration:
   MinHeapFreeRatio         = 0
   MaxHeapFreeRatio         = 100
   MaxHeapSize              = 2051014656 (1956.0MB)
   NewSize                  = 42991616 (41.0MB)
   MaxNewSize               = 683671552 (652.0MB)
   OldSize                  = 87031808 (83.0MB)
   NewRatio                 = 2
   SurvivorRatio            = 8
   MetaspaceSize            = 21807104 (20.796875MB)
   CompressedClassSpaceSize = 1073741824 (1024.0MB)
   MaxMetaspaceSize         = 17592186044415 MB
   G1HeapRegionSize         = 0 (0.0MB)

Heap Usage:
PS Young Generation
Eden Space:
   capacity = 40370176 (38.5MB)
   used     = 34545712 (32.94535827636719MB)
   free     = 5824464 (5.5546417236328125MB)
   85.57235915939529% used
From Space:
   capacity = 1572864 (1.5MB)
   used     = 1474720 (1.406402587890625MB)
   free     = 98144 (0.093597412109375MB)
   93.76017252604167% used
To Space:
   capacity = 1572864 (1.5MB)
   used     = 0 (0.0MB)
   free     = 1572864 (1.5MB)
   0.0% used
PS Old Generation
   capacity = 887619584 (846.5MB)
   used     = 793198648 (756.4531784057617MB)
   free     = 94420936 (90.04682159423828MB)
   89.36245462560682% used

69926 interned Strings occupying 7111088 bytes.
```

```shell
[root@mqs-brokerm00-fromxac ~]# jps -l
21046 org.apache.rocketmq.broker.BrokerStartupExt
15901 sun.tools.jps.Jps


jmap -heap 21046
jstat -gc 21046 10000 2

jstat -class 21046 10000 2



jstack 21046

jmap -dump:format=b,file=/usr/local/games/heap.hprof 21046
```


```shell
[root@mqs-namesrv00-fromxac ~]# jps -l
14166 sun.tools.jps.Jps
24042 org.apache.rocketmq.namesrv.NamesrvStartupExt

jmap -heap 24042
jstat -gc 24042 10000 2

jstat -class 24042 10000 2



jstack 24042


jmap -dump:format=b,file=/usr/local/games/heap.hprof 24042

jmap -histo:live 24042
```
```shell
[root@mqs-umpnamesrv00-fromxac ~]# jps -l
7044 sun.tools.jps.Jps
1796 /data01/ump/mqs-prod/umpnamesrv/umpnamesrv
746 /data01/ump/mqs-prod/umpconnector/umpconnector

jmap -heap 1796
jmap -heap 746
jstat -gc 1796 10000 2
jstat -gc 746 10000 2

jstat -class 1796 10000 2
jstat -class 746 10000 2



jstack 1796
jstack 746


jmap -dump:format=b,file=/usr/local/games/heap.hprof 1796
jmap -dump:format=b,file=/usr/local/games/heap.hprof 746

jmap -histo:live 1796
jmap -histo:live 746
```


## 3.   25.3版本软件包链接


25.3版本软件包链接：https://cmc-szv.clouddragon.huawei.com/cmcversion/index/releaseView?deltaId=13543384055612672&isSelect=Software

## 4. 可信考试准备
![2026-02-25_121230.png](pic20260225/2026-02-25_121230.png)


## 5. 智能汽车解决方案数字化及IT装备部   数字化及IT装备部学分制课程2.0
Hi all，应公司要求，为拓展视野和提升能力，员工需完成以下课程学习，请各位予以重视。

学习链接：https://ilearning.huawei.com/edx/next/program/833483053275680768

层级	必修/选修	通过标准	精品课程名称	学分
IAS BU	必修	通过考试	人人懂汽车	2
人人懂汽车质量2.0考试	2
整车开发流程考试	2
IPD-IAS流程应知应会考试	1.5
FMEA基础课程考试	2
智能驾驶系统概览考试	1.5
智能座舱产品知识学习	1.5
智能车控通用业务知识	2
整车性能开发知识	1.5
功能安全基础	2
智能车载光领域知识	2
底盘域控解决方案	2
大语言模型简介	2
数字化及IT装备部	必修	通过考试	管理业务IT流程3.0介绍	2


## 6.mqs-web00-fromxac

mqs-install-portal

> https://console.ywit-op-beta.yinwang.com/liveops/appdeploy/#/application/stack/4b67e2b5fe644caa922384b89887dad8/logs

![2026-02-13_180949.png](pic20260213/2026-02-13_180949.png)

![2026-02-13_181308.png](pic20260213/2026-02-13_181308.png)


系统升级思路，先备份所有服务的相关数据

java
mqsproxy


/data01/ump/mqs-prod/tomcat-mqs-web


-rwx------  1 root root 219 Apr  1  2020 logrotate
-rwxr-xr-x. 1 root root 618 Oct 30  2018 man-db.cron


### 6.1 MobaXterm 字体搞大一点

MobaXterm Font


### 6.2


> Linux系统——计划任务
> https://blog.csdn.net/m0_64891352/article/details/132679722

## 7.代码提交
