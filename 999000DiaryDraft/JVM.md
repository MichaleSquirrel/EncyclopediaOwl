
1. 简介
   JVM调优，即Java虚拟机（Java Virtual Machine）调优，是指对Java虚拟机的运行参数进行调整，以优化Java应用程序的性能。JVM是Java程序运行的平台，负责装载字节码文件，解释或编译字节码文件，并执行。调优的目标通常包括减少延迟、提高吞吐量、减少内存占用等。

以下是一些常见的JVM调优策略：

堆内存配置：

-Xms：设置JVM启动时的初始堆大小。(-XX:InitialHeapSize=123731968=119M)

-Xmx：设置JVM可以使用的最大堆大小。(-XX:MaxHeapSize=1954545664=1869M)

-Xms256m：设置JVM启动时的初始堆大小为256MB。

-Xmx1024m：设置JVM可以使用的最大堆大小为1024MB。

垃圾回收器选择：

选择合适的垃圾回收器（如Serial GC、Parallel GC、CMS、G1 GC等）以适应不同的应用场景。

-XX:+UseG1GC：选择G1垃圾回收器。

垃圾回收参数调整：

调整垃圾回收的触发条件和频率，例如设置新生代和老年代的大小比例。

-XX:NewRatio=2：设置新生代和老年代的大小比例为1:2。

-XX:SurvivorRatio=8：设置Eden区与Survivor区的大小比例为8:1:1。

JVM参数优化：

调整JVM的其他参数，如栈大小（-Xss 默认为1M）、元空间大小（-XX:MetaspaceSize）、直接内存大小（-XX:MaxDirectMemorySize）等。

-Xss256k：设置每个线程的栈大小为256KB。

-XX:MetaspaceSize=128m：设置元空间的初始大小为128MB。

监控和分析工具使用：

使用JVM监控工具（如VisualVM、JConsole、MAT等）来监控JVM的运行状态，并分析内存泄漏、垃圾回收情况等。

使用VisualVM监控JVM：通过VisualVM的GUI界面实时监控JVM的CPU使用率、内存使用情况、垃圾回收情况等。

代码层面的优化：

// 优化前
for (int i = 0; i < 1000; i++) {
String s = new String("Hello World");
}

// 优化后
String s = "Hello World";
for (int i = 0; i < 1000; i++) {
// 使用s而不是每次都创建新对象
}
AI写代码
java
运行

优化代码逻辑，减少不必要的对象创建，优化数据结构和算法等。

线程和同步优化：

减少锁的竞争，使用无锁数据结构，优化线程池配置等。

使用ConcurrentHashMap代替Hashtable以减少锁的竞争。

启动参数优化：

调整JVM启动参数，如-XX开头的非标准参数，以优化特定场景下的性能。

-XX:+TieredCompilation：启用分层编译，提高编译效率。

类加载器优化：

优化类加载机制，减少类加载和卸载的时间。

通过自定义类加载器来控制类的加载和卸载，优化类加载性能。

JVM日志配置：

配置JVM日志，以便在出现问题时能够快速定位。

-XX:+PrintGCDetails：打印GC日志，方便分析垃圾回收情况。

2. 实例
   查看Java程序具体JVM参数

jps # 7 cloud-api-sample.jar # 716 Jps jinfo PID # jinfo 7
AI写代码
bash
执行jinfo pid

Java System Properties:
...

VM Flags:
-XX:CICompilerCount=2
-XX:ConcGCThreads=1
-XX:G1ConcRefinementThreads=2
-XX:G1HeapRegionSize=1048576
-XX:GCDrainStackTargetSize=64
-XX:InitialHeapSize=123731968
-XX:MarkStackSize=4194304
-XX:MaxHeapSize=1954545664
-XX:MaxNewSize=1172307968
-XX:MinHeapDeltaBytes=1048576
-XX:NonNMethodCodeHeapSize=5825164
-XX:NonProfiledCodeHeapSize=122916538
-XX:ProfiledCodeHeapSize=122916538
-XX:ReservedCodeCacheSize=251658240
-XX:+SegmentedCodeCache
-XX:+UseCompressedClassPointers
-XX:+UseCompressedOops
-XX:+UseG1GC

