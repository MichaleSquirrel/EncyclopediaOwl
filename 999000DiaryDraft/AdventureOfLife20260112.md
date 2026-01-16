Monday January 12 Day 012 week 3 of 2026

## 1.TodoList
1. 买羽绒服，准备1月24号的见面
2. 买米醋和面粉准备洗头的物品，
3. 买红包准备见面礼
4. 准备1月14号的考试
5. 学习RocketMQ
6. 测试FTS
7. 1月24号和27号请假
8. MQS系统升级
9. 算法讲解材料
10. 植物染发
11.


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

::SuperAdmin  Dinosaur
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 3" https://console.ywit.yinwang.com/home/#/index
::projectAdmin Elephant
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 4" https://console.ywit-op-beta.yinwang.com/
::common user Pandan
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 8" https://console.ywit-beta.yinwang.com/home/#/index

::common user Fox
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 5" https://console.ywit-beta.yinwang.com/home/#/index

::common user Rabbit
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 6" https://console.ywit-beta.yinwang.com/home/#/index

::common user Penguin
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 7" https://console.ywit-beta.yinwang.com/home/#/index


::secureAccess  
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 1" https://console.ywit-op-beta.yinwang.com/osaConsole/#/secureAccess?servicealias=osa&app_id=b995709d9d0343b2830ba09dbc317f32&isuser=true


::secureAccess  
start C:\"Program Files"\Google\Chrome\Application\chrome.exe --profile-directory="Profile 9" https://console.ywit-beta.yinwang.com/osaConsole/#/secureAccess?servicealias=osa&app_id=b995709d9d0343b2830ba09dbc317f32&isuser=true

```

## 6.RocketMQ学习
楼兰说技术
发消息
分享知识经验，笑评职场人生。
https://www.bilibili.com/video/BV1EUP2ehEB4


RocketMQ快速实战以及核心概念详解

图灵：楼兰

笔记配合视频课程一起学习

这一章节的目的是最快速度上手RocketMQ产品。

一、MQ简介

MQ：MessageQueue，消息队列。是在互联网中使用非常广泛的一系列服务中间件。这个词可以分两个部分来看，一是Message：消息。消息是在不同进程之间传递的数据。这些进程可以部署在同一台机器上，也可以分布在不同机器上。二是Queue：队列。队列原意是指一种具有FIFO(先进先出)特性的数据结构，是用来缓存数据的。对于消息中间件产品来说，能不能保证FIFO特性，尚值得考量。但是，所有消息队列都是需要具备存储消息，让消息排队的能力。

广义上来说，只要能够实现消息跨进程传输以及队列数据缓存，就可以称之为消息队列。例如我们常用的QQ、微信、阿里旺旺等就都具备了这样的功能。只不过他们对接的使用对象是人，而我们这里讨论的MQ产品需要对接的使用对象是应用程序。

MQ的作用主要有以下三个方面：

异步
例子：快递员发快递，直接到客户家效率会很低。引入菜鸟驿站后，快递员只需要把快递放到菜鸟驿站，就可以继续发其他快递去了。客户再按自己的时间安排去菜鸟驿站取快递。
作用：异步能提高系统的响应速度、吞吐量。

https://blog.csdn.net/roykingw/article/details/110734584

https://www.cnblogs.com/randolf/p/19093528

https://www.ruike1.com/thread-87242-1-1.html




https://blog.csdn.net/roykingw/article/details/143216872
![2026-01-12_151700.png](pic20260112/2026-01-12_151700.png)

### 6.1 RocketMQ Download


https://rocketmq.apache.org/zh/download/

### 6.2 RocketMQ Deploy

![2026-01-12_152542.png](pic20260112/2026-01-12_152542.png)

IP:10.40.161.21
主机名称:kweshdsita01095

初始密码:eR6ysH04^YbH


Huawei Cloud EulerOS 2.0  安装 Java

> APIG常用组件部署
> https://wiki.rnd.yinwang.com/domains/300337/wiki/1000372/WIKI2026010116898707


#### 6.2.1 挂盘
通用操作
挂盘

```shell
# 如果新机器默认存在data01目录，那么需要查看是否已经挂盘到data01目录
fdisk -l
mkfs.xfs -f /dev/vdb
echo '/dev/vdb /data01 xfs defaults 1 2' >> /etc/fstab
mkdir –p  /data01
mount -a
df -h
```

```shell
[root@kweshdsita01095 ~]# mkfs.xfs -f /dev/vdb
meta-data=/dev/vdb               isize=512    agcount=4, agsize=1310720 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=0    bigtime=1 inobtcount=0
data     =                       bsize=4096   blocks=5242880, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
[root@kweshdsita01095 ~]# echo '/dev/vdb /data01 xfs defaults 1 2' >> /etc/fstab
[root@kweshdsita01095 ~]# mkdir –p /data01
[root@kweshdsita01095 ~]# mount -a
[root@kweshdsita01095 ~]# df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        4.0M     0  4.0M   0% /dev
tmpfs           3.7G     0  3.7G   0% /dev/shm
tmpfs           3.7G  8.6M  3.7G   1% /run
tmpfs           4.0M     0  4.0M   0% /sys/fs/cgroup
/dev/vda1        40G  3.1G   35G   9% /
tmpfs           3.7G   36K  3.7G   1% /tmp
/dev/vdb         20G   53M   20G   1% /data01
[root@kweshdsita01095 ~]# df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
devtmpfs       devtmpfs      4096       0      4096   0% /dev
tmpfs          tmpfs      3864628       0   3864628   0% /dev/shm
tmpfs          tmpfs      3864628    8752   3855876   1% /run
tmpfs          tmpfs         4096       0      4096   0% /sys/fs/cgroup
/dev/vda1      ext4      41169244 3207172  36163232   9% /
tmpfs          tmpfs      3864632      36   3864596   1% /tmp
/dev/vdb       xfs       20961280   54004  20907276   1% /data01
[root@kweshdsita01095 ~]# 

