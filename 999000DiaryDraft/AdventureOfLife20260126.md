Monday January 26 Day 026 week 5 of 2026

## 1.TodoList
1. 本周把工作级科目二和科目三搞定
2. 然后开始准备科目四
3. android 单机版和日期显示软件，相关框架用到的设计模式
4. 准备个人简历，多面试
5. 扣翻筋，小学老师
6. 为什么录屏软件 无法 录屏


## 2.代码量统计

刘志 60091017 2026-01-21 11:12
又快月底了，大家记得及时关注自己当月的交付件产出，产出不够的月底前补齐下。 @所有人 
刘志 60091017 2026-01-21 11:13
还有开发同学不知道代码量统计地址的，我再发一下
刘志 60091017 2026-01-21 11:14
代码量统计平台地址
左侧CMC：https://committer.huawei.com/#/committerManagement/committerMechanism?appId=FWjWX6337352021032511387
左侧SCMT：https://scmt.rnd.huawei.com/CompassWeb/codeQuery/personal
左侧个人能力看板：https://his.huawei.com/devopsone/home/#/personalwb/homeDashboard?activeDashboardhome=%E4%B8%AA%E4%BA%BA%E8%83%BD%E5%8A%9B%E7%9C%8B%E6%9D%BF
右侧IAS质量看板：https://tengwu.rnd.yinwang.com/trustworth-web/#/contribution
@所有人 
刘志 60091017 2026-01-21 11:15
开发同学记得收藏一下地址，以免信息多了又找不到


https://wiki.rnd.yinwang.com/domains/1174/wiki/60041/WIKI202506247240902
这个是右侧代码量统计平台的wiki

## 3.提交代码



## 4.测试环境MQS服务器CentOS升级

## 4.测试环境MQS的升级
李胜沛 00847799 2025-12-24 18:20
我们的测试环境的MQS是CentOS的，可以先升级到HCE 2.0
明天开始，有空可以准备下测试环境MQS的升级了  @毛关松 
先拿测试环境来练练手

测试环境租户侧MQS的机器已经纳管到EC2了

![44002047-AC9A-49A4-AE0F-9D209D171DED.png](pic20251225/44002047-AC9A-49A4-AE0F-9D209D171DED.png)

![2C3CC301-4D26-4FEA-D3E3-7E9010949E74.png](pic20251225/2C3CC301-4D26-4FEA-D3E3-7E9010949E74.png)
这个OS版本，实际上是CentOS，只是ywit上没有centos了，所以展示不了


### 4.1 之前提供的材料
![2025-12-25_153732.png](pic20251225/2025-12-25_153732.png)

![BB4D6636-800B-41E5-B131-7CA341711BEA.png](pic20251225/BB4D6636-800B-41E5-B131-7CA341711BEA.png)

李胜沛 00847799 2025-12-03 11:37
我们现在 MQS有很多操作系统是Centos 7.6，当前已经EOS，要求升级到Huawei Cloud EulerOS 2.0, 这个是我之前找齐银鹤要的方案，你也研究下，看看MQS怎么无感升级上去

### 4.2

齐银鹤 00625425 2025-10-24 14:38
这个是三个模板用到的配置，导入liveops平台后改名SysDiskUpgrade，并把各个参数按需调整


![bc0cb742-0fab-4a72-b5ab-82c7204fdb63.png](pic20251225/bc0cb742-0fab-4a72-b5ab-82c7204fdb63.png)

![422d9a8f-1561-487a-b4bb-cc404a4e058c.png](pic20251225/422d9a8f-1561-487a-b4bb-cc404a4e058c.png)