VM Arguments:
java_command: cloud-api-sample.jar --spring.config.location=/app/data/setting/application.yml
java_class_path (initial): cloud-api-sample.jar
Launcher Type: SUN_STANDARD
AI写代码
bash

关键属性解释：

-XX:CICompilerCount=2：

设置编译器线程池中的线程数为2。这些线程负责将热点代码编译成优化的机器码。

-XX:ConcGCThreads=1：

设置并发垃圾回收线程的数量为1。这些线程参与并发标记和并发清理阶段。

-XX:G1ConcRefinementThreads=2：

设置G1并发区域整理（refinement）的线程数为2。这些线程并发地执行G1收集器的区域整理工作。

-XX:G1HeapRegionSize=1048576：

设置G1收集器使用的区域（region）大小为1048576字节（即1MB）。这个参数决定了堆被划分为多少个区域。

-XX:GCDrainStackTargetSize=64：

设置GC时回收堆栈的目标大小为64KB。这是一个性能调优参数，用于减少GC时的开销。

-XX:InitialHeapSize=123731968：

设置JVM启动时的初始堆大小为123731968字节（即约117MB）。

-XX:MarkStackSize=4194304：

设置标记栈的大小为4194304字节（即约4MB）。标记栈用于存储GC过程中的标记信息。

-XX:MaxHeapSize=1954545664：

设置JVM可以使用的最大堆大小为1954545664字节（即约1.8GB）。

-XX:MaxNewSize=1172307968：

设置新生代最大堆大小为1172307968字节（即约1.1GB）。

-XX:MinHeapDeltaBytes=1048576：

设置堆扩展时的最小增量为1048576字节（即1MB）。

-XX:NonNMethodCodeHeapSize=5825164：

设置非NMethod代码堆的大小。

-XX:NonProfiledCodeHeapSize=122916538：

设置未被JVM性能分析器分析过的代码堆的大小。

-XX:ProfiledCodeHeapSize=122916538：

设置被JVM性能分析器分析过的代码堆的大小。

-XX:ReservedCodeCacheSize=251658240：

设置代码缓存区的大小，用于存储JIT编译后的代码。

-XX:+SegmentedCodeCache：

启用分段代码缓存，可以提高代码缓存的利用率。

-XX:+UseCompressedClassPointers：

启用压缩类指针，减少JVM对内存的需求。

-XX:+UseCompressedOops：

启用压缩普通对象指针（Ordinary Object Pointers），减少JVM对内存的需求。

-XX:+UseG1GC：

启用G1垃圾收集器。

2.1 指令
利用一些指令监控JVM当前具体详情，以便做出对应调优策略。

2.1.1 jstat
jstat 是JDK自带的一个轻量级监控工具，全称是 Java Virtual Machine Statistics Monitoring Tool，主要用于监控Java虚拟机的各种运行状态信息，包括类加载、内存、垃圾收集、即时编译等运行数据。

jstat [option] vmid [interval[s|ms] [count]]
AI写代码
bash
option：指定要显示的性能指标，如 -class、-compiler、-gc、-gccapacity、-gcutil 等。

vmid：虚拟机唯一ID（LVMID，Local Virtual Machine Identifier），如果查看本机就是Java进程的进程ID。

interval：显示信息的时间间隔，单位默认毫秒。也可以指定秒为单位，比如：1s。

count：显示数据的次数，默认值是无穷大，这将导致jstat命令一直显示统计信息，直到目标JVM终止或jstat命令终止。

option参数说明：

-class：监视类装载、卸载数量、总空间以及类装载所耗费的时间。

-compiler：显示JIT编译器统计信息。

-gc：监视Java堆垃圾收集的活动。

-gccapacity：显示各个垃圾收集代的容量。

-gcutil：显示垃圾收集代的利用率。

-gcnew：监视新生代垃圾收集活动。

-gcold：监视老年代垃圾收集活动。

-gcmetacapacity：显示元数据空间的统计信息。

jstat -gc 7 1s 4  #查看gc状态信息，每秒显示一次，总共四次