```
![2026-01-12_154203.png](pic20260112/2026-01-12_154203.png)

#### 6.2.2 安装jdk
安装jdk

> 安装华为 JDK
> https://3ms.huawei.com/km/blogs/details/21489324


安装sz
```shell
wget http://mirrors.myhuaweicloud.com/repo/mirrors_source.sh && bash mirrors_source.sh
yum install lrzsz
```

```shell
[root@kweshdsita01095 data01]# vim /etc/profile
[root@kweshdsita01095 data01]# source /etc/profile
[root@kweshdsita01095 data01]# java -version
openjdk version "1.8.0_332"
OpenJDK Runtime Environment Huawei Technologies Co., Ltd (build 1.8.0_332-Huawei_JDK_V100R001C00SPC330B002-b09)
OpenJDK 64-Bit Server VM Huawei Technologies Co., Ltd (build 25.332-b09, mixed mode)
```

将包 jdk-8u332-linux-x64.tar.gz 或 jdk-8u332-linux-aarch64.tar.gz，解压到 /usr/local/ 目录下

```shell
tar -zxvf jdk-8u332-linux-x64.tar.gz -C /usr/local/
```

2. 配置系统环境变量
   修改命令：vim /etc/profile

增加内容:

```shell
export JAVA_HOME=/usr/local/jdk1.8.0_332
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
```
3. 保存后，执行source命令使配置生效

```shell
source /etc/profile
```
4. 验证是否安装成功
   使用以下命令，输出版本号则安装成功
```shell
java -version
```

mkdir -p /data01/rocketmq

![2026-01-12_160233.png](pic20260112/2026-01-12_160233.png)

```shell
[root@kweshdsita01095 rocketmq]# pwd
/data01/rocketmq
[root@kweshdsita01095 rocketmq]# cd rocketmq-all-5.4.0-bin-release
[root@kweshdsita01095 rocketmq-all-5.4.0-bin-release]# ll
total 56
drwxr-xr-x 2 root root   126 Dec 24 16:00 benchmark
drwxrwxr-x 4 root root  4096 Dec 24 15:24 bin
drwxr-xr-x 8 root root  4096 Dec 24 16:00 conf
drwxr-xr-x 2 root root  8192 Dec 24 16:00 lib
-rw-rw-r-- 1 root root 17327 Dec 24 15:24 LICENSE
-rw-rw-r-- 1 root root  1338 Dec 24 15:24 NOTICE
-rw-rw-r-- 1 root root 12270 Dec 24 15:24 README.md
[root@kweshdsita01095 rocketmq-all-5.4.0-bin-release]# ls lib
animal-sniffer-annotations-1.21.jar    j2objc-annotations-2.8.jar                                      netty-resolver-dns-native-macos-4.1.119.Final-osx-x86_64.jar     opentracing-tracerresolver-0.1.8.jar
annotations-13.0.jar                   jackson-core-2.18.1.jar                                         netty-tcnative-boringssl-static-2.0.53.Final.jar                 opentracing-util-0.33.0.jar
annotations-4.1.1.4.jar                jaeger-thrift-1.8.1.jar                                         netty-tcnative-boringssl-static-2.0.53.Final-linux-aarch_64.jar  perfmark-api-0.25.0.jar
annotations-api-6.0.53.jar             jaeger-tracerresolver-1.8.1.jar                                 netty-tcnative-boringssl-static-2.0.53.Final-linux-x86_64.jar    prometheus-metrics-config-1.3.3.jar
awaitility-4.1.0.jar                   javassist-3.20.0-GA.jar                                         netty-tcnative-boringssl-static-2.0.53.Final-osx-aarch_64.jar    prometheus-metrics-exporter-common-1.3.3.jar
bcpkix-jdk15on-1.69.jar                javax.annotation-api-1.3.2.jar                                  netty-tcnative-boringssl-static-2.0.53.Final-osx-x86_64.jar      prometheus-metrics-exporter-httpserver-1.3.3.jar
bcprov-jdk15on-1.69.jar                jctools-core-2.1.1.jar                                          netty-tcnative-boringssl-static-2.0.53.Final-windows-x86_64.jar  prometheus-metrics-exposition-formats-1.3.3.jar
bcutil-jdk15on-1.69.jar                jna-4.2.2.jar                                                   netty-tcnative-classes-2.0.53.Final.jar                          prometheus-metrics-model-1.3.3.jar
bolt-1.6.4.jar                         jraft-core-1.3.14.jar                                           netty-transport-4.1.119.Final.jar                                protobuf-java-3.20.1.jar
caffeine-2.9.3.jar                     jsr305-3.0.2.jar                                                netty-transport-classes-epoll-4.1.119.Final.jar                  protobuf-java-util-3.20.1.jar
checker-qual-3.33.0.jar                jul-to-slf4j-2.0.6.jar                                          netty-transport-classes-kqueue-4.1.119.Final.jar                 proto-google-common-protos-2.9.0.jar
commons-beanutils-1.9.4.jar            kotlin-stdlib-1.8.21.jar                                        netty-transport-native-epoll-4.1.119.Final-linux-aarch_64.jar    reflections-0.9.11.jar
commons-cli-1.5.0.jar                  kotlin-stdlib-common-1.8.21.jar                                 netty-transport-native-epoll-4.1.119.Final-linux-riscv64.jar     rocketmq-auth-5.4.0.jar
commons-codec-1.13.jar                 kotlin-stdlib-jdk7-1.8.21.jar                                   netty-transport-native-epoll-4.1.119.Final-linux-x86_64.jar      rocketmq-broker-5.4.0.jar
commons-collections-3.2.2.jar          kotlin-stdlib-jdk8-1.8.21.jar                                   netty-transport-native-kqueue-4.1.119.Final-osx-aarch_64.jar     rocketmq-client-5.4.0.jar
commons-digester-2.1.jar               libthrift-0.15.0.jar                                            netty-transport-native-kqueue-4.1.119.Final-osx-x86_64.jar       rocketmq-common-5.4.0.jar
commons-io-2.14.0.jar                  listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar  netty-transport-native-unix-common-4.1.119.Final.jar             rocketmq-container-5.4.0.jar
commons-lang-2.6.jar                   lz4-java-1.8.0.jar                                              netty-transport-rxtx-4.1.119.Final.jar                           rocketmq-controller-5.4.0.jar
commons-lang3-3.12.0.jar               metrics-core-4.0.2.jar                                          netty-transport-sctp-4.1.119.Final.jar                           rocketmq-example-5.4.0.jar
commons-logging-1.2.jar                netty-all-4.1.119.Final.jar                                     netty-transport-udt-4.1.119.Final.jar                            rocketmq-filter-5.4.0.jar
commons-validator-1.7.jar              netty-buffer-4.1.119.Final.jar                                  okhttp-4.12.0.jar                                                rocketmq-grpc-netty-codec-haproxy-1.0.0.jar
concurrentlinkedhashmap-lru-1.4.2.jar  netty-codec-4.1.119.Final.jar                                   okio-3.6.0.jar                                                   rocketmq-logback-classic-1.0.1.jar
disruptor-1.2.10.jar                   netty-codec-dns-4.1.119.Final.jar                               okio-jvm-3.4.0.jar                                               rocketmq-namesrv-5.4.0.jar
disruptor-3.3.7.jar                    netty-codec-haproxy-4.1.119.Final.jar                           openmessaging-api-0.3.1-alpha.jar                                rocketmq-openmessaging-5.4.0.jar
dledger-0.3.2.jar                      netty-codec-http2-4.1.119.Final.jar                             opentelemetry-api-1.44.1.jar                                     rocketmq-proto-2.1.1.jar
error_prone_annotations-2.14.0.jar     netty-codec-http-4.1.119.Final.jar                              opentelemetry-api-incubator-1.44.1-alpha.jar                     rocketmq-proxy-5.4.0.jar
failureaccess-1.0.1.jar                netty-codec-memcache-4.1.119.Final.jar                          opentelemetry-context-1.44.1.jar                                 rocketmq-remoting-5.4.0.jar
fastjson-1.2.83.jar                    netty-codec-mqtt-4.1.119.Final.jar                              opentelemetry-exporter-common-1.44.1.jar                         rocketmq-rocksdb-1.0.2.jar
fastjson2-2.0.43.jar                   netty-codec-redis-4.1.119.Final.jar                             opentelemetry-exporter-logging-1.44.1.jar                        rocketmq-shaded-slf4j-api-bridge-1.0.0.jar
grpc-api-1.53.0.jar                    netty-codec-smtp-4.1.119.Final.jar                              opentelemetry-exporter-logging-otlp-1.44.1.jar                   rocketmq-slf4j-api-1.0.1.jar
grpc-context-1.53.0.jar                netty-codec-socks-4.1.119.Final.jar                             opentelemetry-exporter-otlp-1.44.1.jar                           rocketmq-srvutil-5.4.0.jar
grpc-core-1.53.0.jar                   netty-codec-stomp-4.1.119.Final.jar                             opentelemetry-exporter-otlp-common-1.44.1.jar                    rocketmq-store-5.4.0.jar
grpc-netty-shaded-1.53.0.jar           netty-codec-xml-4.1.119.Final.jar                               opentelemetry-exporter-prometheus-1.44.1-alpha.jar               rocketmq-tiered-store-5.4.0.jar
grpc-protobuf-1.53.0.jar               netty-common-4.1.119.Final.jar                                  opentelemetry-exporter-sender-okhttp-1.44.1.jar                  rocketmq-tools-5.4.0.jar
grpc-protobuf-lite-1.53.0.jar          netty-handler-4.1.119.Final.jar                                 opentelemetry-sdk-1.44.1.jar                                     slf4j-api-2.0.3.jar
grpc-services-1.53.0.jar               netty-handler-proxy-4.1.119.Final.jar                           opentelemetry-sdk-common-1.44.1.jar                              snakeyaml-2.0.jar
grpc-stub-1.53.0.jar                   netty-handler-ssl-ocsp-4.1.119.Final.jar                        opentelemetry-sdk-extension-autoconfigure-spi-1.44.1.jar         sofa-common-tools-1.0.12.jar
gson-2.9.0.jar                         netty-resolver-4.1.119.Final.jar                                opentelemetry-sdk-logs-1.44.1.jar                                zstd-jni-1.5.2-2.jar
guava-32.0.1-jre.jar                   netty-resolver-dns-4.1.119.Final.jar                            opentelemetry-sdk-metrics-1.44.1.jar
hamcrest-2.1.jar                       netty-resolver-dns-classes-macos-4.1.119.Final.jar              opentelemetry-sdk-trace-1.44.1.jar
hessian-3.3.6.jar                      netty-resolver-dns-native-macos-4.1.119.Final-osx-aarch_64.jar  opentracing-noop-0.33.0.jar
[root@kweshdsita01095 rocketmq-all-5.4.0-bin-release]# 

