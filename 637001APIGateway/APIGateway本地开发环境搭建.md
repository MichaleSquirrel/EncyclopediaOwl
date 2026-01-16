# APIGateway本地开发环境搭建
## 2.搭建APIG本地开发环境

### 2.1 发现APIG已升级到JDK21


JDK 8 升级到 JDK 21
!3923胡镇华 30033331 创建于 2025-12-05 16:06:52
person_h30033331
至
develop
+3078-2069方雄杰 00800585 合并于 2025-12-10 18:06:12

### 2.2 已运行APIG

包括 apigw-admin

apigw-portal

需要的材料

根秘钥组件
[config](../APIGateway/config)

根秘钥组件解读

配置文件yml
[APIConfigFile](../APIGateway/APIConfigFile)

### 2.3写一遍根秘钥解读的wiki

### 2.4运行APIG 前端代码

```text
PS D:\750000APIGateway\apigw\ui\admin> npm run start
npm : 无法将“npm”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正确，然后再试一次。
所在位置 行:1 字符: 1
+ npm run start
+ ~~~
    + CategoryInfo          : ObjectNotFound: (npm:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS D:\750000APIGateway\apigw\ui\admin> cmd
Microsoft Windows [版本 10.0.26100.3476]
(c) Microsoft Corporation。保留所有权利。

D:\750000APIGateway\apigw\ui\admin>npm run start
'npm' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

D:\750000APIGateway\apigw\ui\admin>
```

![2025-12-15_100750.png](pic20251215/2025-12-15_100750.png)

npm 未安装

### 2.5 npm 安装

写一遍npm安装的wiki

要安装 npm，通常是直接安装 Node.js 官网 官方安装包，因为 npm 随 Node.js 一起安装；安装后通过在终端运行 node -v 和 npm -v 命令验证是否成功；然后根据需求（本地或全局）使用 npm install <包名> 或 npm install -g <包名> 来安装项目包。对于更灵活的版本管理，推荐使用 NVM。

https://nodejs.org/en/download

![2025-12-15_101646.png](pic20251215/2025-12-15_101646.png)


