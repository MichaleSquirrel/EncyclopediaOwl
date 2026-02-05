Saturday January 31 Day 031 week 5 of 2026

## 1.TodoList
1. 购买酒精
2. 去医院或社康看看皮肤科，手指左手食指和右手中指有皮肤藓
3.

## 2.

/authorization/services/jalor/security/user/tryFindOrCreateUser/w3Account/autoCreateUser


![2026-01-31_093027.png](pic20260131/2026-01-31_093027.png)


	10.41.0.118


在op侧登录apigw-portal的服务器抓包，看返回的数据

## 3.使用tcpdump命令拦截网络请求，并使用wireshark查看来解决问题
### 3.1 tcpdump命令

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


https://blog.csdn.net/sunrj_niu/article/details/129538418


### 3.2

/apigw_portals/data/api/test

bb351554bfc64e818bb1b291efde37f1

![2026-01-31_105805.png](pic20260131/2026-01-31_105805.png)


wireshark 过滤 特定请求路径


http.request.uri=="/apigw_portals/data/api/test"


![2026-01-31_111058.png](pic20260131/2026-01-31_111058.png)


kweshcsitd00245	服务器侧通用区(中密)	服务器侧通用区(中密)	响应
status: 204, response_time: 108, ref: e1b070919cef4e0b906732235bb39218
2026-01-31 10:50:15:107




kweshcsitd00245
apig-yw-runtime-g1
Huawei Cloud EulerOS 2.0
v8%LcxRTm7!i

西南-贵阳一
可用区四
10.41.0.247

### 3.3



kweshcsitd00245


kweshcsitd00245

access.log:10.41.1.249 - bb351554bfc64e818bb1b291efde37f1 [2026-01-31T10:50:15+08:00] "POST /api/fdngateway/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/w3Account/autoCreateUser HTTP/1.1" 204 0 "ApiGateway Java SDK 1.1.0" "317de9611d5d40b189a53158daa9579c" "e1b070919cef4e0b906732235bb39218"


服务器文件  传到堡垒机

![2026-01-31_150002.png](pic20260131/2026-01-31_150002.png)
> HTTP状态码：204 No Content（总结HTTP状态码）
> https://blog.csdn.net/u011047968/article/details/106120470



/saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/${w3Account}/${autoCreateUser}


http.request.uri=="/saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/${w3Account}/${autoCreateUser}"


```shell
tcp.stream eq 1050
```


97b974802c304b6b8c2307722c83bb46

![2026-01-31_151220.png](pic20260131/2026-01-31_151220.png)


![2026-01-31_151330.png](pic20260131/2026-01-31_151330.png)

都在246


## 3.7 异常响应

bb351554bfc64e818bb1b291efde37f1	10.41.1.249	2026-01-31 14:45:25.192	服务器侧通用区(中密)	apig-beta.yinwang.com	HTTPS	POST	/fdngateway/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/w3Account/autoCreateUser	204	129 ms	详情

![2026-01-31_152605.png](pic20260131/2026-01-31_152605.png)

![2026-01-31_152622.png](pic20260131/2026-01-31_152622.png)

```shell
tcp.stream eq 1050
```

![2026-01-31_152951.png](pic20260131/2026-01-31_152951.png)

![2026-01-31_153248.png](pic20260131/2026-01-31_153248.png)


## 3.8 正常响应


http.request.uri contains "/saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser"

![2026-01-31_154740.png](pic20260131/2026-01-31_154740.png)

![2026-01-31_161602.png](pic20260131/2026-01-31_161602.png)


## 3.9数据比对

