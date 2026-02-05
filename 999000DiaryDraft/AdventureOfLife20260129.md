Thursday January 29 Day 029 week 5 of 2026

## 1.TodoList



```shell
local _M = {}

_M['nodes_ip'] = {
    ['01'] = '10.201.32.53',
    ['02'] = '10.201.32.169'
}

_M['sgov_auth_url'] = 'http://oauth2-op.yinwang.com/umws4login/services/Authentication'

_M['token_expire_seconds'] = 180

_M['his3_iam_auth_url'] = 'https://iam.ywit-op.yinwang.com/iam/auth/token'

_M['auth_white_list'] = {
'XXXXXXXXXXXXXXXXXXXXXX'
}


_M['nodes_ip'] = {
    ['01'] = '10.201.32.53',
    ['02'] = '10.201.32.169'
}

_M['sgov_auth_url'] = 'http://oauth2-op.yinwang.com/umws4login/services/Authentication'

_M['token_expire_seconds'] = 180

_M['his3_iam_auth_url'] = 'https://iam.ywit-op.yinwang.com/iam/auth/token'

_M['auth_white_list'] = {
'XXXXXXXXXXXXXXXXXXXXXX'
}

```



```text
CB.2110003.451 / fetch docker cluster 'cloudbuild_docker_4U8G_green_IT_01', image 'kwe-ecr-ywpro-x16ibw.swr-pro.myhuaweicloud.com/ecr-build/ias_ubuntu_jdk21_20260113:v1.1', group 'g9c0900a1c68f4a94a73f6588dd9ab8a4' scheduling information from config hosting server failed, There is no build resource corresponding to this image.
```



curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.32.169:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
20260109022cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824



curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.32.53:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.32.211:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"



ImportHECImageTask-fail:create server error : httpCode:400;response:{"error":{"message":"query data image [null] fail:[<html>\n<head>\n<title>404 Not Found</title>\n</head>\n<body>\n<h1>404 Not Found</h1>\nNo image found with ID null<br />\n<br />\n\n</body> </html>]","code":"Ecs.0304","details":[{"code":"Ecs.1520","message":"Failed to call Glance API to query image. Fail reason is: no image found with ID null."}]}}


curl -H "Content-Type: application/json" -H "appid:00000000000000000000000000000092" -H "token:apMK3woDRwd6xEJZokRU7pf1KoE40+pL86PRZXog" -H "account:op_fts" -H "enterprise:88888888888888888888888888888888" -X POST -d 'hello' "http://10.201.33.154:80/file?sha256=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


![2026-01-29_162542.png](pic20260129/2026-01-29_162542.png)



## 6.APIG

