Tuesday February 24 Day 055 week 9 of 2026

## 1.TodoList
1. 牛奶洗澡有用吗
2. 2月25日起，通过个人所得税App，可预约2025年度个人所得税综合所得汇算清缴办理。
3. Xshell 控制台 输出到文件
4. IntelliJ IDEA  markdown 网络图片 无法加载
5. Xshell 控制台 输出到文件


## 2.2026年2月24号学习进展
2026年2月24号学习进展：
1. 练习JVM常用工具命令
2. 学习MAT从入门到精通
   大概用时：4小时

## 3.20260224WindowsStartScriptV3

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
:: start PixPin
start C:\"Program Files"\PixPin\PixPin.exe

:: start GitHubDesktop
start C:\Users\m30026548\AppData\Local\GitHubDesktop\GitHubDesktop.exe

:: normal work
start C:\"Program Files (x86)"\YINWANGWeLink\YINWANGWeLink.exe

::normal work
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Default" https://w3.huawei.com/next/indexa.html

:: yinwang op  Dinosaur
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 3" https://console.ywit-op.yinwang.com/
:: yinwang tenant Elephant
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 4" https://console.ywit.yinwang.com/home/#/index

::yinwang test op Pandan
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 8" https://console.ywit-op-beta.yinwang.com/
::yinwang test tenant Fox
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 5" https://console.ywit-beta.yinwang.com/home/#/index

::common user Rabbit
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 6" https://console.ywit-beta.yinwang.com/home/#/index
::common user Penguin
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 7" https://console.ywit-beta.yinwang.com/home/#/index

:: start VMware Workstation Pro
start C:\"Program Files (x86)"\VMware\"VMware Workstation"\vmware.exe

:: start MobaXterm
start D:\ProgrammFiles\"MobaXterm_Portable_v26.0"\MobaXterm_Personal_26.0.exe


## 4.练习JVM常用工具命令

[root@mqs-web00-fromxac ~]# jmap -dump:format=b,file=heap.hprof 19127
Dumping heap to /root/heap.hprof ...
Permission denied
-rwxr-xr-x 1 umpadmin umpgrp  17296 Nov  4  2022 jmap

## 4.测试环境升级一台mqs-portal

mqs-install-portal

> https://console.ywit-op-beta.yinwang.com/liveops/appdeploy/#/application/stack/4b67e2b5fe644caa922384b89887dad8/logs

![2026-02-13_180949.png](pic20260213/2026-02-13_180949.png)

![2026-02-13_181308.png](pic20260213/2026-02-13_181308.png)

## 5.练习JVM常用工具

```shell
[root@mqs-web00-fromxac ~]# jps
19429 Jps
19127 Bootstrap
7882 jar
[root@mqs-web00-fromxac ~]# jps -l
19127 org.apache.catalina.startup.Bootstrap
19496 sun.tools.jps.Jps
7882 mqsproxy.jar
[root@mqs-web00-fromxac ~]# jinfo -flag MaxHeapSize 19127
-XX:MaxHeapSize=2051014656

jinfo -flag MaxHeapSize 19127
jinfo -flag MaxHeapSizeXXX 19127
jinfo -flags 19127
jinfo -flags 7882


[root@mqs-web00-fromxac ~]# jinfo -flags 19127
Attaching to process ID 19127, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 25.352-b08
Non-default VM flags: -XX:CICompilerCount=3 -XX:InitialHeapSize=130023424 -XX:MaxHeapSize=2051014656 -XX:MaxNewSize=683671552 -XX:MinHeapDeltaBytes=524288 -XX:NewSize=42991616 -XX:OldSize=87031808 -XX:+UseCompressedClassPointers -XX:+UseCompressedOops -XX:+UseFastUnorderedTimeStamps -XX:+UseParallelGC 
Command line:  -Djava.util.logging.config.file=/data01/ump/mqs-prod/tomcat-mqs-web/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 -Dignore.endorsed.dirs= -Dcatalina.base=/data01/ump/mqs-prod/tomcat-mqs-web -Dcatalina.home=/data01/ump/mqs-prod/tomcat-mqs-web -Djava.io.tmpdir=/data01/ump/mqs-prod/tomcat-mqs-web/temp
[root@mqs-web00-fromxac ~]# jinfo -flags 7882
Attaching to process ID 7882, please wait...
Debugger attached successfully.
Server compiler detected.
JVM version is 25.352-b08
Non-default VM flags: -XX:CICompilerCount=3 -XX:InitialHeapSize=130023424 -XX:MaxHeapSize=2051014656 -XX:MaxNewSize=683671552 -XX:MinHeapDeltaBytes=524288 -XX:NewSize=42991616 -XX:OldSize=87031808 -XX:+UseCompressedClassPointers -XX:+UseCompressedOops -XX:+UseFastUnorderedTimeStamps -XX:+UseParallelGC 
Command line:  

[root@mqs-web00-fromxac ~]# java -version
openjdk version "1.8.0_352"
OpenJDK Runtime Environment Huawei Technologies Co., Ltd (build 1.8.0_352-Huawei_JDK_V100R001C00SPC351B001-b08)
OpenJDK 64-Bit Server VM Huawei Technologies Co., Ltd (build 25.352-b08, mixed mode)

```