```shell
POST /saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/${w3Account}/${autoCreateUser}?userAccount=l60072044 HTTP/1.1
Host: liveflow.ywit-beta.yinwang.com:9090
Connection: close
Content-Length: 0
proxy_scheme: https
User-Agent: ApiGateway Java SDK 1.1.0
X-GW-TENANT-ID: 8c8b823898bae7f80198bb20e3590002
Content-Type: application/json; charset=UTF-8
Accept-Encoding: gzip,deflate
x-microzerotrust-id: xdefend
LF_CALLER_APPID: 97b974802c304b6b8c2307722c83bb46
LF_TRACE_ID: fb6cf71978e94a9bb9df20944e6f7d77
ruleChainId: 17743790-8dc9-11ef-add9-693c922e36ba
x-jwt-gw-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJlbXBUeXBlIjoiYXBwbGljYXRpb24iLCJhcHBJZCI6Ijk3Yjk3NDgwMmMzMDRiNmI4YzIzMDc3MjJjODNiYjQ2IiwiYXVkIjoiZTFiMDcwOTE5Y2VmNGUwYjkwNjczMjIzNWJiMzkyMTgiLCJleHAiOjE3Njk4NDIyMzQsImlzcyI6ImdhdGV3YXkiLCJ1aWQiOiI5N2I5NzQ4MDJjMzA0YjZiOGMyMzA3NzIyYzgzYmI0NiIsInV1aWQiOiI5N2I5NzQ4MDJjMzA0YjZiOGMyMzA3NzIyYzgzYmI0NiIsImF1eiI6InRydWUiLCJuaWNrTmFtZSI6InNnb3YifQ.4bPxiDLgkEKLktN_jYxWgifivSinj0hPz68JTVYWmXAFptNq2BebzEOdcd0EYbNDq2J1N3owZFbi3T3RtE-vcw
elb_redirect_host_mgmt: mit-base-mgmt.ccs-common-ywbeta.beta.yinwang.com
elb_redirect_host_query: mit-base-query.ccs-common-ywbeta.beta.yinwang.com
envalias: default
elb_redirect_host_cx: mit-base-cx.ccs-common-ywbeta.beta.yinwang.com
elb_redirect_host_csp: csp-data-m.ccs-common-ywbeta.beta.yinwang.com
x-meta-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJjdHgiOnsicmVudGVySWQiOjIyMDAwMDA0LCJyZW50ZXJDbGFzcyI6ImRlZmF1bHQiLCJhcHBJZCI6ImUxYjA3MDkxOWNlZjRlMGI5MDY3MzIyMzViYjM5MjE4In0sImV4dCI6eyJhcHBJZCI6ImUxYjA3MDkxOWNlZjRlMGI5MDY3MzIyMzViYjM5MjE4In19.ZCBGsqALWF74pWUYlEsuaqpNqDLGZ9XJuIYjd99HxUIKGN7Wv8b80OG/Nozlt7RGhbduFKMS92+12E3bsGwKPg
Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJvcF9oc2EiLCJhY2NvdW50X3R5cGUiOiJJQU1fU0VSVklDRSIsIm5iZiI6MTc2OTc1Mzg0NSwiYWNjb3VudF9pZCI6IjhjOGI4MTBhOThlMDBkMmIwMTk4ZjllYzc0ZTkwMWQ1IiwiZW50ZXJwcmlzZSI6IjhjOGI4MjM4OThiYWU3ZjgwMTk4YmIyMGUzNTkwMDAyIiwiaXNzIjoiaWFtIiwibmFtZSI6Im9wX2hzYSIsInByb2plY3QiOiJlMWIwNzA5MTljZWY0ZTBiOTA2NzMyMjM1YmIzOTIxOCIsImV4cCI6MTc2OTkyNjY0NSwiaWF0IjoxNzY5ODQwMjQ1LCJqdGkiOiI3MjUxZjFkYS1iNTk0LTQ1YjItODk2OC01ODcxZTZkNzJhZGIifQ.Z-ku9H77a8Q50B4NKwzHnaYLTkrpkszN25w3zSLk19AxONfTQLO-ARwRDIlQ_XLx-gXqzcvwd0zYmeUE9eSTHhG2Qry3jLicvn8mgSBiD_lCmRJdFtqvHCDj4Z-Iu7jg36hgqO49WGIh5uVM-Ph67s92wokZxmNXYIy4woKXL-Irq5Cuk3_F6eDRN7_jScLNn-5f8TBeA4_ntaeGKe5NIFfLuK7BP0FqyEYW3fmNDQbRaFtMcMcVykhWRW2AaaqUWivfaHDbzpAS9KS-5XdOWZoBplQPLg4HVJ4QC8gil5uymU6dZ7l4MytkmX4_q0oJ7AyrGox6BWCEu1F83WiQXg
x-renter-id: 22000004
env: kwepro
fdn-Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJvcF9oc2EiLCJhY2NvdW50X3R5cGUiOiJJQU1fU0VSVklDRSIsIm5iZiI6MTc2OTc1Mzg0NSwiYWNjb3VudF9pZCI6IjhjOGI4MTBhOThlMDBkMmIwMTk4ZjllYzc0ZTkwMWQ1IiwiZW50ZXJwcmlzZSI6IjhjOGI4MjM4OThiYWU3ZjgwMTk4YmIyMGUzNTkwMDAyIiwiaXNzIjoiaWFtIiwibmFtZSI6Im9wX2hzYSIsInByb2plY3QiOiJlMWIwNzA5MTljZWY0ZTBiOTA2NzMyMjM1YmIzOTIxOCIsImV4cCI6MTc2OTkyNjY0NSwiaWF0IjoxNzY5ODQwMjQ1LCJqdGkiOiI3MjUxZjFkYS1iNTk0LTQ1YjItODk2OC01ODcxZTZkNzJhZGIifQ.Z-ku9H77a8Q50B4NKwzHnaYLTkrpkszN25w3zSLk19AxONfTQLO-ARwRDIlQ_XLx-gXqzcvwd0zYmeUE9eSTHhG2Qry3jLicvn8mgSBiD_lCmRJdFtqvHCDj4Z-Iu7jg36hgqO49WGIh5uVM-Ph67s92wokZxmNXYIy4woKXL-Irq5Cuk3_F6eDRN7_jScLNn-5f8TBeA4_ntaeGKe5NIFfLuK7BP0FqyEYW3fmNDQbRaFtMcMcVykhWRW2AaaqUWivfaHDbzpAS9KS-5XdOWZoBplQPLg4HVJ4QC8gil5uymU6dZ7l4MytkmX4_q0oJ7AyrGox6BWCEu1F83WiQXg


HTTP/1.1 200 OK
route_path: liveflow
Content-Type: application/json
transactionId: 1f0fe7071da4e908d44a111f5656897
content-length: 830

{"appNames":null,"endDate":null,"lastUpdateDate":null,"globalUserId":"139038346627896","consumerSubappId":null,"uuid":"11139038346627640","employeeNumber":"60072044","defaultOrg":null,"employeeNameEng":null,"currentProgramIds":null,"lastUpdateUserCN":null,"apartmentCode":null,"rowIdx":null,"currentRole":null,"lang":null,"userCN":"lusheng 60072044","email":"lusheng@beta.yinwang.com","creationUserCN":null,"fname":null,"defaultRole":null,"maskedUserAccount":"l60*044","dept":null,"programValidity":null,"creationDate":null,"userId":"139038346627896","currentPrograms":null,"validRoles":null,"areaCode":null,"createdBy":null,"userAccount":"l60072044","displayNameCn":null,"tenantId":null,"displayNameEn":null,"msaAppId":null,"userType":"HWE","scopes":null,"currentOrg":null,"lowerW3Account":"l60072044","coalitionPermission":null}
```


