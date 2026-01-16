# 引望测试环境FTS部署过程记录

## 1.FTS简介
FTS: 文件传输服务（File Transmission Service），是MQS 团队自研的 服务，用于实现大消息的传递。
即当消息超过2048字节的时候，SDK会自动选择FTS方式进行消息传递。 消息发送或接收方不需关注具体的实现机制。

> 使用FTS大消息传递有哪些条件和限制
> https://3ms.huawei.com/km/groups/1002717/blogs/details/17836130?ctype=-1

## 2.部署

> FTS部署
> https://wiki.huawei.com/domains/137/wiki/4138/WIKI202505076748883

## 3.测试环境部署过程

已成功部署一台
![2026-01-09_103049.png](pic20260109/2026-01-09_103049.png)
部署第二台FTS过程记录如下

### 3.1 登录
主机名称:kweshdsita01068

IP:10.42.128.40

初始密码:VC0SxTM198_9

### 3.2 将部署文件放到上传到ec2，并解压

在/tmp目录执行以下命令

```shell
wget http://mirrors.myhuaweicloud.com/repo/mirrors_source.sh && bash mirrors_source.sh
yum install lrzsz
yum install geoip
```

> 通过lrzsz来拖拽上传文件到服务器上
> https://3ms.huawei.com/km/blogs/details/9753911

### 3.3 修改配置文件

vim /usr/local/openresty/nginx/conf/nginx.conf
![2026-01-09_120731.png](pic20260109/2026-01-09_120731.png)

vim /usr/local/openresty/nginx/lua/config.lua（IP和编号关系，此处需要记录所有的机器，01和02都要写，后续扩容也要写进来，注意最后一个没有逗号）

```lua
[root@shapheds04616 lua]# cat config.lua
-- config file

local _M = {}

_M['nodes_ip'] = {
    ['01'] = '10.42.129.50',
    ['02'] = '10.42.128.40'
}

_M['sgov_auth_url'] = 'https://oauth2-op-beta.yinwang.com/umws4login/services/Authentication'

_M['token_expire_seconds'] = 180

_M['his3_iam_auth_url'] = 'https://apig-beta.hieds.net/api/iam/auth/token'

_M['auth_white_list'] = {
    'XXXXXXXXXXXXXXXXXXXXXXXXX'
}

return _M
```

### 3.4、启动服务

```shell
# 启动nginx
systemctl start openresty.service 
# 进程守护，开机自启
systemctl enable openresty.service
# 验证功能
curl -H "Content-Type: application/json" -H "appid:b995709d9d0343b2830ba09dbc317f32" -H "token:2RBH8zNegCldqhSd/SowMT2Wg1cZRs/A6rtz1UWn" -H "account:b995709d9d0343b2830ba09dbc317f32" -H "enterprise:8c8b823898bae7f80198bb20e3590002" -X POST -d 'hello' "http://10.42.128.40:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```

