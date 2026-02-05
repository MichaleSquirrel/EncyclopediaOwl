Tuesday February 3 Day 034 week 6 of 2026

## 1.TodoList





## 2.YW侧要增加部署HDP作业助手

明超 wx1347541 2026-02-02 15:11
你好，YW侧要增加部署HDP作业助手，这个服务依赖规则引擎和规则引擎3.0的接口，
/liverule/api/dorunning	e9fc587da39440cb97693542d9a7e081	APIGW	融合联接	消息联接	规则引擎	规则引擎
/liverule/api/public	        9d918a4b9bba411b88abfade54af8ff3	APIGW	融合联接	消息联接	规则引擎	规则引擎
规则公共服务接口	        2b9f70b8c7a4486f95f5616ab63ded3a	APIGW	融合联接	消息联接	规则引擎	规则引擎3.0
规则调用接口	                c9ad96fe50e94deaad5e06dc1ffbd9cf	APIGW	融合联接	消息联接	规则引擎	规则引擎3.0
毛关松 30026548 2026-02-02 15:12
要添加授权是吗？
明超 wx1347541 2026-02-02 15:12
麻烦你帮忙看下  1、规则引擎3.0和规则引擎有什么差异，规则引擎3.0是不是在YW侧没部署，能否替换为规则引擎的上边两个接口
2、规则引擎应该是已经在YW侧部署了的，这两个接口与左侧是否一样
毛关松 30026548 2026-02-02 15:18
好的
毛关松 30026548 2026-02-02 15:23
是生产环境？
明超 wx1347541 2026-02-02 15:23
现在还没部署，只是先分析下这些依赖的接口是否要调整
明超 wx1347541 2026-02-03 08:43
松哥，能帮忙确认下不
毛关松 30026548 2026-02-03 09:56
应该要使用规则引擎3.0的接口


## 3.写变更方案

MQS OP侧 FTS服务器升级方案

1、那几台没用的关机
2、OP侧的FTS升级


李胜沛 00847799 2026-01-27 12:10
kweshcsitd01407
kweshcsitd01408
kweshcsitd01052
这三台，我看了下没有java和nginx进程，应该是没用的，下周变更关机先吧
李胜沛 00847799 2026-01-27 12:11
op侧的


李胜沛 00847799 2026-01-28 10:34
OP侧的两台FTS，没用流量，升级无风险，也可以放在第一批升OS
毛关松 30026548 2026-01-28 10:36
好
李胜沛 00847799 2026-01-28 10:36
kweshcsitd00260
kweshcsitd00251



kweshcsitd00260
kweshcsitd00251

登录ec2主页https://console.ywit-op.yinwang.com/rmv3/#/hisec2/VmList?servicealias=ec2&app_id=00000000000000000000000000000092
使用已制作好的私有镜像fts_hce_image替换系统盘，

确认配置文件配置，
vim /usr/local/openresty/nginx/conf/nginx.conf

启动FTS服务

启动nginx
systemctl start openresty.service
进程守护，开机自启
systemctl enable openresty.service


验证功能
执行以下命令验证FTS功能正常
curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.33.154:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


## 4.
tcpdump -i any -s 0 host xx.xx.xx.xx and port 8002  -vv -w filename.cap

-i 指定网卡，any表示所有网卡  
host 指定的对端IP（该IP到本机的包）  
post 指定端口  
-vv 显示抓了多少包  
-w抓包文件.cap的保存位置

tcpdump -vv '(host 127.0.0.1 or host 127.0.0.2)' and port 80 -w 1105.cap

tcpdump -vv '(host 10.41.0.118 or host 10.41.1.249)' and port 8900 -w analyzer.cap


tcpdump -vv '(host 10.41.0.118 or host 127.0.0.1)' and port 8081 -w analyzer1.cap


tcpdump -vv '(host 10.41.0.118 or host 10.41.1.249)' -w analyzer1.cap


tcpdump -vv '(host 10.41.0.118 or host 10.41.1.249)' -w analyzer1.cap

tcpdump -i any port 8081  -vv -w analyzer.cap


tcpdump -vv -i any -w analyzer3.cap


http.request.uri contains "/publicservices/mid/midMemberApplyRecordService/syncMemberInfo"


http.request.uri contains "syncMemberInfo"


10.42.129.158


tcpdump -vv '(host 10.42.129.158)' -w analyzer1.cap


## 4.
我看了一下部署包，报错来自这里
at com.huawei.it.eip.apigw.portal.service.test.impl.ApiTestServiceImpl.parseTestHistoryResponse(ApiTestServiceImpl.java:221)

![2026-02-03_161925.png](pic20260203/2026-02-03_161925.png)
问题根源就是部署包没有对content为空做处理。

新代码
![2026-02-03_162336.png](pic20260203/2026-02-03_162336.png)


## 5.Tcpdump抓包和内容查看
使用tcpdump命令拦截网络请求，并使用wireshark查看抓包内容

有时候需要在服务端抓包来确定问题原因
使用tcpdump命令拦截网络请求，并使用wireshark查看抓包内容

### 5.1 tcpdump 命令简介


tcpdump -i any -s 0 host xx.xx.xx.xx and port 8002  -vv -w filename.cap

-i 指定网卡，any表示所有网卡  
host 指定的对端IP（该IP到本机的包）  
post 指定端口  
-vv 显示抓了多少包  
-w抓包文件.cap的保存位置

> Linux：tcpdump抓包指令
> https://www.cnblogs.com/ShineLeBlog/p/18135595


# 监听主机10.41.0.118和主机10.41.1.249
tcpdump -vv '(host 10.41.0.118 or host 10.41.1.249)' -w analyzer1.cap


# 监听主机10.41.0.118和主机10.41.1.249的8080端口，并将抓包文件保存到analyzer1.cap
tcpdump -vv '(host 10.41.0.118 or host 10.41.1.249)' and port 8081 -w analyzer1.cap

# 监听所有网络请求
tcpdump -vv -i any -w analyzer3.cap


以在APIG服务器抓包为例

![2026-02-03_191425.png](pic20260203/2026-02-03_191425.png)



多个服务器一起抓包可以使用撰写模式
![2026-02-03_191812.png](pic20260203/2026-02-03_191812.png)


![2026-02-03_192325.png](pic20260203/2026-02-03_192325.png)


把抓包文件拷贝到堡垒机
![2026-02-03_192840.png](pic20260203/2026-02-03_192840.png)

把堡垒机文件复制到本地电脑



### 5.2 安装wireshark

> Wireshark Official Website
> https://www.wireshark.org/download.html

![2026-02-03_193847.png](pic20260203/2026-02-03_193847.png)

> 内网下载链接
> https://clouddrive.huawei.com/p/9dff50c0b61196bddd95dfe09663bf9b

> 【2025最新】Wireshark安装保姆级教程＋Wireshark抓包(超详细)，建议收藏！
> https://blog.csdn.net/A1_3_9_7/article/details/154700079

### 5.3 查看抓包内容

找到cap文件
![2026-02-03_204033.png](pic20260203/2026-02-03_204033.png)

过滤特定URL的包
> http.request.uri=="/apigw_portals/data/api/test"
> http.request.uri contains "/saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser"

![2026-02-03_204903.png](pic20260203/2026-02-03_204903.png)

查看包的具体内容
![2025-11-16_090612.png](pic20260203/2025-11-16_090612.png)

![2026-01-31_153248.png](pic20260203/2026-01-31_153248.png)