```shell
POST /saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/${w3Account}/${autoCreateUser} HTTP/1.1
Host: liveflow.ywit-beta.yinwang.com:9090
Connection: close
Content-Length: 0
proxy_scheme: https
User-Agent: ApiGateway Java SDK 1.1.0
X-GW-TENANT-ID: 8c8b823898bae7f80198bb20e3590002
Content-Type: application/json; charset=UTF-8
Accept-Encoding: gzip,deflate
x-microzerotrust-id: xdefend
LF_CALLER_APPID: bb351554bfc64e818bb1b291efde37f1
LF_TRACE_ID: 608510f740024bef83596ae9d681174a
ruleChainId: 17743790-8dc9-11ef-add9-693c922e36ba
x-jwt-gw-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJlbXBUeXBlIjoiYXBwbGljYXRpb24iLCJhcHBJZCI6ImJiMzUxNTU0YmZjNjRlODE4YmIxYjI5MWVmZGUzN2YxIiwiYXVkIjoiZTFiMDcwOTE5Y2VmNGUwYjkwNjczMjIzNWJiMzkyMTgiLCJleHAiOjE3Njk4NDIyMjUsImlzcyI6ImdhdGV3YXkiLCJ1aWQiOiJiYjM1MTU1NGJmYzY0ZTgxOGJiMWIyOTFlZmRlMzdmMSIsInV1aWQiOiJiYjM1MTU1NGJmYzY0ZTgxOGJiMWIyOTFlZmRlMzdmMSIsImF1eiI6InRydWUiLCJuaWNrTmFtZSI6InNnb3YifQ._R-iUxJWVXqULP2snUViuEiILMi-CiLgJA4IExqQMWaGyKpBLppCrq_TGR2KxpNlfIaWxycGlnNVA4V1eaWxOw
elb_redirect_host_query: mit-base-query.ccs-common-ywbeta.beta.yinwang.com
envalias: default
x-meta-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJjdHgiOnsicmVudGVySWQiOjIyMDAwMDA0LCJyZW50ZXJDbGFzcyI6ImRlZmF1bHQiLCJhcHBJZCI6ImUxYjA3MDkxOWNlZjRlMGI5MDY3MzIyMzViYjM5MjE4In0sImV4dCI6eyJhcHBJZCI6ImUxYjA3MDkxOWNlZjRlMGI5MDY3MzIyMzViYjM5MjE4In19.ZCBGsqALWF74pWUYlEsuaqpNqDLGZ9XJuIYjd99HxUIKGN7Wv8b80OG/Nozlt7RGhbduFKMS92+12E3bsGwKPg
elb_redirect_host_cx: mit-base-cx.ccs-common-ywbeta.beta.yinwang.com
Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJvcF9oc2EiLCJhY2NvdW50X3R5cGUiOiJJQU1fU0VSVklDRSIsIm5iZiI6MTc2OTc1Mzg0NSwiYWNjb3VudF9pZCI6IjhjOGI4MTBhOThlMDBkMmIwMTk4ZjllYzc0ZTkwMWQ1IiwiZW50ZXJwcmlzZSI6IjhjOGI4MjM4OThiYWU3ZjgwMTk4YmIyMGUzNTkwMDAyIiwiaXNzIjoiaWFtIiwibmFtZSI6Im9wX2hzYSIsInByb2plY3QiOiJlMWIwNzA5MTljZWY0ZTBiOTA2NzMyMjM1YmIzOTIxOCIsImV4cCI6MTc2OTkyNjY0NSwiaWF0IjoxNzY5ODQwMjQ1LCJqdGkiOiI3MjUxZjFkYS1iNTk0LTQ1YjItODk2OC01ODcxZTZkNzJhZGIifQ.Z-ku9H77a8Q50B4NKwzHnaYLTkrpkszN25w3zSLk19AxONfTQLO-ARwRDIlQ_XLx-gXqzcvwd0zYmeUE9eSTHhG2Qry3jLicvn8mgSBiD_lCmRJdFtqvHCDj4Z-Iu7jg36hgqO49WGIh5uVM-Ph67s92wokZxmNXYIy4woKXL-Irq5Cuk3_F6eDRN7_jScLNn-5f8TBeA4_ntaeGKe5NIFfLuK7BP0FqyEYW3fmNDQbRaFtMcMcVykhWRW2AaaqUWivfaHDbzpAS9KS-5XdOWZoBplQPLg4HVJ4QC8gil5uymU6dZ7l4MytkmX4_q0oJ7AyrGox6BWCEu1F83WiQXg
elb_redirect_host_csp: csp-data-m.ccs-common-ywbeta.beta.yinwang.com
elb_redirect_host_mgmt: mit-base-mgmt.ccs-common-ywbeta.beta.yinwang.com
x-renter-id: 22000004
env: kwepro
fdn-Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOiJvcF9oc2EiLCJhY2NvdW50X3R5cGUiOiJJQU1fU0VSVklDRSIsIm5iZiI6MTc2OTc1Mzg0NSwiYWNjb3VudF9pZCI6IjhjOGI4MTBhOThlMDBkMmIwMTk4ZjllYzc0ZTkwMWQ1IiwiZW50ZXJwcmlzZSI6IjhjOGI4MjM4OThiYWU3ZjgwMTk4YmIyMGUzNTkwMDAyIiwiaXNzIjoiaWFtIiwibmFtZSI6Im9wX2hzYSIsInByb2plY3QiOiJlMWIwNzA5MTljZWY0ZTBiOTA2NzMyMjM1YmIzOTIxOCIsImV4cCI6MTc2OTkyNjY0NSwiaWF0IjoxNzY5ODQwMjQ1LCJqdGkiOiI3MjUxZjFkYS1iNTk0LTQ1YjItODk2OC01ODcxZTZkNzJhZGIifQ.Z-ku9H77a8Q50B4NKwzHnaYLTkrpkszN25w3zSLk19AxONfTQLO-ARwRDIlQ_XLx-gXqzcvwd0zYmeUE9eSTHhG2Qry3jLicvn8mgSBiD_lCmRJdFtqvHCDj4Z-Iu7jg36hgqO49WGIh5uVM-Ph67s92wokZxmNXYIy4woKXL-Irq5Cuk3_F6eDRN7_jScLNn-5f8TBeA4_ntaeGKe5NIFfLuK7BP0FqyEYW3fmNDQbRaFtMcMcVykhWRW2AaaqUWivfaHDbzpAS9KS-5XdOWZoBplQPLg4HVJ4QC8gil5uymU6dZ7l4MytkmX4_q0oJ7AyrGox6BWCEu1F83WiQXg


HTTP/1.1 204 No Content
route-path: liveflow
Content-Type: application/json
transactionId: 1f0fe706c06e9b08d44a111f5656897
```