### 5.1 参数解析

```shell
Non-default VM flags: -XX:CICompilerCount=3 -XX:InitialHeapSize=130023424 -XX:MaxHeapSize=2051014656 -XX:MaxNewSize=683671552 -XX:MinHeapDeltaBytes=524288 -XX:NewSize=42991616 -XX:OldSize=87031808 -XX:+UseCompressedClassPointers -XX:+UseCompressedOops -XX:+UseFastUnorderedTimeStamps -XX:+UseParallelGC
Command line:  -Djava.util.logging.config.file=/data01/ump/mqs-prod/tomcat-mqs-web/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Dorg.apache.catalina.security.SecurityListener.UMASK=0027 -Dignore.endorsed.dirs= -Dcatalina.base=/data01/ump/mqs-prod/tomcat-mqs-web -Dcatalina.home=/data01/ump/mqs-prod/tomcat-mqs-web -Djava.io.tmpdir=/data01/ump/mqs-prod/tomcat-mqs-web/temp

```

-XX:CICompilerCount=3  最大并行编译数
-XX:InitialHeapSize=130023424   初始化堆大小 130023424 = 124M
-XX:MaxHeapSize=2051014656 最大堆大小  2051014656 = 1956M
-XX:NewSize=42991616  设置年轻代的大小  42991616 = 41M
-XX:MaxNewSize=683671552  年轻代最大大小  683671552 = 652M
-XX:MinHeapDeltaBytes=524288 设置堆扩展时的最小增量为524288字节（即512KB）。
-XX:OldSize=87031808   设置老年代大小 87031808 = 83MB

-XX:+UseCompressedClassPointers  启用压缩类指针，减少JVM对内存的需求。
-XX:+UseCompressedOops  启用压缩普通对象指针（Ordinary Object Pointers），减少JVM对内存的需求。
-XX:+UseFastUnorderedTimeStamps  开启该参数后，JVM 会使用更快但无序的时间戳来记录事件。这在某些场景下能提高性能，不过时间戳可能会出现无序的情况。
-XX:+UseParallelGC  表明 JVM 使用并行垃圾回收器来处理新生代的垃圾回收工作。并行垃圾回收器会使用多个线程同时进行垃圾回收，能提高垃圾回收的效率，比较适合多 CPU 环境下的应用程序。

> JVM调优
> https://blog.csdn.net/weixin_44929475/article/details/144337552
> JVM GC相关参数
> https://zhuanlan.zhihu.com/p/1895563461003547358
```
-Xms1000M等价于-XX:InitialHeapSize=1000M
-Xmx1000M等价于-XX:MaxHeapSize=1000M
-Xss100等价于-XX:ThreadStackSize=100
```

```shell
-XX:InitialHeapSize=130023424 
-XX:MaxHeapSize=2051014656
-XX:MaxNewSize=683671552   
-XX:OldSize=87031808
```

-XX:MinHeapDeltaBytes=524288：

设置堆扩展时的最小增量为1048576字节（即1MB）。

130023424 = 124M
2051014656 = 1956M
683671552 = 652M

87031808 = 83MB

524288 = 512KB