jstat -gcold 7 1s 4
MC       MU      CCSC     CCSU       OC          OU       YGC    FGC    FGCT    CGC    CGCT     GCT   
109856.0 104452.7  14280.0  12115.9    151552.0     64595.4     53     0    0.000    10    0.060    1.280
109856.0 104452.7  14280.0  12115.9    151552.0     64595.4     53     0    0.000    10    0.060    1.280
109856.0 104452.7  14280.0  12115.9    151552.0     64595.4     53     0    0.000    10    0.060    1.280
109856.0 104452.7  14280.0  12115.9    151552.0     64595.4     53     0    0.000    10    0.060    1.280
AI写代码
bash
显示状态字段释义：

S0C: 年轻代中第一个Survivor区（S0）的容量（Capacity）。

S1C: 年轻代中第二个Survivor区（S1）的容量。

S0U: 年轻代中第一个Survivor区（S0）当前使用量（Used）。

S1U: 年轻代中第二个Survivor区（S1）当前使用量。

EC: 年轻代中Eden区的容量。

EU: 年轻代中Eden区当前使用量。

OC: 老年代的容量。

OU: 老年代当前使用量。

MC: 元数据区（Metaspace，JDK 8及以上版本）的容量。

MU: 元数据区当前使用量。

CCSC: 压缩类空间的容量（JDK 8以下版本为PermGen）。

CCSU: 压缩类空间当前使用量。

YGC: 年轻代垃圾回收次数。

YGCT: 年轻代垃圾回收消耗的时间。

FGC: 老年代垃圾回收次数。

FGCT: 老年代垃圾回收消耗的时间。

CGC: 并发垃圾回收次数（适用于CMS等并发收集器）。

CGCT: 并发垃圾回收消耗的时间。

GCT: 整个Java虚拟机垃圾回收消耗的总时间。

常用指令：

监控垃圾回收（GC）活动：

jstat -gc <pid>：显示垃圾收集统计信息，包括年轻代和老年代的收集次数和时间。

jstat -gccapacity <pid>：显示各个代的容量和垃圾收集后的剩余空间。

jstat -gcutil <pid>：显示垃圾收集统计信息，包括各个代的利用率百分比。

监控类加载信息：

jstat -class <pid>：显示类加载、卸载和总类数量的信息。

监控编译信息：

jstat -compiler <pid>：显示JIT编译器的统计信息。

监控线程信息：

jstat -thread <pid>：显示Java线程和系统线程的统计信息。

监控同步和锁信息：

jstat -lock <pid>：显示锁信息，包括轻量级锁和重量级锁的争用情况。

jstat -printcompilation <pid>：显示即时编译器的统计信息。

监控内存使用情况：

jstat -gcnew <pid>：显示年轻代的垃圾收集统计信息。

jstat -gcold <pid>：显示老年代的垃圾收集统计信息。

jstat -gcmetacapacity <pid>：显示元数据区的统计信息。

实时监控：

jstat -gc <pid> 1000：每1000毫秒打印一次垃圾收集统计信息。

jstat -gcutil <pid> 1000 10：每1000毫秒打印一次垃圾收集统计信息，共打印10次。

查看编译代码大小：

jstat -printcompilation <pid>：显示JIT编译的方法统计信息。

监控代码缓存信息：

jstat -compiler <pid>：显示JIT编译器的统计信息。

2.1.2 jstack
jstack 是一个由 JDK 提供的命令行工具，用于打印出给定 Java 进程中所有线程的堆栈跟踪。常用来诊断死锁、线程长时间停顿或者分析线程行为等性能问题。

jstack <pid>  #打印线程堆栈信息

jstack 7 > threaddump.txt  # 重定向到文件