![2026-01-31_163029.png](pic20260131/2026-01-31_163029.png)

对比之后发现，LF_CALLER_APPID和x-jwt-gw-token不一样

204 的 LF_CALLER_APPID: bb351554bfc64e818bb1b291efde37f1

x-jwt-gw-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJlbXBUeXBlIjoiYXBwbGljYXRpb24iLCJhcHBJZCI6ImJiMzUxNTU0YmZjNjRlODE4YmIxYjI5MWVmZGUzN2YxIiwiYXVkIjoiZTFiMDcwOTE5Y2VmNGUwYjkwNjczMjIzNWJiMzkyMTgiLCJleHAiOjE3Njk4NDIyMjUsImlzcyI6ImdhdGV3YXkiLCJ1aWQiOiJiYjM1MTU1NGJmYzY0ZTgxOGJiMWIyOTFlZmRlMzdmMSIsInV1aWQiOiJiYjM1MTU1NGJmYzY0ZTgxOGJiMWIyOTFlZmRlMzdmMSIsImF1eiI6InRydWUiLCJuaWNrTmFtZSI6InNnb3YifQ._R-iUxJWVXqULP2snUViuEiILMi-CiLgJA4IExqQMWaGyKpBLppCrq_TGR2KxpNlfIaWxycGlnNVA4V1eaWxOw

