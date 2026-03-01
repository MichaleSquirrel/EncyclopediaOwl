Friday February 27 Day 058 week 9 of 2026

## 1.TodoList



## 2.


https://10.210.19.175/mqs
https://10.210.19.130/mqs



aes.key


[root@mqs-web00-fromxac classes]# pwd
/data01/ump/mqs-prod/tomcat-mqs-web/webapps/mqs/WEB-INF/classes



```shell
user=umpadmin
group=umpgrp

egrep "^$group" /etc/group >& /dev/null
if [ $? -ne 0 ]
then
  groupadd -g 550 $group
  echo 'execute: groupadd -g 550 $group'  
else
  echo $group ' already exit nothing to do'
fi


egrep "^$user" /etc/passwd >& /dev/null
if [ $? -ne 0 ]; then
     useradd -u 551 -g $group -d /data01/ump -s /bin/bash $user 
     echo 'execute: useradd -u 551 -g $group -d /data01/ump -s /bin/bash $user'
	 echo $userPasswd | passwd --stdin $user  
	 passwd -x 99999 $user 
else
  echo $user ' already exit nothing to do'
fi
chown -R $user:$group /data01/ump
echo $user > /etc/cron.allow
```


./addUser.sh -userPasswd 1Xk9_CyjwP8Er63E


```shell
[root@mqs-web00-fromxac ump]# ll
total 20236
-rwxr-xr-x 1 umpadmin umpgrp 20716097 Aug  8  2025 encrypt_decrypt_random.jar
drwxr-xr-x 3 umpadmin umpgrp       60 Aug  8  2025 java
drwxr-xr-x 9 umpadmin umpgrp      109 Jan  5 14:55 logs
drwxr-xr-x 3 umpadmin umpgrp       19 Aug  8  2025 mqs
drwxr-xr-x 9 umpadmin umpgrp      203 Aug  8  2025 mqs-prod
drwxr-xr-x 3 umpadmin umpgrp       86 Sep 15 11:20 sdkTest
drwxr-xr-x 3 umpadmin umpgrp       86 Nov 14  2024 sdkTest-20250808143416
-rw-r--r-- 1 umpadmin umpgrp      166 Sep 15 12:11 sdkTest.zip
drwxr-xr-x 2 umpadmin umpgrp       77 Aug  8  2025 sql
drwxr-xr-x 2 umpadmin umpgrp       77 Aug  8  2025 sql-20250808143355
drwxr-x--- 2 umpadmin umpgrp        6 Aug  8  2025 uploadedfile
drwxr-xr-x 2 umpadmin umpgrp        6 Aug  8  2025 uploadTmpsk  
```