```text
PS D:\750000APIGateway\apigw\ui\admin> npm run start
npm : 无法加载文件 C:\Program Files\nodejs\npm.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 1
+ npm run start
+ ~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS D:\750000APIGateway\apigw\ui\admin> cmd
Microsoft Windows [版本 10.0.26100.3476]
(c) Microsoft Corporation。保留所有权利。

D:\750000APIGateway\apigw\ui\admin>
D:\750000APIGateway\apigw\ui\admin>npm run start
Debugger attached.

> start
> npm run dev:roma

Debugger attached.

> dev:roma
> cross-env DEPLOY_ENV=roma HIC_VERSION=sit webpack serve -c webpack/config.dev.js

'cross-env' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
Waiting for the debugger to disconnect...
Waiting for the debugger to disconnect...

D:\750000APIGateway\apigw\ui\admin>npm install
Debugger attached.

added 800 packages in 8s

94 packages are looking for funding
  run `npm fund` for details
Waiting for the debugger to disconnect...

D:\750000APIGateway\apigw\ui\admin>npm run start
Debugger attached.

> start
> npm run dev:roma

Debugger attached.

> dev:roma
> cross-env DEPLOY_ENV=roma HIC_VERSION=sit webpack serve -c webpack/config.dev.js

Debugger attached.
Debugger attached.
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
(node:28876) [DEP_WEBPACK_DEV_SERVER_HTTPS] DeprecationWarning: 'https' option is deprecated. Please use the 'server' option.
(Use `node --trace-deprecation ...` to show where the warning was created)
<i> [webpack-dev-server] Generating SSL certificate...
<i> [webpack-dev-server] SSL certificate: D:\750000APIGateway\apigw\ui\admin\node_modules\.cache\webpack-dev-server\server.pem
<i> [webpack-dev-server] [HPM] Proxy created: /apigw_admin  -> http://localhost:9098
<i> [webpack-dev-server] [HPM] Proxy created: /roma-web-common  -> http://eip-dev.huawei.com
<i> [webpack-dev-server] [HPM] Proxy created: /roma  -> https://console.his-op-beta.huawei.com/
<i> [webpack-dev-server] [HPM] Proxy rewrite rule created: "^" ~> ""
<i> [webpack-dev-server] [HPM] Proxy created: /gw/iam  -> https://console.his-op-beta.huawei.com/
<i> [webpack-dev-server] [HPM] Proxy rewrite rule created: "^" ~> ""
<i> [webpack-dev-server] [HPM] Proxy created: /epstenant  -> https://console.his-op-beta.huawei.com/
<i> [webpack-dev-server] [HPM] Proxy rewrite rule created: "^" ~> ""
<i> [webpack-dev-server] [HPM] Proxy created: /hicweb  -> https://console.his-op-beta.huawei.com/
<i> [webpack-dev-server] [HPM] Proxy rewrite rule created: "^" ~> ""
<i> [webpack-dev-server] Project is running at:
<i> [webpack-dev-server] Project is running at:
<i> [webpack-dev-server] Loopback: https://localhost:9091/
<i> [webpack-dev-server] Project is running at:
<i> [webpack-dev-server] Loopback: https://localhost:9091/
<i> [webpack-dev-server] On Your Network (IPv4): https://10.65.13.62:9091/
<i> [webpack-dev-server] Content not from webpack is served from 'D:\750000APIGateway\apigw\ui\admin\public' directory
assets by path assets/images/ 8.46 MiB 134 assets
assets by path assets/js/*.js 52 MiB
  assets by chunk 14.5 MiB (id hint: vendors) 9 assets
  + 40 assets
assets by path assets/login/ 1010 KiB 12 assets
assets by path assets/style/*.css 20.6 KiB
  asset assets/style/roma_menu.css 19.9 KiB [emitted] [from: public/assets/style/roma_menu.css] [copied]
  asset assets/style/hic_main.css 688 bytes [emitted] [from: public/assets/style/hic_main.css] [copied]
assets by path assets/template/*.xlsx 17.4 KiB
  asset assets/template/dict_import_template_zh.xlsx 8.7 KiB [emitted] [from: public/assets/template/dict_import_template_zh.xlsx] [copied]
  asset assets/template/dict_import_template_en.xlsx 8.69 KiB [emitted] [from: public/assets/template/dict_import_template_en.xlsx] [copied]
assets by path *.html 9.87 KiB
  asset login.html 8.67 KiB [emitted]
  asset index.html 1.2 KiB [emitted]
asset assets/bootstrap/css/bootstrap.min.css 138 KiB [emitted] [from: public/assets/bootstrap/css/bootstrap.min.css] [copied]
runtime modules 63.4 KiB 31 modules
orphan modules 34.7 KiB [orphan] 18 modules
modules by path ./node_modules/ 14.4 MiB
  javascript modules 14.4 MiB 4264 modules
  json modules 25.8 KiB 2 modules
modules by path ./src/ 1.08 MiB
  javascript modules 900 KiB 107 modules
  json modules 205 KiB 4 modules
asset modules 7.28 KiB
  ./public/assets/images/require.svg 3.34 KiB [built] [code generated]
  ./public/assets/images/require_hover.svg 3.34 KiB [built] [code generated]
  ./public/assets/images/nav_btn.png 620 bytes [built] [code generated]
./locale-data/complete.js (ignored) 15 bytes [built] [code generated]
webpack 5.89.0 compiled successfully in 6027 ms
```
1. 直接安装 Node.js 官网 官方安装包
2. npm install
3. npm run start
4. open  https://localhost.huawei.com:9091/
5. 用户名admin  密码 admin123

![2025-12-15_103322.png](pic20251215/2025-12-15_103322.png)

![2025-12-15_103437.png](pic20251215/2025-12-15_103437.png)


![2025-12-15_103935.png](pic20251215/2025-12-15_103935.png)

```text
加载失败的资源列表

由于网络原因，此页面部分资源加载失败。这些问题可能是由您的网络、代理服务器或网站本身引起的。

这些问题并非由 ZeroOmega 自身导致，它只不过检测并报告了错误而已。

*.huawei.com
在使用自动切换情景时，才可以将这些资源添加为切换条件。

取消

设置网络检测选项
```

## 2.6	开发环境数据库
7.197.145.201:8335/apigw
密码admin@apigw

![2025-12-15_110605.png](pic20251215/2025-12-15_110605.png)