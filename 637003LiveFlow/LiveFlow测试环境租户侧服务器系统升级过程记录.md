# LiveFlow测试环境租户侧服务器系统升级过程记录

## 1.升级背景
因CentOS日落，需要把存量CentOS的服务器升级到Huawei Cloud EulerOS 2.0。服务器上部署了ETCD服务。

## 2.涉及的服务器
### 2.1 OP侧
EKS是承载流程的，EC2是承载ETCD的

EC2，有3台，用来做ETCD的
![2026-01-04_101044.png](pic20260104/2026-01-04_101044.png)
因OP侧3台服务器中ETCD的Leader无法切换，导致有一台ETCD服务器无法正常升级。

### 2.2 租户侧
EC2
![2026-01-04_101654.png](pic20260104/2026-01-04_101654.png)
## 3. 升级方案
### 3.1 总体思路
先备份服务器上ETCD的数据，然后关闭服务器上的ETCD服务，然后验证LiveFlow功能是否正常，功能正常再关闭服务器，升级操作系统。
### 3.1 验证LiveFlow功能方法
在LiveFlow页面上验证LiveFlow流程能顺利进行
判断标准：
1. 在监控运维-->流程追踪中，查看任务能执行成功
2. 流程能正常部署和卸载
3. 有HTTP请求的流程能正常响应

#### 3.1.1 任务能执行成功
选择测试环境中WMS服务(appid：6656fca4738a4a34865a71328aea841a)中的流程"资源中心发运回写指令"作为观测对象，
![2025-12-10_151904.png](pic20251210/2025-12-10_151904.png)
该流程从每小时的 0 分 0 秒开始，每隔 5 分钟执行一次
![2025-12-10_152005.png](pic20251210/2025-12-10_152005.png)
在监控运维--》流程追踪中 查看该任务是不是能执行成功
![2025-12-10_152251.png](pic20251210/2025-12-10_152251.png)


#### 3.1.2 流程能正常部署和卸载
流程能正常部署和卸载
自己创建了一个流程LiveFlowVerify
ETCD服务关闭后确认能正常部署和卸载
![2025-12-11_113914.png](pic20251210/2025-12-11_113914.png)

![2025-12-11_123614.png](pic20251210/2025-12-11_123614.png)

#### 3.1.3 有HTTP请求的流程能正常响应

回款与对账数据准备服（appid：b40223cdee5a4486acfe375b3a13c304）有一个流程getTaskStartTime_CCS_PRO使用了HTTP请求，可用此流程校验服务器功能是否正常
apigp-beta.hieds.net/api/sit/getTaskStartTime_CCS_PRO
成功后返回如下图
![2025-12-31_192444.png](pic20251210/2025-12-31_192444.png)

最终，验证etcd集群功能正常，LiveFlow服务功能正常

### 3.3 CentOS服务器升级成Huawei Cloud EulerOS 2.0
关闭服务器
替换系统盘
启动服务器

## 4.操作步骤

### 4.1.备份etcd
```shell
zip -r etcd1.zip /data01/

lcd D:\Users\ywbeta_h60094160_13\Desktop\etcd-backup
```
所有主机都要备份，比如备份到堡垒机桌面etcd-backup文件夹
![2026-01-14_142059.png](pic20260104/2026-01-14_142059.png)

![2026-01-14_142414.png](pic20260104/2026-01-14_142414.png)

![2026-01-14_142634.png](pic20260104/2026-01-14_142634.png)

![2026-01-14_142707.png](pic20260104/2026-01-14_142707.png)
备份好以后如下图:
![2026-01-14_142923.png](pic20260104/2026-01-14_142923.png)

### 4.2.检查集群状态

```shell
./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint health
```

```shell
[root@kweshdsita00126 etcd-v3.4.16-linux-amd64]# ./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint health
10.42.129.31:2379 is healthy: successfully committed proposal: took = 1.33552ms
10.42.128.46:2379 is healthy: successfully committed proposal: took = 1.616814ms
10.42.128.113:2379 is healthy: successfully committed proposal: took = 2.149119ms
```

### 4.3.验证ETCD Leader可以转移
现有主机
kweshdsita00126  10.42.128.46
kweshdsita00127  10.42.129.31
kweshdsita00128  10.42.128.113