/apigw_portals/data/api/test
2026-01-29 16:40:47.892 [http-nio-0.0.0.0-8081-exec-60040] - [ERROR] [o.a.c.c.C.[.[.[/apigw_portals].[dispatcherServlet] : 175] -Servlet.service() for servlet [dispatcherServlet] in context with path [/apigw_portals] threw exception [Request processing failed; nested exception is java.lang.NullPointerException] with root cause
java.lang.NullPointerException: null


/apigw_portals/data/api/test  NullPointerException



/authorization/services/jalor/security/user/tryFindOrCreateUser/w3Account/autoCreateUser

## 7.
提交代码

git config --global user.name "m30026548"
git config --global user.email "maoguansong@yw-partners.com"

```text
Cloning into 'APIG-PythonScript'...
fatal: unable to access 'https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git/': schannel: SEC_E_UNTRUSTED_ROOT (0x80090325) - ֤�������ɲ������εİ䷢�����䷢�ġ�

```

> git克隆报错问题解决
> https://3ms.huawei.com/km/blogs/details/21407544

```shell
git config --system http.sslbackend openssl

$ git config --system http.sslbackend openssl
error: could not lock config file C:/Program Files/Git/etc/gitconfig: Permission denied

```


https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git

```shell
m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git clone https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git
Cloning into 'APIG-PythonScript'...
fatal: unable to access 'https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git/': schannel: SEC_E_UNTRUSTED_ROOT (0x80090325) - ֤�������ɲ������εİ䷢�����䷢�ġ�

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
user.name=MichaleSquirrel
user.email=122731161+MichaleSquirrel@users.noreply.github.com
credential.https://codehub-dg-g.huawei.com.provider=generic

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --global user.name "m30026548"

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --global user.email "maoguansong@yw-partners.com"

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
user.name=m30026548
user.email=maoguansong@yw-partners.com
credential.https://codehub-dg-g.huawei.com.provider=generic

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git clone https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git
Cloning into 'APIG-PythonScript'...
fatal: unable to access 'https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git/': schannel: SEC_E_UNTRUSTED_ROOT (0x80090325) - ֤�������ɲ������εİ䷢�����䷢�ġ�

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --system http.sslbackend openssl
error: could not lock config file C:/Program Files/Git/etc/gitconfig: Permission denied

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --system http.sslbackend openssl
error: could not lock config file C:/Program Files/Git/etc/gitconfig: Permission denied

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --system http.sslbackend openssl
error: could not lock config file C:/Program Files/Git/etc/gitconfig: Permission denied

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git config --global http.sslVerify false

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git clone https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git
Cloning into 'APIG-PythonScript'...
warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more information.
warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more information.
fatal: User cancelled dialog.



m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git clone https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git
Cloning into 'APIG-PythonScript'...


m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git clone https://codehub-g-git.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript.git
Cloning into 'APIG-PythonScript'...
warning: ----------------- SECURITY WARNING ----------------
warning: | TLS certificate verification has been disabled! |
warning: ---------------------------------------------------
warning: HTTPS connections may not be secure. See https://aka.ms/gcm/tlsverify for more information.
remote: Enumerating objects: 51, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 51 (delta 0), reused 0 (delta 0), pack-reused 50 (from 1)
Unpacking objects: 100% (51/51), 12.59 KiB | 91.00 KiB/s, done.

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ git fetch
fatal: not a git repository (or any of the parent directories): .git

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ ll
total 0
drwxr-xr-x 1 m30026548 1049089 0 Jan 29 21:11 APIG-PythonScript/

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104
$ cd APIG-PythonScript/

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (master)
$ git fetch

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (master)
$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/develop
  remotes/origin/master
  remotes/origin/person_l30036208_01
  remotes/origin/person_m30026548

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (master)
$ git checkout -b person_l30036208_01 /origin/person_l30036208_01
fatal: Invalid path 'C:/Program Files/Git/origin': No such file or directory

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (master)
$ git checkout -b person_l30036208_01 origin/person_l30036208_01
branch 'person_l30036208_01' set up to track 'origin/person_l30036208_01'.
Switched to a new branch 'person_l30036208_01'

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (person_l30036208_01)
$ git status
On branch person_m30026548
Your branch is up to date with 'origin/person_m30026548'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/

nothing added to commit but untracked files present (use "git add" to track)

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (person_m30026548)
$ git merge develop
Updating cfb13bd..61ab776
Fast-forward
 .cloudbuild/build.sh      |  56 ++++++++
 .cloudbuild/build.yml     |  34 +++++
 .codecheck/check.yml      |  16 +++
 FetchAppOwnerFromIam.py   | 152 +++++++++++++++++++++
 FetchProdInfoFromEAMAP.py | 334 ++++++++++++++++++++++++++++++++++++++++++++++
 log_rotate.sh.py          | 158 ++++++++++++++++++++++
 requirements.txt          | Bin 0 -> 1108 bytes
 7 files changed, 750 insertions(+)
 create mode 100644 .cloudbuild/build.sh
 create mode 100644 .cloudbuild/build.yml
 create mode 100644 .codecheck/check.yml
 create mode 100644 FetchAppOwnerFromIam.py
 create mode 100644 FetchProdInfoFromEAMAP.py
 create mode 100644 log_rotate.sh.py
 create mode 100644 requirements.txt

m30026548@DESKTOP-U0TQ3BB MINGW64 /d/202601291104/APIG-PythonScript (person_m30026548)
$ git

```

Guan@3279502884Song