![2026-01-31_163741.png](pic20260131/2026-01-31_163741.png)

```shell
{
  "typ": "JWT",
  "alg": "HS512"
}

{
  "empType": "application",
  "appId": "bb351554bfc64e818bb1b291efde37f1",
  "aud": "e1b070919cef4e0b906732235bb39218",
  "exp": 1769842225,
  "iss": "gateway",
  "uid": "bb351554bfc64e818bb1b291efde37f1",
  "uuid": "bb351554bfc64e818bb1b291efde37f1",
  "auz": "true",
  "nickName": "sgov"
}
```



> JWT解码 | JWT Decoder
> https://jwt.box3.cn/

200 的 LF_CALLER_APPID: 97b974802c304b6b8c2307722c83bb46

x-jwt-gw-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJlbXBUeXBlIjoiYXBwbGljYXRpb24iLCJhcHBJZCI6Ijk3Yjk3NDgwMmMzMDRiNmI4YzIzMDc3MjJjODNiYjQ2IiwiYXVkIjoiZTFiMDcwOTE5Y2VmNGUwYjkwNjczMjIzNWJiMzkyMTgiLCJleHAiOjE3Njk4NDIyMzQsImlzcyI6ImdhdGV3YXkiLCJ1aWQiOiI5N2I5NzQ4MDJjMzA0YjZiOGMyMzA3NzIyYzgzYmI0NiIsInV1aWQiOiI5N2I5NzQ4MDJjMzA0YjZiOGMyMzA3NzIyYzgzYmI0NiIsImF1eiI6InRydWUiLCJuaWNrTmFtZSI6InNnb3YifQ.4bPxiDLgkEKLktN_jYxWgifivSinj0hPz68JTVYWmXAFptNq2BebzEOdcd0EYbNDq2J1N3owZFbi3T3RtE-vcw