```

```shell
[root@kweshdsita01095 rocketmq-all-5.4.0-bin-release]# vim bin/runserver.sh
[root@kweshdsita01095 rocketmq-all-5.4.0-bin-release]# vim bin/runbroker.sh
[root@kweshdsita01095 rocketmq-all-5.4.0-bin-release]# nohup bin/runserver.sh &

```


cd /app/rocketmq/rocketmq/example/bin/tools.sh org.apache.rocketmq.example.quickstart.Producer


bin/tools.sh org.apache.rocketmq.example.quickstart.Producer

bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer\



org.codehaus.mojo:mojo-parent.92


## 7.

https://github.com/killme2008/Metamorphosis


ROCKETMQ_HOME=D:\Download\RocketMQ

-C D:\Download\RocketMQ\conf\broker.conf


#nameServer
namesrvAddr=127.0.0.1:9876
autoCreateTopicEnable = true

storePathRootDir = D:\\Download\\RocketMQ\\store
#commitLog存储路径
storePathCommitLog = D:\\Download\\RocketMQ\\store\\commitlog
#消费队列存储路径
storePathConsumeQueue = D:\\Download\\RocketMQ\\store\\consumequeue
#消息索引存储路径
storePathIndex = D:\\Download\\RocketMQ\\store\\index
#checkpoint文件存储路径
storeCheckpoint = D:\\Download\\RocketMQ\\store\\checkpoint
#abort文件存储路径
abortFile = D:\\Download\\RocketMQ\\store\\abort