| 参数                                                                                |                                                 含义                                                 |                                                                    说明                                                                    |
| :---------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: |
| -XX:CICompilerCount=3                                                               |                                            最大并行编译数                                            |                               如果设置大于1，虽然编译速度会提高，但是同样影响系统稳定性，会增加JVM崩溃的可能                               |
| -XX:InitialHeapSize=100M                                                            |                                             初始化堆大小                                             |                                                                简写-Xms100M                                                                |
| -XX:MaxHeapSize=100M                                                                |                                              最大堆大小                                              |                                                                简写-Xms100M                                                                |
| -XX:NewSize=20M                                                                     |                                           设置年轻代的大小                                           |                                                                                                                                            |
| -XX:MaxNewSize=50M                                                                  |                                            年轻代最大大小                                            |                                                                                                                                            |
| -XX:OldSize=50M                                                                     |                                            设置老年代大小                                            |                                                                                                                                            |
| -XX:MetaspaceSize=50M                                                               |                                            设置方法区大小                                            |                                                                                                                                            |
| -XX:MaxMetaspaceSize=50M                                                            |                                            方法区最大大小                                            |                                                                                                                                            |
| -XX:+UseParallelGC                                                                  |                                           使用UseParallelGC                                           |                                                             新生代，吞吐量优先                                                             |
| -XX:+UseParallelOldGC                                                               |                                         使用UseParallelOldGC                                         |                                                             老年代，吞吐量优先                                                             |
| -XX:+UseConcMarkSweepGC                                                             |                                                使用CMS                                                |                                                            老年代，停顿时间优先                                                            |
| -XX:+UseG1GC                                                                        |                                               使用G1GC                                               |                                                        新生代，老年代，停顿时间优先                                                        |
| -XX:NewRatio                                                                        |                                            新老生代的比值                                            |                                   比如-XX:Ratio=4，则表示新生代:老年代=1:4，也就是新生代占整个堆内存的1/5                                   |
| -XX:SurvivorRatio                                                                   |                                         两个S区和Eden区的比值                                         |                               比如-XX:SurvivorRatio=8，也就是(S0+S1):Eden=2:8，也就是一个S占整个新生代的1/10                               |
| -XX:+HeapDumpOnOutOfMemoryError                                                     |                                          启动堆内存溢出打印                                          |                                             当JVM堆内存发生溢出时，也就是OOM，自动生成dump文件                                             |
| -XX:HeapDumpPath=heap.hprof                                                         |                                        指定堆内存溢出打印目录                                        |                                                    表示在当前目录生成一个heap.hprof文件                                                    |
| -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps -Xloggc:g1-gc.log |                                             打印出GC日志                                             |                                                  可以使用不同的垃圾收集器，对比查看GC情况                                                  |
| -Xss128k                                                                            |                                        设置每个线程的堆栈大小                                        |                                                            经验值是3000-5000最佳                                                            |
| -XX:MaxTenuringThreshold=6                                                          |                                        提升年老代的最大临界值                                        |                                                                 默认值为 15                                                                 |
| -XX:InitiatingHeapOccupancyPercent                                                  |                                    启动并发GC周期时堆内存使用占比                                    |     G1之类的垃圾收集器用它来触发并发GC周期,基于整个堆的使用率,而不只是某一代内存的使用比. 值为 0 则表示”一直执行GC循环”. 默认值为 45.     |
| -XX:G1HeapWastePercent                                                              |                                        允许的浪费堆空间的占比                                        |                                       默认是10%，如果并发标记可回收的空间小于10%,则不会触发MixedGC。                                       |
| -XX:MaxGCPauseMillis=200ms                                                          |                                            G1最大停顿时间                                            | 暂停时间不能太小，太小的话就会导致出现G1跟不上垃圾产生的速度。最终退化成Full GC。所以对这个参数的调优是一个持续的过程，逐步调整到最佳状态。 |
| -XX:ConcGCThreads=n                                                                 |                                     并发垃圾收集器使用的线程数量                                     |                                                       默认值随JVM运行的平台不同而不同                                                       |
| -XX:G1MixedGCLiveThresholdPercent=65                                                |                            混合垃圾回收周期中要包括的旧区域设置占用率阈值                            |                                                              默认占用率为 65%                                                              |
| -XX:G1MixedGCCountTarget=8                                                          | 设置标记周期完成后，对存活数据上限为 G1MixedGCLIveThresholdPercent 的旧区域执行混合垃圾回收的目标次数 |                                         默认8次混合垃圾回收，混合回收的目标是要控制在此目标次数以内                                         |
| -XX:G1OldCSetRegionThresholdPercent=1                                               |                               描述Mixed GC时，Old Region被加入到CSet中                               |                                                默认情况下，G1只把10%的Old Region加入到CSet中                                                |
|                                                                                     |                                                                                                      |                                                                                                                                            |


jstat -gc 19127 1000 10
jstat -gc 7882 1000 10


jstat -class 19127 1000 10

jstat -class 7882 1000 10jstat -class 7882 1000 10

jstack 19127
jstack 7882

```
jmap -heap 19127
jmap -heap 7882
```
{}
qos_request_hour
6000


jmap -dump:format=b,file=/usr/local/games/heap.hprof 19127
jmap -dump:format=b,file=heap.hprof 7882

```shell
[root@mqs-web00-fromxac ~]# jmap -dump:format=b,file=heap.hprof 19127
Dumping heap to /root/heap.hprof ...
Permission denied
-rwxr-xr-x 1 umpadmin umpgrp  17296 Nov  4  2022 jmap
```
jmap -dump Permission denied
## 6.API接口有限流吗？


步骤日志查询
/build-project-artifacts-api/logs/recordId/log/task/steps/stepId/log


Java高精尖技术分享

MAT从入门到精通


## 7.

![2026-02-24_151918.png](pic20260224/2026-02-24_151918.png)