![2026-01-31_163959.png](pic20260131/2026-01-31_163959.png)

```shell


{
"typ": "JWT",
"alg": "HS512"
}


{
"empType": "application",
"appId": "97b974802c304b6b8c2307722c83bb46",
"aud": "e1b070919cef4e0b906732235bb39218",
"exp": 1769842234,
"iss": "gateway",
"uid": "97b974802c304b6b8c2307722c83bb46",
"uuid": "97b974802c304b6b8c2307722c83bb46",
"auz": "true",
"nickName": "sgov"
}
```

```shell


{
  "empType": "application",
  "appId": "bb351554bfc64e818bb1b291efde37f1",
  "aud": "e1b070919cef4e0b906732235bb39218",
  "exp": 1769842225,
  "iss": "gateway",
  "uid": "bb351554bfc64e818bb1b291efde37f1",
  "uuid": "bb351554bfc64e818bb1b291efde37f1",
  "auz": "true",
  "nickName": "sgov"
}

{
  "empType": "application",
  "appId": "97b974802c304b6b8c2307722c83bb46",
  "aud": "e1b070919cef4e0b906732235bb39218",
  "exp": 1769842234,
  "iss": "gateway",
  "uid": "97b974802c304b6b8c2307722c83bb46",
  "uuid": "97b974802c304b6b8c2307722c83bb46",
  "auz": "true",
  "nickName": "sgov"
}
```

经过比对，不一样的只有appId和exp时间戳

### 3.10 去LiveFlow查看原因

POST /saliveflow/base/mfup/authorization/services/jalor/security/user/tryFindOrCreateUser/${w3Account}/${autoCreateUser} HTTP/1.1

没找到对应的流程，等周一再解决

## 4.解决1月29号的问题
[Video_2026-01-29_151635.wmv](../../VideoRecoder/Video_2026-01-29_151635.wmv)

[Video_2026-01-29_174116.wmv](../../VideoRecoder/Video_2026-01-29_174116.wmv)、

姚沙 30021089

/gateway/iscp/hios/services/file/download

![2026-01-31_170644.png](pic20260131/2026-01-31_170644.png)

527d4b14f2434c5ab652e562b8abec9f


tcpdump -vv -i any -w analyzer5.cap

http.request.uri contains "/file/download"
## 5.问题已解决

叶惠 60073988

![CB629AB0-BCE3-488A-EDE8-8FF205116A23.gif](pic20260131/CB629AB0-BCE3-488A-EDE8-8FF205116A23.gif)

规则代码已经存在

[Video_2026-01-31_161318.wmv](../../VideoRecoder/Video_2026-01-31_161318.wmv)


## 6.在服务器抓包并在办公电脑查看全流程记录


## 7.