"pool-1-thread-9" #78 prio=5 os_prio=0 cpu=479.78ms elapsed=1586.56s tid=0x00007fdbd8034800 nid=0x57 waiting on condition  [0x00007fdb94a40000]
java.lang.Thread.State: WAITING (parking)
at jdk.internal.misc.Unsafe.park(java.base@11.0.14.1/Native Method)
- parking to wait for  <0x000000008d2f1988> (a java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject)
at java.util.concurrent.locks.LockSupport.park(java.base@11.0.14.1/LockSupport.java:194)
at java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(java.base@11.0.14.1/AbstractQueuedSynchronizer.java:2081)
at java.util.concurrent.LinkedBlockingQueue.take(java.base@11.0.14.1/LinkedBlockingQueue.java:433)
at java.util.concurrent.ThreadPoolExecutor.getTask(java.base@11.0.14.1/ThreadPoolExecutor.java:1054)
at java.util.concurrent.ThreadPoolExecutor.runWorker(java.base@11.0.14.1/ThreadPoolExecutor.java:1114)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(java.base@11.0.14.1/ThreadPoolExecutor.java:628)
at java.lang.Thread.run(java.base@11.0.14.1/Thread.java:829)

"pool-1-thread-10" #79 prio=5 os_prio=0 cpu=423.35ms elapsed=1585.21s tid=0x000055864597c800 nid=0x58 waiting on condition  [0x00007fdb9493f000]
java.lang.Thread.State: WAITING (parking)
at jdk.internal.misc.Unsafe.park(java.base@11.0.14.1/Native Method)
- parking to wait for  <0x000000008d2f1988> (a java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject)
at java.util.concurrent.locks.LockSupport.park(java.base@11.0.14.1/LockSupport.java:194)
at java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(java.base@11.0.14.1/AbstractQueuedSynchronizer.java:2081)
at java.util.concurrent.LinkedBlockingQueue.take(java.base@11.0.14.1/LinkedBlockingQueue.java:433)
at java.util.concurrent.ThreadPoolExecutor.getTask(java.base@11.0.14.1/ThreadPoolExecutor.java:1054)
at java.util.concurrent.ThreadPoolExecutor.runWorker(java.base@11.0.14.1/ThreadPoolExecutor.java:1114)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(java.base@11.0.14.1/ThreadPoolExecutor.java:628)
at java.lang.Thread.run(java.base@11.0.14.1/Thread.java:829)

"pool-2-thread-5" #80 prio=5 os_prio=0 cpu=17.83ms elapsed=1584.30s tid=0x000055864597e800 nid=0x59 waiting on condition  [0x00007fdb9463e000]
AI写代码
bash

需要重点关注：

"Found one Java-level deadlock"：如果存在死锁，jstack会在输出的开头部分明确指出，并显示死锁的详情。

"java.lang.Thread.State"：每个线程的状态，特别是BLOCKED状态的线程，因为它们可能在等待其他线程释放锁。

注意事项：

使用 jstack 可能会对性能产生一定影响，因为它需要暂停所有线程来获取堆栈跟踪。

jstack 需要 Java 进程的调试权限，因此在某些受限环境中可能无法使用。

jstack 输出的信息量可能非常大，特别是对于多线程的应用程序，因此通常需要结合其他工具（如 grep）来过滤和分析输出。

2.1.3 jmap
主要用于生成Java堆转储快照（heap dump），分析内存使用情况和定位内存泄漏等问题。

jmap -dump:format=b,file=heapdump.hprof <pid>
AI写代码
bash
生成dump.hprof文件，使用visualVM打开文件，查看具体详情。

2.2 visualVM工具
VisualVM（Visual Monitoring, Profiling and Debugging of Java Applications）是一个强大的多合一工具，用于监控、分析和调试Java应用程序。它是NetBeans IDE的一部分，但也可以在独立模式下使用。VisualVM提供了以下功能：

性能监控：

实时监控CPU和内存使用情况。

跟踪垃圾回收活动。

监控线程和锁的使用。

分析：

收集和分析CPU和内存的采样或跟踪数据。

分析应用程序的运行时行为，包括方法调用和内存分配。

堆转储分析：

查看和分析堆转储文件，以识别内存泄漏和内存消耗模式。

使用不同的算法进行内存泄漏检测。

线程分析：

分析线程的运行时信息，包括状态和堆栈跟踪。

检测死锁和线程争用。

方法剖析：

记录方法调用和执行时间，帮助识别性能瓶颈。

GC日志分析：

解析和可视化垃圾收集日志。
————————————————
版权声明：本文为CSDN博主「菜鸟起航ing」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44929475/article/details/144337552