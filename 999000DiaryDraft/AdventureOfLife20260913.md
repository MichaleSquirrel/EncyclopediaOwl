Sunday September 13 Day 256 week 38 of 2026

## 1.TodoList




## 2.MCA课程学习进度

2026年09月13号学习进展：
1. 复习
2. 阅读
   大概用时：小时


## 3.
【浙江新华】尊敬的用户，您的图书订单已发货，快递单号：ZTO:79032352765608，可登录平台查询。客服热线：400-8056-785，祝您生活愉快！


https://www.zto.com/



## 4.


我在本地搭建了一个局域网，其中192.168.165.40跑了SpringAISseMcpServer
192.168.165.71跑了SpringAISseMcpClient，当我在192.168.165.71上用浏览器访问http://localhost:8080/ai/chat?message=北京天气如何?
，然后出现如上报错


本地windows电脑和macOS连接同一个手机wifi搭建一个局域网，如何实现两台机器互相访问？如何能ping通


mac 无法局域网内 Ping 通 Windows 主机 IP 的解决方法


Pinging 192.168.165.40 with 32 bytes of data:
Request timed out.
Reply from 192.168.165.71: Destination host unreachable.
Reply from 192.168.165.71: Destination host unreachable.
Reply from 192.168.165.71: Destination host unreachable.


## 5.

查询员工信息的一个MCP：

https://api.openweathermap.org/data/2.5/weather?lat=22.54&lon=114.06&appid=363a215938d32a5d738ea78504954fa9
{"coord":{"lon":114.06,"lat":22.54},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"base":"stations","main":{"temp":302.18,"feels_like":309.18,"temp_min":300.64,"temp_max":302.56,"pressure":1015,"humidity":86,"sea_level":1015,"grnd_level":1006},"visibility":10000,"wind":{"speed":0.9,"deg":58,"gust":1.5},"clouds":{"all":11},"dt":1789346189,"sys":{"type":2,"id":2031340,"country":"CN","sunrise":1789337408,"sunset":1789381751},"timezone":28800,"id":7001297,"name":"Gangxia","cod":200}

http://api.openweathermap.org/data/2.5/weather?q=Beijing&appid=363a215938d32a5d738ea78504954fa9&units=metric&lang=zh_cn

{"coord":{"lon":116.3972,"lat":39.9075},"weather":[{"id":800,"main":"Clear","description":"晴","icon":"01d"}],"base":"stations","main":{"temp":20.94,"feels_like":19.95,"temp_min":20.94,"temp_max":20.94,"pressure":1025,"humidity":33,"sea_level":1025,"grnd_level":1020},"visibility":10000,"wind":{"speed":1.82,"deg":32,"gust":2.5},"clouds":{"all":0},"dt":1789346178,"sys":{"type":1,"id":9609,"country":"CN","sunrise":1789336441,"sunset":1789381597},"timezone":28800,"id":1816670,"name":"Beijing","cod":200}


http://localhost:8999/ai/chat?message=北京天气如何?

