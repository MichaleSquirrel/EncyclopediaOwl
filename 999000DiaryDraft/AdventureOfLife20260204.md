Wednesday February 4 Day 035 week 6 of 2026

## 1.TodoList


## 2.简单自我介绍
姓名:毛关松

2022年3月24号入职左侧的融合联接，

2025年12月入职引望 数字化及IT装备部门

2025年12月17日通过Java工作级

![2026-02-02_183333.png](pic20260204/2026-02-02_183333.png)

2026年1月14号通过Java专业级

![2026-02-02_183451.png](pic20260204/2026-02-02_183451.png)


![D7E644C8-ED3C-4AB6-A1BF-B043F651C38F.JPG](pic20260204/D7E644C8-ED3C-4AB6-A1BF-B043F651C38F.JPG)


## 3.幸福来的猝不及防




## 4. MQS FTS镜像制作过程
生产OP侧FTS服务器系统升级

> 生产环境OP侧EC2地址
> https://console.ywit-op.yinwang.com/rmv3/#/hisims/ListImage?active_name=imageTabVM&app_id=00000000000000000000000000000092&servicealias=ec2ims


### 4.1 创建主机镜像

登录生产环境OP侧EC2，根据FTS服务器主机规格创建主机镜像
![2026-02-04_110531.png](pic20260204/2026-02-04_110531.png)

![2026-02-04_111257.png](pic20260204/2026-02-04_111257.png)

![2026-01-28_210521.png](pic20260204/2026-01-28_210521.png)

镜像主机IP为10.201.32.211

### 4.2 在主机镜像中部署FTS服务

> FTS部署
> https://wiki.huawei.com/domains/137/wiki/4138/WIKI202505076748883
>
> 引望测试环境租户侧FTS部署过程记录
> https://wiki.rnd.yinwang.com/domains/300337/wiki/1000372/WIKI2026011516916360

通过堡垒机登录主机镜像，并部署FTS服务



### 4.3 通过WePAM获取生产环境配置
运行服务
通过 运维控制 WePAM 申请例外流程，获取到生产环境服务器账号，并查看相应配置，用于部署FTS
![2026-02-04_113531.png](pic20260204/2026-02-04_113531.png)

```lua
[root@shapheds04616 lua]# cat config.lua
-- config file

local _M = {}

_M['nodes_ip'] = {
    ['01'] = '10.201.32.169',
    ['02'] = '10.201.32.53'
}

_M['sgov_auth_url'] = 'https://oauth2-op-beta.yinwang.com/umws4login/services/Authentication'

_M['token_expire_seconds'] = 180

_M['his3_iam_auth_url'] = 'https://apig.hieds.net/api/iam/auth/token'

_M['auth_white_list'] = {
    'XXXXXXXXXXXXXXXXXXXXXXXXX'
}

return _M
```

### 4.4 验证服务可用性

部署完成后使用以下命令验证FTS服务可用性，因为镜像主机IP为10.201.32.211
```shell
curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.32.211:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
```

### 4.5 根据历史经验
根据历史经验，镜像自动挂载会有问题，如果实例规格不一样,自动挂载会起不来,因此要注释挂载的配置
注释过程录像:
![2026-02-04_115844.png](pic20260204/2026-02-04_115844.png)


/etc/fstab注释截图
![2026-02-04_141702.png](pic20260204/2026-02-04_141702.png)

> /etc/rc.local 是一个经典的开机自启动脚本文件

FTS服务器原主机rc.local文件没有配置自启动服务,所以镜像也没有配置
![2026-02-04_120734.png](pic20260204/2026-02-04_120734.png)
先关机,再制作镜像
![2026-02-04_142440.png](pic20260204/2026-02-04_142440.png)


![2026-02-04_142753.png](pic20260204/2026-02-04_142753.png)


![2026-02-04_142948.png](pic20260204/2026-02-04_142948.png)

![2026-02-04_143127.png](pic20260204/2026-02-04_143127.png)


### 4.6 使用镜像创建一台主机
使用镜像创建一台主机,并验证功能是否正常

![2026-02-04_143603.png](pic20260204/2026-02-04_143603.png)

```shell
curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.33.154:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

```

![2026-01-29_162542.png](pic20260204/2026-01-29_162542.png)

## 5.变更流程

### 5.1 先提事件单
以op侧为例
https://console.ywit-op.yinwang.com/itsm/?servicealias=itsm&app_id=b8846618c8d0485e89bdef35f35e63df#/incident/createOrder

![2026-02-04_152622.png](pic20260204/2026-02-04_152622.png)

![2026-02-04_152927.png](pic20260204/2026-02-04_152927.png)


### 5.2 提变更单

![2026-02-04_153426.png](pic20260204/2026-02-04_153426.png)



![2026-02-04_153559.png](pic20260204/2026-02-04_153559.png)
变更来源选择事件单
![2026-02-04_153846.png](pic20260204/2026-02-04_153846.png)

### 5.3 变更登记
https://onebox.huawei.com/v/0b6ca1c009daa33367a920300570fff9?type=1&sheet=%E5%BC%95%E6%9C%9BIT%E5%B9%B3%E5%8F%B0%E5%8F%98%E6%9B%B4%E7%99%BB%E8%AE%B0%E8%A1%A8

![2026-02-04_152336.png](pic20260204/2026-02-04_152336.png)


### 5.4 评审会评审

![2026-02-04_154053.png](pic20260204/2026-02-04_154053.png)


### 5.5 变更评审会纪要

变更描述：【资源与连接】【融合联接】生产OP侧MQS服务器3台无进程服务器关机，2台服务器CentOS系统升级
变更时间窗：2026/02/09 20:00 - 2026/02/09 23:59
业务影响：无影响
评审意见：无
遗留问题：无
评审结论：通过



变更描述：【资源与连接】【融合联接】【规则引擎LiveRule】规则引擎op侧configmap修改配置
变更时间窗：2026/02/09 20:00 - 2026/02/09 23:55
业务影响：无
评审意见：验证加步骤
遗留问题：无
评审结论：通过

### 5.6 变更实施




## 6.


grep "/log/request" *.log


## 7.堡垒机使用和安装

1. 学习CentOS下载和虚拟机安装，并在其上部署RocketMQ等服务
2. 部署MQS相关服务，使用本地代码调用
3. 部署APIG服务，使用代码调用
4. 学习网络安全中有关Linux章节
5. 学习openResty和Lua
6. 学习RocketMQ
7. 


## 8.同事信息

姓名 lishuangping 30036208
账号 l30036208
手机 +86 15779384052(李双平)
邮箱 lishuangping1@h-partners.com
服务部门 智能汽车解决方案数字化及IT装备部(智能汽车解决方案BU)
部门主管 丁旭
当地时间 08:53（24小时制）

姓名 linanqing 30036344
账号 l30036344
手机 +86 17773067125
邮箱 linanqing@h-partners.com
服务部门 智能汽车解决方案数字化及IT装备部(智能汽车解决方案BU)
部门主管 丁旭
地址 中国(China) -深圳(Shenzhen)-龙华区九华山A1栋
座位 3楼
当地时间 08:53（24小时制）

姓名 lishaolong 30046743
账号 l30046743
手机 +86 15827516605
邮箱 lishaolong17@h-partners.com
服务部门 智能汽车解决方案数字化及IT装备部(智能汽车解决方案BU)
部门主管 丁旭
当地时间 08:53（24小时制）