### 4.3 2026年1月26号新任务
李胜沛 00847799 2026-01-26 10:50
关松  融合联接这边  OS切换的
后面你统一负责一下
你可以让对应的责任人来搞
毛关松 30026548 2026-01-26 10:51
好的，正在看MQS的要怎么升级
李胜沛 00847799 2026-01-26 10:51
你马上要续签了，给你安排一些比较容易出成绩的活
到时好写一点
OS切换的统一你来负责
到时带着他们搞
毛关松 30026548 2026-01-26 10:52
嗯，感谢
李胜沛 00847799 2026-01-26 10:58
https://onebox.huawei.com/v/c44e7aac14cf14b3c025962bc775d92b?type=1
这是待切换的OS清单
毛关松 30026548 2026-01-26 10:58
好的
李胜沛 00847799 2026-01-26 10:59
绿色是已经完成的
这是CentOS的
李胜沛 00847799 2026-01-26 11:00
还有Euler2.9的，也要切换成HCE2.0，这是Euler2.9的清单：https://onebox.huawei.com/v/86ffb2d7e417faa39566302cd42ddb93?type=1&sheet=%E5%85%A8%E7%BD%91%E5%BE%85%E5%88%87%E6%8D%A2Euler2.9%E6%80%BB%E8%A1%A8
MQS的几乎每一台机器都要升级
你主要投入到MQS上，看看怎么升上去
李胜沛 00847799 2026-01-26 11:01
50-60台


