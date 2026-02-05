# Tcpdump抓包和内容查看
有时候需要在服务端抓包来确定问题原因
可以使用tcpdump命令拦截网络请求，并使用wireshark查看抓包内容

## 1.tcpdump 命令简介

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

## 2. 安装wireshark

> Wireshark Official Website
> https://www.wireshark.org/download.html

![2026-02-03_193847.png](pic20260203/2026-02-03_193847.png)

## 3. 查看抓包内容
![2025-11-16_090612.png](pic20260203/2025-11-16_090612.png)

![2026-01-31_153248.png](pic20260203/2026-01-31_153248.png)