```shell
[root@kweshdsita00126 etcd-v3.4.16-linux-amd64]# ./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint status -w table
+--------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|      ENDPOINT      |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+--------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|  10.42.128.46:2379 | e67c26c7efd08c07 |  3.4.16 |  1.6 MB |     false |      false |         7 |    1439263 |            1439263 |        |
|  10.42.129.31:2379 | e2110c4b9bd40704 |  3.4.16 |  1.6 MB |      true |      false |         7 |    1439263 |            1439263 |        |
| 10.42.128.113:2379 | 4209ee4e59ca797e |  3.4.16 |  1.6 MB |     false |      false |         7 |    1439263 |            1439263 |        |
+--------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+

./etcdctl  move-leader e2110c4b9bd40704
```
![2026-01-14_143438.png](pic20260104/2026-01-14_143438.png)
ETCD Leader成功转移
![2026-01-14_143651.png](pic20260104/2026-01-14_143651.png)

### 4.4.关闭ETCD进程并验证LiveFlow流程能顺利进行
关闭ETCD进程
```shell
ps -ef | grep etcd

kill -9 pid
```
![2026-01-14_145231.png](pic20260104/2026-01-14_145231.png)

```shell
# 检查集群状态
./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint status -w table
# 能正常查询数据
./etcdctl get --prefix liveflow:route:
```
![2026-01-14_145554.png](pic20260104/2026-01-14_145554.png)

### 4.5 验证LiveFlow流程能顺利进行

> 参考 3.1 验证LiveFlow功能方法

最终，验证etcd集群功能正常，LiveFlow服务功能正常

### 4.6 在EC2上关机

在EC2上把要升级的主机关机
![2026-01-14_144036.png](pic20260104/2026-01-14_144036.png)
确认
![2026-01-14_150158.png](pic20260104/2026-01-14_150158.png)

### 4.7 在EC2上替换系统盘
在EC2上替换系统盘
![2026-01-14_150407.png](pic20260104/2026-01-14_150407.png)
确认
![2026-01-14_150448.png](pic20260104/2026-01-14_150448.png)
选择镜像:Huawei_Cloud_EulerOS_2.0_YWbeta_sp202511
![2026-01-14_150621.png](pic20260104/2026-01-14_150621.png)

![2026-01-14_150750.png](pic20260104/2026-01-14_150750.png)

![2026-01-14_150845.png](pic20260104/2026-01-14_150845.png)
等待系统盘更换成功
### 4.8 配置升级后的主机
登录到系统成功升级的主机
查看操作系统信息
```shell
cat /etc/os-release
cat /etc/hce-release
```
![2026-01-14_155622.png](pic20260104/2026-01-14_155622.png)

```shell
[root@kweshdsita00126 ~]# cat /etc/os-release
NAME="Huawei Cloud EulerOS"
VERSION="2.0 (x86_64)"
ID="hce"
VERSION_ID="2.0"
PRETTY_NAME="Huawei Cloud EulerOS 2.0 (x86_64)"
ANSI_COLOR="0;31"

[root@kweshdsita00126 ~]# cat /etc/hce-release
Huawei Cloud EulerOS release 2.0 (West Lake)
```

```shell
df -h
lsblk
echo "/dev/vdb /data01 xfs defaults 1 2" >> /etc/fstab
mkdir -p /data01
mount /dev/vdb /data01
df -h
```
确保数据盘能正常加载
![2026-01-14_151516.png](pic20260104/2026-01-14_151516.png)

查看数据盘上是否有etcd数据，如果有数据可以直接使用，如果没有可以使用备份数据解压

把etcd备份数据传到新主机上
```shell

lcd D:\Users\ywbeta_h60094160_13\Desktop\etcd-backup

put etcd1.zip 
```
![2026-01-14_151655.png](pic20260104/2026-01-14_151655.png)

解压
```shell
unzip etcd1.zip 
```
![2026-01-14_152327.png](pic20260104/2026-01-14_152327.png)

![2026-01-14_152430.png](pic20260104/2026-01-14_152430.png)

![2026-01-14_152601.png](pic20260104/2026-01-14_152601.png)
重启ETCD服务
![2026-01-14_152819.png](pic20260104/2026-01-14_152819.png)

查看ETCD集群状态
```shell
# 检查集群状态
./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint status -w table
# 能正常查询数据
./etcdctl get --prefix liveflow:route:
```
![2026-01-14_153016.png](pic20260104/2026-01-14_153016.png)

```shell
# 检查集群状态
./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint status -w table
# 转移Leader
./etcdctl  move-leader e2110c4b9bd40704
# 检查集群状态，验证Leader是否转换
./etcdctl --endpoints=10.42.128.46:2379,10.42.129.31:2379,10.42.128.113:2379 endpoint status -w table
# 能正常查询数据
./etcdctl get --prefix liveflow:route:
```
ETCD Leader切回
![2026-01-14_153525.png](pic20260104/2026-01-14_153525.png)

### 4.9 验证升级后LiveFlow功能是否正常

## 5.验证LiveFlow功能
全部升级成功后再验证LiveFlow功能，总结升级过程




