```shell
"script":"#!/bin/bash\n# sys_1.1-backup.sh\n# 需要持续完善\nmqs_white_process_list=(\"java\" \"prometheus\" \"grafana\" \"redis\")\nmqs_white_process_info=\"\"\nmqs_white_process_count=0\n# 进程黑名单，如果检查到了，就报错不再执行, 用来防止系统盘安装的软件丢失\nmqs_black_process_list=(\"nginx\")\n# 忽略名单，不需要进行恢复的应用\nmqs_ignore_process_pattern=\".*((logstash)|(node_exporter)|(doris)|(DorisBE)|(TrustTestJavaExecutor)|(RasFireServer)).*\"\n\nes_auth_header=\"${esAuthHeader}\"\nes_addr=\"${esAddr}\"\n\nfunction check_black_process(){\n    total=0\n    for item in \"${mqs_black_process_list[@]}\"; do\n        process_list_count=$(ps -ef|grep $item|grep -v grep|wc -l)\n        echo \"$item : process_list_count: ${process_list_count} \"\n        if (( process_list_count > 0 )); then\n           total=$((total+process_list_count))\n        fi\n    done\n    echo \"black total process count: ${total}\"\n    if (( total > 0 )); then\n        echo \"black total process exits. exit with error\"\n        exit 1\n    fi\n}\n\nfunction get_white_process_count(){\n    mqs_white_process_count=0\n    for item in \"${mqs_white_process_list[@]}\"; do\n        process_list_count=$(ps -ef|grep $item|grep -v grep|grep -vE \"${mqs_ignore_process_pattern}\"|wc -l)\n        process_info=$(ps -ef|grep $item|grep -v grep|grep -vE \"${mqs_ignore_process_pattern}\")\n        if (( process_list_count > 0 )); then\n            mqs_white_process_info=\"${mqs_white_process_info} \\n ${process_info}\"\n            mqs_white_process_count=$((mqs_white_process_count+process_list_count))\n        fi\n    done\n    if (( mqs_white_process_count == 0 )); then\n        echo \"mqs_white_process_count is 0. exit with error\"\n        exit 1\n    fi\n    mqs_white_process_info=$(echo \"${mqs_white_process_info}\" | sed ':a;N;$!ba;s/\\n/\\\\n/g' )\n}\n\n# 检查条件：data01必须挂载，并且总容量大于90G\nfunction check_disk_mount_status(){\n    echo \"check_disk_mount_status start.\"\n    data01_mount_count=$(df -h |grep data01|wc -l)\n    if (( data01_mount_count != 1 )); then\n        echo \"data01 mount error, please check the host disk mount status. exit with error\"\n        exit 1\n    fi\n    echo \"data01 disk is mounted\"\n\n    data01_total_size_gb=$(df --output=size -B 1G /data01 | awk 'NR==2 {print $1}')\n    if (( data01_total_size_gb < 90 )); then\n        echo \"data01 total size is less than 90GB, please check the host disk mount status. exit with error\"\n        exit 1\n    fi\n    echo \"data01 disk total size is ${data01_total_size_gb} GB\"\n\n    echo \"check_disk_mount_status finish.\"\n}\n\n\n# 这个脚本是为了在升级前对OS的信息进行备份\nfunction backup_info_remote () {\n    os_host_name=$(hostname -s)\n    ip_count=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}'|wc -l)\n    if (( ip_count != 1 )); then\n        echo \"ip_count:${ip_count} is not 1. exit with error\"\n        exit 1\n    fi\n    ip=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}')\n\n    osversion=$(uname -a)\n    now=$(date +\"%Y-%m-%d %H:%M:%S\")\n    unixtimestamp=$(date +%s)\n    unixtimestamp_millis=\"${unixtimestamp}000\"\n    fstab_info=$(grep -E \".*((data01)|(data02)).*\" /etc/fstab | sed ':a;N;$!ba;s/\\n/\\\\n/g')\n    passwd_info=$(grep -E \".*((mqsadmin)|(umpadmin)|(fts)).*\" /etc/passwd | sed ':a;N;$!ba;s/\\n/\\\\n/g')\n    # umpadmin_process=$(ps -ef|grep -v grep|grep -E \".*((mqsadmin)|(umpadmin)|(nginx)|(prometheus)|(grafana)|(redis)).*\"| sed ':a;N;$!ba;s/\\n/\\\\n/g')\n    java_process=$(jps -l | grep -v jps| sed ':a;N;$!ba;s/\\n/\\\\n/g')\n    crontab_info=$(crontab -l -u umpadmin | sed ':a;N;$!ba;s/\\n/\\\\n/g')\n    jvm_info=$(grep -E \".*((JAVA_HOME)).*\" /etc/profile | sed ':a;N;$!ba;s/\\n/\\\\n/g')\n    data01_used_GBytes=$(du -sh --block-size=1G /data01 |awk '{print $1}')\n    data01_total_size_gb=$(df --output=size -B 1G /data01 | awk 'NR==2 {print $1}')\n    data=\"{\n        \\\"hostname\\\": \\\"${os_host_name}\\\",\n        \\\"fstab\\\": \\\"${fstab_info}\\\",\n        \\\"passwd\\\": \\\"${passwd_info}\\\",\n        \\\"osversion\\\": \\\"${osversion}\\\",\n        \\\"time\\\": \\\"${now}\\\",\n        \\\"unixtimestamp\\\": ${unixtimestamp},\n        \\\"unixtimestamp_millis\\\": ${unixtimestamp_millis},\n        \\\"ip\\\": \\\"${ip}\\\",\n        \\\"java_process\\\": \\\"${java_process}\\\",\n        \\\"crontab_info\\\": \\\"${crontab_info}\\\",\n        \\\"jvm_info\\\": \\\"${jvm_info}\\\",\n        \\\"data01_used_GBytes\\\": \\\"${data01_used_GBytes}\\\",\n        \\\"data01_total_size_gb\\\": \\\"${data01_total_size_gb}\\\",\n        \\\"mqs_white_process_info\\\": \\\"${mqs_white_process_info}\\\",\n        \\\"mqs_white_process_count\\\": \\\"${mqs_white_process_count}\\\"\n    }\"\n\n    echo -e \"\\n${data}\\n\"\n\n    if [[ -z \"${crontab_info}\" ]]; then\n        echo \"crontab_info is empty, exit with error\"\n        exit 2\n    fi\n    if [[ -z \"${passwd_info}\" ]]; then\n        echo \"passwd_info is empty, exit with error\"\n        exit 2\n    fi\n    if [[ -z \"${osversion}\" ]]; then\n        echo \"osversion is empty, exit with error\"\n        exit 2\n    fi\n    if [[ -z \"${os_host_name}\" ]]; then\n        echo \"os_host_name is empty, exit with error\"\n        exit 2\n    fi\n    if [[ -z \"${ip}\" ]]; then\n        echo \"ip is empty, exit with error\"\n        exit 2\n    fi\n    if [[ -z \"${fstab_info}\" ]]; then\n        echo \"fstab_info is empty, exit with error\"\n        exit 2\n    fi\n\n    temp_resp_file=/tmp/mqs_temp_resp_file.log\n\n    http_code=$(curl --connect-timeout 5 --max-time 30 -s -S -w \"%{http_code}\" --request POST \\\n    --url ${es_addr}'/os-system-replace-backup/_doc' \\\n    --header \"${es_auth_header}\" \\\n    --header 'Content-Type: application/json' \\\n    -o \"${temp_resp_file}\" \\\n    --data \"${data}\")\n    exit_code=$?\n\n    echo \"respose body:\"\n    cat \"${temp_resp_file}\"\n    echo -e \"\\n\"\n    rm -f \"${temp_resp_file}\"\n\n    if [ $exit_code -ne 0 ]; then\n        echo \"request error, exit code: $exit_code\"\n        exit 1\n    elif [[ $http_code =~ ^2 ]]; then  # 2xx 表示成功\n        echo \"request success, HTTP code: $http_code\"\n    else\n        echo \"request error, HTTP code: $http_code\"\n        exit 2\n    fi\n\n}\n\n\n\n# 获得机器备份的信息, 检查是否备份成功\nfunction get_os_backup_info () {\n    os_host_name=$(hostname -s)\n\n    os_info=$(curl  --connect-timeout 5 --max-time 30 --request POST \\\n    --url ${es_addr}'/os-system-replace-backup/_search?format=json&pretty=true' \\\n    --header \"${es_auth_header}\" \\\n    --header 'Content-Type: application/json' \\\n    --data \"{\\\"query\\\":{\\\"bool\\\":{\\\"must\\\":[{\\\"match\\\":{\\\"hostname\\\":\\\"${os_host_name}\\\"}}],\\\"must_not\\\":[],\\\"should\\\":[]}},\\\"from\\\":0,\\\"size\\\":1,\\\"sort\\\":[{\\\"unixtimestamp\\\":{\\\"order\\\":\\\"desc\\\"}}],\\\"aggs\\\":{}}\")\n\n    backup_hostname=$(echo \"${os_info}\" | grep '\"hostname\" :'| grep -oP '(?<=: \")[^\"]+')\n    # backup_time=$(echo \"${os_info}\" | grep '\"time\" :'| grep -oP '(?<=: \")[^\"]+')\n    backup_unixtimestamp=$(echo \"${os_info}\" | grep '\"unixtimestamp\" :'| grep -o '[0-9]\\+')\n    backup_ip=$(echo \"${os_info}\" | grep '\"ip\" :'| grep -oP '(?<=: \")[^\"]+')\n\n    echo \"backup_hostname=${backup_hostname}\"\n    echo \"backup_ip=${backup_ip}\"\n    # echo \"backup_time=${backup_time}\"\n    echo \"backup_unixtimestamp=${backup_unixtimestamp}\"\n\n    # check again\n    current_os_host_name=$(hostname -s)\n    echo \"current_os_host_name=${current_os_host_name}\"\n    ip_count=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}'|wc -l)\n    if (( ip_count != 1 )); then\n        echo \"ip_count:${ip_count} is not 1. exit with error\"\n        exit 1\n    fi\n    current_ip=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}')\n    if [[ \"${current_os_host_name}\" != \"${backup_hostname}\" ]]; then\n        echo \"The os info backup error, because hostname, exit.\"\n        exit 1;\n    fi\n    if [[ \"${current_ip}\" != \"${backup_ip}\" ]]; then\n        echo \"The os info backup error, because backup_ip, exit.\"\n        exit 2;\n    fi\n    unixtimestamp_current=$(date +%s)\n    delta_time=$((unixtimestamp_current - backup_unixtimestamp))\n    if (( delta_time > 120 )); then\n        echo \"The backup info time ${delta_time} is more than 60s, exit.\"\n        exit 3;\n    fi\n    echo \"The current_os_host_name and current_ip equals to backup_hostname and backup_ip\"\n    echo -e \"check get the os system info from es : \\n ${os_info}\"\n\n}\n\n\ncheck_black_process\nget_white_process_count\ncheck_disk_mount_status\n\nbackup_info_remote\n# 为了确保下一步的查询校验成功，要等ES 30S\nsleep 30\nget_os_backup_info\n\necho -e \"\\nback info remote finish.\\n\"\n\n",
			
```

