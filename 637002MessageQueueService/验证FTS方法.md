# 验证FTS方法

## 1.使用Postman调用FTS接口验证

### 1.1 下载一个计算SHA256值的工具

> 7zip官网
> https://www.7-zip.org/

![2026-01-15_154307.png](pic20260115/2026-01-15_154307.png)
安装后可查看文件的SHA256的值
![2026-01-15_154340.png](pic20260115/2026-01-15_154340.png)
![2026-01-15_154542.png](pic20260115/2026-01-15_154542.png)

复制SHA256值备用
```txt
997d6ce78291343732c05426292f613e0cb32096a458fa52326ba9c054bf42ef
```

### 1.2 Postman安装

> 【工具分享】免登陆版postman
> https://3ms.huawei.com/km/groups/3956009/blogs/details/22028993

需在堡垒机上调用
### 1.3 Postman请求接口验证
其中sha256为上一步中获取的SHA256值
http://fts-beta.ywit-beta.yinwang.com/file?sha256=997d6ce78291343732c05426292f613e0cb32096a458fa52326ba9c054bf42ef

![2026-01-15_162625.png](pic20260115/2026-01-15_162625.png)

> FTS接口文档
> https://wiki.huawei.com/domains/137/wiki/4138/WIKI2021122301051

![2026-01-15_165326.png](pic20260115/2026-01-15_165326.png)

token为创建时获取的AccountSecret

![2026-01-15_165749.png](pic20260115/2026-01-15_165749.png)

![2026-01-15_170206.png](pic20260115/2026-01-15_170206.png)

## 2.发送大消息验证

### 2.1 发送大消息
准备一个超过2M的文件，放在"D:\m30026548\jdk1.8.0_471\bin\mqs_big_message\body.txt"目录下
![2026-01-15_142952.png](pic20260115/2026-01-15_142952.png)

![2026-01-15_143314.png](pic20260115/2026-01-15_143314.png)

编写发送消息的代码

```java
package com.yinwang;


import com.huawei.his.mqs.client.producer.Producer;
import com.huawei.his.mqs.common.exception.UmpException;
import com.huawei.his.mqs.common.message.Message;

import java.nio.charset.StandardCharsets;

public class ProducerBigMessageDemo {

    public static void main(String[] args) {
        final String appId = "b995709d9d0343b2830ba09dbc317f32";
        final String topic = "T_lunar_new_year";
        final String umpnamesrv = "mqs-umpnamesrv00-beta.yinwang.com:9776;mqs-umpnamesrv01-beta.yinwang.com:9776";

        ReadFileUtils readFileUtils = new ReadFileUtils();

        String body = readFileUtils.readFile();
        System.out.println(body);
        Producer producer = new Producer();
        producer.setEnterprise("8c8b823898bae7f80198bb20e3590002");
        producer.setProjectId("b995709d9d0343b2830ba09dbc317f32");
        producer.setAccount("b995709d9d0343b2830ba09dbc317f32");
        producer.setAccountSecret("*******************************");

        producer.setUmpNamesrvUrls(umpnamesrv);
        producer.setTopic(topic);
        // 在发送消息前, 必须调用start方法来启动Producer, 只需调用一次即可
        try {
            producer.start();
        } catch (UmpException e) {
            throw new RuntimeException(e);
        }
        // 发送消息
        Message msg = new Message();
        msg.setBody(body.getBytes(StandardCharsets.UTF_8));
        try {
            producer.send(msg);
        } catch (UmpException e) {
            throw new RuntimeException(e);
        }
    }
}
```

![2026-01-15_143554.png](pic20260115/2026-01-15_143554.png)


打包成jar包，复制到堡垒机中，
![2026-01-15_143912.png](pic20260115/2026-01-15_143912.png)
切换到指定目录，执行命令java -jar mqs_big_message\mqs-example.jar，发送消息，发送成功如上图所示
```shell
java -jar mqs_big_message\mqs-example.jar
```

### 2.2 验证消息发送成功
进入MQS页面搜索Topic  "T_lunar_new_year",确认方发送时间、消息大小、客户端IP都符合实际情况，确认消息发送成功。

![2026-01-15_144522.png](pic20260115/2026-01-15_144522.png)
客户端IP和MQS页面显示的一致
![2026-01-15_144745.png](pic20260115/2026-01-15_144745.png)

登录FTS服务器，查看 /usr/local/openresty/nginx/logs/fts.access.log
![2026-01-15_145341.png](pic20260115/2026-01-15_145341.png)
确认发送时间和其他参数符合实际情况
![2026-01-15_145208.png](pic20260115/2026-01-15_145208.png)

```shell
55 Security package(s) need update.
No Bugfix package(s) need update.
No Enhancement package(s) need update.
No Newpackage package(s) need update.
73 Other package(s) need update.
Run "osmt update -s --security" or "osmt update -s --all" to show more.
Last login: Mon Jan 12 15:34:17 2026 from 10.42.160.125
[root@kweshdsita01067 ~]# cd /usr/local/openresty/nginx/logs/
[root@kweshdsita01067 logs]# ll
total 16
-rw-r--r-- 1 umpadmin root      0 Jan 15 01:00 access.log
-rw-r--r-- 1 umpadmin root    485 Jan 15 14:21 error.log
-rw-r--r-- 1 umpadmin root    389 Jan 15 14:21 fts.access.log
drwxr-xr-x 2 umpadmin umpgrp 4096 Jan 15 01:00 history_log
-rw-r--r-- 1 root     root      7 Jan  9 14:12 nginx.pid
[root@kweshdsita01067 logs]# cat access.log 
[root@kweshdsita01067 logs]# cat fts.access.log 
{"@timestamp":"2026-01-15T14:21:41+08:00","host":"10.42.129.50","client":"10.42.160.125","appid":"b995709d9d0343b2830ba09dbc317f32","folderName":"-","url":"/file/20260115028ee73e7c88178a08472896f6b2d8a8ab06024ce0b1551696a7cdbfdaef7fc157","request_method":"GET","request_length":439,"status":"200","forwarded_for":"-","node_id":"01","region":"EDC","user_agent":"MQS/2.5.9) Java/1.8.0_471"}

```

登录另一台FTS服务器发现服务器保存的消息内容和发送的消息内容一致,实际大小一致

![2026-01-15_150604.png](pic20260115/2026-01-15_150604.png)

![2026-01-15_150733.png](pic20260115/2026-01-15_150733.png)

```shell
[root@kweshdsita01068 e7]# pwd
/data01/mqs/files/2026/01/15/8e/e7
[root@kweshdsita01068 e7]# ll
total 7020
-rw-rw-rw- 1 umpadmin umpgrp 7185936 Jan 15 14:20 8ee73e7c88178a08472896f6b2d8a8ab06024ce0b1551696a7cdbfdaef7fc157
[root@kweshdsita01068 e7]# ll -h
total 6.9M
-rw-rw-rw- 1 umpadmin umpgrp 6.9M Jan 15 14:20 8ee73e7c88178a08472896f6b2d8a8ab06024ce0b1551696a7cdbfdaef7fc157
```
经验证，FTS部署成功，能正常响应用户发送大消息的请求。