执行结果
```shell
[root@kweshdsita01068 ~]# curl -H "Content-Type: application/json" -H "appid:b995709d9d0343b2830ba09dbc317f32" -H "token:2RBH8zNegCldqhSd/SowMT2Wg1cZRs/A6rtz1UWn" -H "account:b995709d9d0343b2830ba09dbc317f32" -H "enterprise:8c8b823898bae7f80198bb20e3590002" -X POST -d 'hello' "http://10.42.128.40:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
20260109022cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

### 3.5 给第一台服务器添加配置并重启

```text
_M['nodes_ip'] = {
['01'] = '10.42.129.50',
['02'] = '10.42.128.40'
}
```

重启第一台服务器

### 3.6 确认服务部署OK后，申请ELB，挂载2台机器IP

![2026-01-09_150325.png](pic20260109/2026-01-09_150325.png)

fts-beta-edc

fts-beta-edc-elb

![2026-01-09_151439.png](pic20260109/2026-01-09_151439.png)

![2026-01-09_151803.png](pic20260109/2026-01-09_151803.png)

![2026-01-09_151831.png](pic20260109/2026-01-09_151831.png)

![2026-01-09_152015.png](pic20260109/2026-01-09_152015.png)

### 3.7 申请DNS，DNS指向ELB的IP（VIP）

![2026-01-09_152454.png](pic20260109/2026-01-09_152454.png)

![2026-01-09_155056.png](pic20260109/2026-01-09_155056.png)

![2026-01-09_155327.png](pic20260109/2026-01-09_155327.png)

![2026-01-09_155515.png](pic20260109/2026-01-09_155515.png)

fts-beta-edc
10.42.129.240(VIP)

fts-beta.ywit-beta.yinwang.com

### 3.8 验证通过域名上传文件

curl -H "Content-Type: application/json" -H "appid:b995709d9d0343b2830ba09dbc317f32" -H "token:2RBH8zNegCldqhSd/SowMT2Wg1cZRs/A6rtz1UWn" -H "account:b995709d9d0343b2830ba09dbc317f32" -H "enterprise:8c8b823898bae7f80198bb20e3590002" -X POST -d 'hello' "http://fts-beta.ywit-beta.yinwang.com/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

```shell
[root@mqs-umpnamesrv00 ~]# curl -H "Content-Type: application/json" -H "appid:b995709d9d0343b2830ba09dbc317f32" -H "token:2RBH8zNegCldqhSd/SowMT2Wg1cZRs/A6rtz1UWn" -H "account:b995709d9d0343b2830ba09dbc317f32" -H "enterprise:8c8b823898bae7f80198bb20e3590002" -X POST -d 'hello' "http://fts-beta.ywit-beta.yinwang.com/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
20260109022cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
[root@mqs-umpnamesrv00 ~]# 
```
部署成功

![2026-01-09_161751.png](pic20260109/2026-01-09_161751.png)

### 3.9 登录MQS的两台umpnamesrv， 配置fts地址：

![2026-01-09_160717.png](pic20260109/2026-01-09_160717.png)

vim kvConfig.json
{"configTable":{"fts":{"fileServiceUrl":"http://fts-beta.ywit-beta.yinwang.com/file"}}}


### 3.10 配置完，重启umpnamesrv，注意要切到umpadmin运行账号执行重启

![2026-01-09_163804.png](pic20260109/2026-01-09_163804.png)

![2026-01-09_170235.png](pic20260109/2026-01-09_170235.png)


```shell
[root@mqs-umpnamesrv00 umpnamesrv]# su - umpadmin
Last login: Fri Nov  7 17:53:22 CST 2025 on pts/0
[umpadmin@mqs-umpnamesrv00 ~]$ jps -l
8114 /data01/ump/mqs-prod/umpnamesrv/umpnamesrv
8117 /data01/ump/mqs-prod/umpconnector/umpconnector
2538 sun.tools.jps.Jps
[umpadmin@mqs-umpnamesrv00 ~]$ jps -v
8114 umpnamesrv -Xms2g -Xmx2g -Xmn1g -XX:PermSize=128m -XX:MaxPermSize=320m -XX:-OmitStackTraceInFastThrow -XX:+UseConcMarkSweepGC -XX:+UseCMSCompactAtFullCollection -XX:CMSInitiatingOccupancyFraction=70 -XX:+CMSParallelRemarkEnabled -XX:SoftRefLRUPolicyMSPerMB=0 -XX:+CMSClassUnloadingEnabled -XX:SurvivorRatio=8 -XX:+DisableExplicitGC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/data01/ump/logs/ump/ -XX:+CrashOnOutOfMemoryError -Djava.ext.dirs=/data01/ump/java/jdk1.8.0_352/jre/lib/ext
8117 umpconnector -Xms4g -Xmx4g -Xmn2g -XX:PermSize=128m -XX:MaxPermSize=320m -XX:-OmitStackTraceInFastThrow -XX:+UseConcMarkSweepGC -XX:+UseCMSCompactAtFullCollection -XX:CMSInitiatingOccupancyFraction=70 -XX:+CMSParallelRemarkEnabled -XX:SoftRefLRUPolicyMSPerMB=0 -XX:+CMSClassUnloadingEnabled -XX:SurvivorRatio=8 -XX:+DisableExplicitGC -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/data01/ump/logs/ump/ -XX:+CrashOnOutOfMemoryError -Djava.ext.dirs=/data01/ump/java/jdk1.8.0_352/jre/lib/ext
2990 Jps -Denv.class.path=.:/data01/ump/java/jdk1.8.0_352/lib/dt.jar:/data01/ump/java/jdk1.8.0_352/lib/tools.jar -Dapplication.home=/data01/ump/java/jdk1.8.0_352 -Xms8m
[umpadmin@mqs-umpnamesrv00 ~]$ 
```
已成功升级一个
![2026-01-09_175111.png](pic20260109/2026-01-09_175111.png)

![2026-01-09_175300.png](pic20260109/2026-01-09_175300.png)

> JDK神器之jps（虚拟机进程状态工具）
> https://blog.csdn.net/zwz1342/article/details/145610714


> jps(JVM Process Status Tool)：虚拟机进程状态工具，可以列出正在运行的虚拟机进程，并显示虚拟机执行主类（Main Class，main()函数所在的类）的名称，以及这些进程的本地虚拟机的唯一ID（LVMID,Local Vitual Machine Identifier）,它是使用频率最高的JDK命令行工具，因为其他JDK工具大多需要输入它查询到的LVMID来确定要监控的是哪一个虚拟机进程。
> 对于本地虚拟机进程来说，LVMID与操作系统进程ID（PID，Process Identifier）是一致的。
> 如果同时启动了多个虚拟机进程，无法根据进程名称定位时，那就只能依靠jps命令显示主类的功能才能区分了。