安装portal
```shell
INSTALL_DIR_WEB=/data01/ump/mqs-prod/tomcat-mqs-web

CRONTABJOB='* * * * * /bin/sh /data01/ump/mqs-prod/tomcat-mqs-web/bin/scan.sh >> /dev/null'
task_count_disable=$(crontab -l|grep "${CRONTABJOB}"|wc -l)
if [ $task_count_disable -ne 0 ];then
  crontab -l | grep -v "${CRONTABJOB}"| crontab -
  echo "Remove crontab task."
else
  echo "Crontab task is not exist."
fi

CRONTABJOB='* * * * * /bin/sh /data01/ump/mqs-prod/mqs-rest-api/tomcat-mqs-web/bin/scan.sh >> /dev/null'
task_count_disable=$(crontab -l|grep "${CRONTABJOB}"|wc -l)
if [ $task_count_disable -ne 0 ];then
  crontab -l | grep -v "${CRONTABJOB}"| crontab -
  echo "Remove crontab task."
else
  echo "Crontab task is not exist."
fi




INSTALL_DIR_WEB=/data01/ump/mqs-prod/tomcat-mqs-web
# 判断该机器是否已经有mqs-web在运行了
if [ -d "$INSTALL_DIR_WEB" ]; then
  MAIN_CLASS=Bootstrap
  pidlist=`ps -ef|grep "${MAIN_CLASS}"|grep -v "grep"|awk '{print $2}'`
  if [ ! "$pidlist" = "" ]; then
    kill -9 $pidlist
    echo "service stop success"
  fi
  randomVal=$(date +%Y%m%d%H%M%S)
  mv $INSTALL_DIR_WEB $INSTALL_DIR_WEB-$randomVal
fi

INSTALL_DIR_API=/data01/ump/mqs-prod/mqs-rest-api/tomcat-mqs-web
# 判断该机器是否已经有mqs-rest-api在运行了
if [ -d "$INSTALL_DIR_API" ]; then
  randomVal=$(date +%Y%m%d%H%M%S)
  mv $INSTALL_DIR_API $INSTALL_DIR_API-$randomVal
fi

if [ ! -d "/data01/ump/uploadTmp" ]; then
  mkdir -p /data01/ump/uploadTmp
fi

unzip /tmp/tomcat-mqs-web.zip -d /data01/ump/mqs-prod
cd /data01/ump/mqs-prod
chmod +x -R tomcat-mqs-web

applicationConfigFile=${INSTALL_DIR_WEB}/webapps/mqs/WEB-INF/classes/application.properties
# 修改application.properties配置文件
sed -i "/mqs.jdbc.url=/c\mqs.jdbc.url=$dbUrl" $applicationConfigFile
sed -i "/mqs.jdbc.username=/c\mqs.jdbc.username=$dbUser" $applicationConfigFile
sed -i "/mqs.jdbc.password=/c\mqs.jdbc.password=$encryptDbPass" $applicationConfigFile
sed -i "/els.url=/c\els.url=$es_url" $applicationConfigFile
sed -i "/monitor.redis.url=/c\monitor.redis.url=$singleRedisUrl" $applicationConfigFile
sed -i "/monitor.redis.password=/c\monitor.redis.password=$encryptRedisSecret" $applicationConfigFile
sed -i "/cache.redis.url=/c\cache.redis.url=$singleRedisUrl" $applicationConfigFile
sed -i "/cache.redis.password=/c\cache.redis.password=$encryptRedisSecret" $applicationConfigFile
sed -i "/mqs.proxy.address=/c\mqs.proxy.address=http://${apigwUrl}/api/mqs/proxy" $applicationConfigFile
sed -i "/mqs.proxy.appid=/c\mqs.proxy.appid=${ProjectId}" $applicationConfigFile
sed -i "/mqs.proxy.token=/c\mqs.proxy.token=${encryptApigwMqsToken}" $applicationConfigFile
sed -i "/mqs.proxy.es.address.uri=/c\mqs.proxy.es.address.uri=${apigwUrl}" $applicationConfigFile
sed -i "/prometheus.api.url=/c\prometheus.api.url=http://${prometheusIP}:8428/victoria-metrics/api/v1/" $applicationConfigFile
sed -i "/headerAddress.url=/c\headerAddress.url=${headerAddress}" $applicationConfigFile
sed -i "/jquery.url=/c\jquery.url=${jquery}" $applicationConfigFile
sed -i 's/\r$//' $applicationConfigFile

umiFile=${INSTALL_DIR_WEB}/webapps/mqs/umi.103d8c5d.js
sed -i "s#console.heds.huawei.com#${consoleUrl}#g" $umiFile

ssoAdapterConfigFile=${INSTALL_DIR_WEB}/webapps/mqs/WEB-INF/classes/sso-adapter.properties
sed -i "/sso.domain.white.list=/c\sso.domain.white.list=${consoleUrl:8}" $ssoAdapterConfigFile
sed -i "/sso.appid=/c\sso.appid=${ProjectId}" $ssoAdapterConfigFile
sed -i "/sso.url=/c\sso.url=https://iam.${consoleUrl:8}" $ssoAdapterConfigFile
sed -i "/sso.login.url=/c\sso.login.url=https://console.%s/epstenant/#/login" $ssoAdapterConfigFile
sed -i "/sso.mqs.opEnterprise=/c\sso.mqs.opEnterprise=$ENTERPRISE_ID" $ssoAdapterConfigFile
sed -i "/sso.mqs.opProject=/c\sso.mqs.opProject=$ProjectId" $ssoAdapterConfigFile
sed -i "/sso.mqs.opAccount=/c\sso.mqs.opAccount=$AccountName" $ssoAdapterConfigFile
sed -i "/sso.mqs.opSecret=/c\sso.mqs.opSecret=$encryptAccountSecret" $ssoAdapterConfigFile
sed -i "/enterprise=/c\enterprise=$ENTERPRISE_ID" $ssoAdapterConfigFile
sed -i "/project=/c\project=$ProjectId" $ssoAdapterConfigFile
sed -i "/iam.op.account=/c\iam.op.account=$AccountName" $ssoAdapterConfigFile
sed -i "/iam.op.secret=/c\iam.op.secret=$encryptAccountSecret" $ssoAdapterConfigFile
sed -i "/iam.endpoint=/c\iam.endpoint=https://iam.${consoleUrl:8}" $ssoAdapterConfigFile
sed -i 's/\r$//' $ssoAdapterConfigFile

# 去除概览页的华为相关信息
indexHtmlFile=${INSTALL_DIR_WEB}/webapps/mqs/index.html
styleRightPanel='<style>.right_panels___3s8Ae>.ant-row>.ant-col{height:0px;overflow:hidden;}</style>'
sed -i "s#head><body#head>$styleRightPanel<body#g" $indexHtmlFile

```