张光雄 60067463 2026-02-24 15:01
RDBConn_SDM_OpenGauss_01
张光雄 60067463 2026-02-24 15:02
PP-MP-集成华技代采供应能力数据   1489
https://console.ywit-beta.yinwang.com/roma3c/#/taskRelease

毛关松 30026548 2026-02-24 15:17
应该是数据源的问题
https://blog.csdn.net/SunWuKong_Hadoop/article/details/89353425


节点类型 | 节点 | 节点编号 | 时间 | 耗时 | 数据量 | 分片 | 状态 | 脚本 | 提示信息
--- | --- | --- | --- | --- | --- | --- | --- | --- | ---
SQLQUERY | cts_sdm_agent_capacity_ti集成数据 | 16_36 | 2026-02-24 07:30:20 | 0 | 0 |  | ERROR | 查看脚本 | 点击展开提示信息

Query spend 187 ms. com.huawei.roma3cv2.common.exception.Roma3cJobException: sqlQuery job error, retryCount: 0 errorMsg: [12.11.0.71:42466/10.41.4.174:8000] ERROR: memory is temporarily unavailable Detail: Failed on request of size 16 bytes under queryid 0 in list.cpp:166. at com.huawei.roma3cv2.core.job.impl.SqlQueryJob.execute(SqlQueryJob.java:180) at com.huawei.roma3cv2.core.worker.impl.LocalWorker.lambda$submitJob$0(LocalWorker.java:69) at java.util.concurrent.FutureTask.run(FutureTask.java:266) at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) at java.lang.Thread.run(Thread.java:750) Caused by: com.huawei.opengauss.jdbc.util.PSQLException: [12.11.0.71:42466/10.41.4.174:8000] ERROR: memory is temporarily unavailable Detail: Failed on request of size 16 bytes under queryid 0 in list.cpp:166. at com.huawei.opengauss.jdbc.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:2672) at com.huawei.opengauss.jdbc.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2943) at com.huawei.opengauss.jdbc.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:376) at com.huawei.idbc.jdbc.PoStatement.runOueryExecutor(PoStatement.java:617) at

2026-02-21 07:30:15
2026-02-20 08:50:15
2026-02-20 07:30:15

清空 cts_sdm_agent_capacity_ti[35]
cts_sdm_agent_capacity_ti[集成数据[36]]
清空储备值PO[26]
更新储备值[25]
更新PO-data_plan [29]

search keywords：memory is temporarily unavailable Detail: Failed on request of size 16 bytes under queryid 0 in list.cpp:166.


## 8.

漫漫回家路
saroo brierley

ganesh talai

He studied business and hospitality at the Australian International Hotel School in Canberra.[3] As an adult, he spent around three years conducting searches using the satellite images on Google Earth, painstakingly following railway lines radiating out from Howrah railway station.[6] He relied on his vague memories of the main features around Burhanpur railway station, although he knew little of the name of the station except that it began with the letter B.[4] Late one night in 2011, he came upon a small railway station that closely matched his childhood recollection of where he had become trapped in an empty carriage; the name of this station was Burhanpur, very close to a phonetic spelling of the name he remembered from his childhood ordeal. He followed the satellite images of the railway line north and found the town of Khandwa. He had no recollection of that name, but the town contained recognizable features, such as a fountain near the train tracks where he used to play. He was able to trace a path through the streets to what appeared to be the place where he and his family used to live.

## 9.


[root@mqs-web00-fromxac ~]# jstat -gc 19127 10000 10
S0C    S1C    S0U    S1U      EC       EU        OC         OU       MC     MU    CCSC   CCSU   YGC     YGCT    FGC    FGCT     GCT   
1024.0 1024.0  0.0   672.0  33792.0   8446.6   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   8589.2   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   8794.8   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   8794.8   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   8794.8   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   8794.8   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   9112.2   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   9256.4   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   9466.5   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921
1024.0 1024.0  0.0   672.0  33792.0   9466.5   183808.0   132543.5  131032.0 125512.3 13824.0 12684.0   5045   23.590   4      0.331   23.921

EC: 年轻代中Eden区的容量。

-XX:NewSize=42991616  设置年轻代的大小  42991616 = 41M
-XX:MaxNewSize=683671552  年轻代最大大小  683671552 = 652M
-XX:OldSize=87031808   设置老年代大小 87031808 = 83MB


JDK自带工具局限：jmap仅能导出快照、jhat功能简陋易崩溃、jvisualvm、JConsole分析慢且不精准
https://visualvm.github.io/download.html


![2026-02-24_214517.png](pic20260224/2026-02-24_214517.png)

Incompatible JVM Version 1.8.0_342 of the JVM is not suitable for this product. Version: 17 or greater is required.

确定