用java写一段代码，把脚本写入文本文件


18123708371


这是一个用于系统备份的Bash脚本，主要功能是在系统升级前进行环境检查和信息备份。以下是脚本的主要功能解读：

主要功能模块
1. 进程检查
   白名单进程：检查java、prometheus、grafana、redis等关键服务是否运行
   黑名单进程：检查nginx是否运行（如果存在则报错退出）
   忽略模式：排除logstash、node_exporter等不需要恢复的应用
2. 磁盘状态检查
   验证/data01目录是否正常挂载
   检查/data01分区容量是否大于90GB
3. 系统信息备份
   备份以下信息到Elasticsearch：

主机名、IP地址、系统版本
/etc/fstab中data相关配置
/etc/passwd中用户信息
Java进程列表（jps输出）
umpadmin用户的crontab任务
JVM环境变量配置
磁盘使用情况统计
4. 备份验证
   从ES查询最新的备份记录
   验证备份数据的完整性和时效性（120秒内）
   执行流程
   检查黑名单进程 → 如有则退出
   统计白名单进程 → 如无关键进程则退出
   检查磁盘挂载状态 → 异常则退出
   收集系统信息并备份到ES
   等待30秒后验证备份是否成功
   脚本特点
   安全防护：通过进程检查和磁盘验证确保执行环境安全
   完整性检查：备份前后都进行数据验证
   远程存储：使用ES作为备份数据存储
   错误处理：严格的异常退出机制
   这个脚本主要用于系统维护升级前的环境检查和信息归档，确保升级过程可追溯、可恢复。