deployPortal.sh
-dbUrl jdbc:mysql://10.210.39.79:3306/mqs?useUnicode=true&characterEncoding=utf-8
-dbUser mqsAdmin
-encryptDbPass
-es_url 10.210.37.221:9200
-singleRedisUrl 10.210.38.120:6379
-encryptRedisSecret
-apigwUrl apig.ywit-op-beta.yinwang.com
-ProjectId 00000000000000000000000000000092
-encryptApigwMqsToken
-prometheusIP 10.210.34.123
-consoleUrl 10.210.2.245
-ENTERPRISE_ID 88888888888888888888888888888888
-AccountName 00000000000000000000000000000092
-encryptAccountSecret
-headerAddress 	/hicweb/common/hic4Console.js
-jquery /roma-web-iam/js/jquery.js

## 3.在VMWare上

```shell

[root@localhost ~]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:0c:29:1a:33:60 brd ff:ff:ff:ff:ff:ff
    inet 192.168.88.31/24 brd 192.168.88.255 scope global noprefixroute ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::5ddd:7c2e:3edd:fa7f/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
[root@localhost ~]#

```

```shell

C:\Users\m30026548>java -jar D:\760001MQS\mqs\MqsWeb\mqs-web\out\artifacts\EncryTest_jar\mqs-web.jar
Error: A JNI error has occurred, please check your installation and try again
Exception in thread "main" java.lang.SecurityException: Invalid signature file digest for Manifest main attributes
        at java.base/sun.security.util.SignatureFileVerifier.processImpl(SignatureFileVerifier.java:340)
        at java.base/sun.security.util.SignatureFileVerifier.process(SignatureFileVerifier.java:282)
        at java.base/java.util.jar.JarVerifier.processEntry(JarVerifier.java:323)
        at java.base/java.util.jar.JarVerifier.update(JarVerifier.java:235)
        at java.base/java.util.jar.JarFile.initializeVerifier(JarFile.java:761)
        at java.base/java.util.jar.JarFile.ensureInitialization(JarFile.java:1071)
        at java.base/java.util.jar.JavaUtilJarAccessImpl.ensureInitialization(JavaUtilJarAccessImpl.java:42)
        at java.base/jdk.internal.loader.URLClassPath$JarLoader$2.getManifest(URLClassPath.java:852)
        at java.base/jdk.internal.loader.BuiltinClassLoader.defineClass(BuiltinClassLoader.java:848)
        at java.base/jdk.internal.loader.BuiltinClassLoader.findClassOnClassPathOrNull(BuiltinClassLoader.java:760)
        at java.base/jdk.internal.loader.BuiltinClassLoader.loadClassOrNull(BuiltinClassLoader.java:681)
        at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:639)
        at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
        at java.base/java.lang.Class.forName0(Native Method)
        at java.base/java.lang.Class.forName(Class.java:536)
        at java.base/java.lang.Class.forName(Class.java:515)
        at java.base/sun.launcher.LauncherHelper.loadMainClass(LauncherHelper.java:818)
        at java.base/sun.launcher.LauncherHelper.checkAndLoadMain(LauncherHelper.java:713)
```



grep -rn "javax.crypto.AEADBadTagException: Tag mismatch" .