ps -ef|grep nginx|grep -v grep|wc -l

```shell
#!/bin/bash
# sys_1.1-backup.sh
# 需要持续完善
mqs_white_process_list=("java" "prometheus" "grafana" "redis")
mqs_white_process_info=""
mqs_white_process_count=0
# 进程黑名单，如果检查到了，就报错不再执行, 用来防止系统盘安装的软件丢失
mqs_black_process_list=("nginx")
# 忽略名单，不需要进行恢复的应用
mqs_ignore_process_pattern=\".*((logstash)|(node_exporter)|(doris)|(DorisBE)|(TrustTestJavaExecutor)|(RasFireServer)).*"

es_auth_header="${esAuthHeader}"
es_addr="${esAddr}"
function check_black_process(){
 total=0
  for item in "${mqs_black_process_list[@]}"; do
   process_list_count=$(ps -ef|grep $item|grep -v grep|wc -l)
    echo "$item : process_list_count: ${process_list_count} "
     if (( process_list_count > 0 )); then total=$((total+process_list_count))
      fi
       done echo "black total process count: ${total}"
        if (( total > 0 )); then
         echo "black total process exits. exit with error"
          exit 1
           fi
           }
function get_white_process_count(){
 mqs_white_process_count=0 
 for item in "${mqs_white_process_list[@]}"; do
  process_list_count=$(ps -ef|grep $item|grep -v grep|grep -vE "${mqs_ignore_process_pattern}"|wc -l)
   process_info=$(ps -ef|grep $item|grep -v grep|grep -vE "${mqs_ignore_process_pattern}")
    if (( process_list_count > 0 )); then
     mqs_white_process_info="${mqs_white_process_info} \\n ${process_info}"
      mqs_white_process_count=$((mqs_white_process_count+process_list_count))
       fi
        done
         if (( mqs_white_process_count == 0 )); then
          echo "mqs_white_process_count is 0. exit with error"
           exit 1
            fi
             mqs_white_process_info=$(echo "${mqs_white_process_info}" | sed ':a;N;$!ba;s/\\n/\\\\n/g' )
             }
             
# 检查条件：data01必须挂载，并且总容量大于90G
function check_disk_mount_status(){
 echo "check_disk_mount_status start."
  data01_mount_count=$(df -h |grep data01|wc -l)
   if (( data01_mount_count != 1 )); then
    echo "data01 mount error, please check the host disk mount status. exit with error"
     exit 1
      fi
       echo "data01 disk is mounted"
        data01_total_size_gb=$(df --output=size -B 1G /data01 | awk 'NR==2 {print $1}')
         if (( data01_total_size_gb < 90 )); then
          echo "data01 total size is less than 90GB, please check the host disk mount status. exit with error"
           exit 1
            fi
             echo "data01 disk total size is ${data01_total_size_gb} GB"
              echo "check_disk_mount_status finish."
              }
              
              
# 这个脚本是为了在升级前对OS的信息进行备份
function backup_info_remote () {
 os_host_name=$(hostname -s)
  ip_count=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}'|wc -l)
   if (( ip_count != 1 )); then
    echo "ip_count:${ip_count} is not 1. exit with error"
     exit 1
      fi
       ip=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}')
        osversion=$(uname -a)
         now=$(date +\"%Y-%m-%d %H:%M:%S\")
          unixtimestamp=$(date +%s)
           unixtimestamp_millis=\"${unixtimestamp}000"
            fstab_info=$(grep -E \".*((data01)|(data02)).*" /etc/fstab | sed ':a;N;$!ba;s/\\n/\\\\n/g')
             passwd_info=$(grep -E \".*((mqsadmin)|(umpadmin)|(fts)).*\" /etc/passwd | sed ':a;N;$!ba;s/\\n/\\\\n/g'
              # 
              umpadmin_process=$(ps -ef|grep -v grep|grep -E \".*((mqsadmin)|(umpadmin)|(nginx)|(prometheus)|(grafana)|(redis)).*\"| sed ':a;N;$!ba;s/\\n/\\\\n/g')
               java_process=$(jps -l | grep -v jps| sed ':a;N;$!ba;s/\\n/\\\\n/g')
                crontab_info=$(crontab -l -u umpadmin | sed ':a;N;$!ba;s/\\n/\\\\n/g')
                 jvm_info=$(grep -E \".*((JAVA_HOME)).*\" /etc/profile | sed ':a;N;$!ba;s/\\n/\\\\n/g')
                  data01_used_GBytes=$(du -sh --block-size=1G /data01 |awk '{print $1}')\n data01_total_size_gb=$(df --output=size -B 1G /data01 | awk 'NR==2 {print $1}')
                   data="{\n \\\"hostname\\\": \\\"${os_host_name}\\\",\n \\\"fstab\\\": \\\"${fstab_info}\\\",\n \\\"passwd\\\": \\\"${passwd_info}\\\",\n \\\"osversion\\\": \\\"${osversion}\\\",\n \\\"time\\\": \\\"${now}\\\",\n \\\"unixtimestamp\\\": ${unixtimestamp},\n \\\"unixtimestamp_millis\\\": ${unixtimestamp_millis},\n \\\"ip\\\": \\\"${ip}\\\",\n \\\"java_process\\\": \\\"${java_process}\\\",\n \\\"crontab_info\\\": \\\"${crontab_info}\\\",\n \\\"jvm_info\\\": \\\"${jvm_info}\\\",\n \\\"data01_used_GBytes\\\": \\\"${data01_used_GBytes}\\\",\n \\\"data01_total_size_gb\\\": \\\"${data01_total_size_gb}\\\",\n \\\"mqs_white_process_info\\\": \\\"${mqs_white_process_info}\\\",\n \\\"mqs_white_process_count\\\": \\\"${mqs_white_process_count}\\\"\n }\"\n\n echo -e \"\\n${data}\\n\"
                    if [[ -z \"${crontab_info}\" ]]; then
                     echo "crontab_info is empty, exit with error"
                      exit 2
                       fi
                        if [[ -z \"${passwd_info}\" ]]; then
                         echo "passwd_info is empty, exit with error"
                          exit 2
                           fi
                            if [[ -z \"${osversion}\" ]]; then
                             echo "osversion is empty, exit with error"
                              exit 2
                               fi
                                if [[ -z \"${os_host_name}\" ]]; then
                                 echo "os_host_name is empty, exit with error"
                                  exit 2
                                   fi
                                    if [[ -z \"${ip}\" ]]; then
                                    echo "ip is empty, exit with error"
                                     exit 2
                                      fi
                                       if [[ -z \"${fstab_info}\" ]]; then
                                        echo "fstab_info is empty, exit with error"
                                         exit 2
                                          fi
                                           
                                           temp_resp_file=/tmp/mqs_temp_resp_file.log
                                            
                                            http_code=$(curl --connect-timeout 5 --max-time 30 -s -S -w \"%{http_code}\" --request POST \\\n --url ${es_addr}'/os-system-replace-backup/_doc' \\\n --header \"${es_auth_header}\" \\\n --header 'Content-Type: application/json' \\\n -o \"${temp_resp_file}\" \\\n --data \"${data}\")\n exit_code=$?
                                             echo "respose body:" cat "${temp_resp_file}"
                                              echo -e "\\n"
                                               rm -f "${temp_resp_file}"
                                                if [ $exit_code -ne 0 ]; then
                                                 echo "request error, exit code: $exit_code"
                                                  exit 1
                                                   elif [[ $http_code =~ ^2 ]]; then 
                                                  # 2xx 表示成功
                                                   echo "request success, HTTP code: $http_code" 
                                                   else
                                                    echo "request error, HTTP code: $http_code"
                                                     exit 2
                                                      fi
                                                      
                                                      }
                                                      
                                                      
                                                      
                                                      # 获得机器备份的信息, 检查是否备份成功
function get_os_backup_info () {
 os_host_name=$(hostname -s)
  
  os_info=$(curl --connect-timeout 5 --max-time 30 --request POST \\\n --url ${es_addr}'/os-system-replace-backup/_search?format=json&pretty=true' \\\n --header \"${es_auth_header}\" \\\n --header 'Content-Type: application/json' \\\n --data \"{\\\"query\\\":{\\\"bool\\\":{\\\"must\\\":[{\\\"match\\\":{\\\"hostname\\\":\\\"${os_host_name}\\\"}}],\\\"must_not\\\":[],\\\"should\\\":[]}},\\\"from\\\":0,\\\"size\\\":1,\\\"sort\\\":[{\\\"unixtimestamp\\\":{\\\"order\\\":\\\"desc\\\"}}],\\\"aggs\\\":{}}\")\n\n backup_hostname=$(echo \"${os_info}\" | grep '\"hostname\" :'| grep -oP '(?<=: \")[^\"]+')\n # backup_time=$(echo \"${os_info}\" | grep '\"time\" :'| grep -oP '(?<=: \")[^\"]+')\n backup_unixtimestamp=$(echo \"${os_info}\" | grep '\"unixtimestamp\" :'| grep -o '[0-9]\\+')\n backup_ip=$(echo \"${os_info}\" | grep '\"ip\" :'| grep -oP '(?<=: \")[^\"]+')\n\n echo \"backup_hostname=${backup_hostname}\"\n echo \"backup_ip=${backup_ip}\"\n # echo \"backup_time=${backup_time}\"\n echo \"backup_unixtimestamp=${backup_unixtimestamp}\"\n\n # check again\n current_os_host_name=$(hostname -s)\n echo \"current_os_host_name=${current_os_host_name}\"\n ip_count=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}'|wc -l)\n if (( ip_count != 1 )); then\n echo \"ip_count:${ip_count} is not 1. exit with error\"\n exit 1\n fi\n current_ip=$(ifconfig |grep inet|grep -v '127.0.0.1'|awk '{print $2}')\n if [[ \"${current_os_host_name}\" != \"${backup_hostname}\" ]]; then
   echo "The os info backup error, because hostname, exit."
    exit 1;
    fi
    if [[ \"${current_ip}\" != \"${backup_ip}\" ]]; then
     echo "The os info backup error, because backup_ip, exit."
      exit 2;
       fi
        unixtimestamp_current=$(date +%s) delta_time=$((unixtimestamp_current - backup_unixtimestamp))
         if (( delta_time > 120 )); then
          echo "The backup info time ${delta_time} is more than 60s, exit."
           exit 3;
            fi
             echo "The current_os_host_name and current_ip equals to backup_hostname and backup_ip"
              echo -e "check get the os system info from es : \\n ${os_info}\"
              
              }
              
              check_black_process
              get_white_process_count
              check_disk_mount_status
              
              backup_info_remote
              # 为了确保下一步的查询校验成功，要等ES 30S
              sleep 30
              get_os_backup_info
              echo -e "back info remote finish."
              
              
              
```
