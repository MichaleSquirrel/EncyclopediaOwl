Thursday February 26 Day 057 week 9 of 2026

## 1.TodoList



## 2.运维脚本

DevOps Scripts

虎君，我提交的代码，请审批
https://codehub-g.rnd.yinwang.com/IAS_IT/Resources/APIG/APIG-PythonScript/merge_requests/3


翻译  运维脚本

operational scripts


“运维脚本”翻译为英文是 Operations Script、Operations Scripting 或 DevOps Script。通常也称为 Ops Script、Automation Script (自动化脚本) 或 System Administration Script (系统管理脚本)。

> 九个 Python 运维脚本封神！比 Shell 简单十倍，新手复制直接用（附完整代码）
> https://www.51cto.com/article/830775.html


```python
import psutil
import datetime

def check_system_resource():
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"=== 服务器资源检查报告（{current_time}）===")

    # CPU使用率（interval=1表示采样1秒，更准确）
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU 使用率：{cpu_usage}%")
    # 可选：输出每个CPU核心的使用率
    # cpu_core_usage = psutil.cpu_percent(interval=1, percpu=True)
    # print(f"各核心CPU使用率：{cpu_core_usage}")

    # 内存使用率（total=总内存，used=已用，free=空闲）
    mem_info = psutil.virtual_memory()
    mem_total = round(mem_info.total / 1024 / 1024 / 1024, 2)  # 转换为GB
    mem_used = round(mem_info.used / 1024 / 1024 / 1024, 2)
    mem_usage = mem_info.percent
    print(f"内存总量：{mem_total}GB，已用：{mem_used}GB，使用率：{mem_usage}%")

    # 磁盘使用率（默认检查/分区，可修改为其他分区如/data）
    disk_info = psutil.disk_usage('/')
    disk_total = round(disk_info.total / 1024 / 1024 / 1024, 2)
    disk_used = round(disk_info.used / 1024 / 1024 / 1024, 2)
    disk_usage = disk_info.percent
    print(f"磁盘总量：{disk_total}GB，已用：{disk_used}GB，使用率：{disk_usage}%")

    # 可选：添加告警阈值（使用率超过85%提示警告）
    if cpu_usage > 85 or mem_usage > 85 or disk_usage > 85:
        print("\n⚠️  警告：部分资源使用率超过85%，请及时检查！")

if __name__ == "__main__":
    check_system_resource()
```


markdown  python

markdown  展示 python 代码

```shell
D:\ProgrammFiles\python314\python.exe "D:\202601291104\APIG-PythonScript\ DevOpsScript\check_resource.py" 
=== 服务器资源检查报告（2026-02-26 09:25:20）===
CPU 使用率：2.6%
内存总量：31.63GB，已用：17.47GB，使用率：55.2%
磁盘总量：1676.13GB，已用：242.84GB，使用率：14.5%

Process finished with exit code 0
```


25年的可以在scmt平台统计（https://scmt.rnd.huawei.com/CompassWeb/codeQuery/personal）
26年的在腾雾平台统计（https://tengwu.rnd.yinwang.com/trustworth-web/#/contribution）
大家平时都关注下自己的代码量情况，保证要满足要求  @所有人 

![2026-02-26_100810.png](pic20260226/2026-02-26_100810.png)


```python
毛关松，我来帮你优化这个服务器巡检脚本。主要改进点包括：异常处理、代码结构优化、功能增强等。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
服务器巡检脚本 - 优化版
作者：毛关松
功能：生成详细的服务器巡检报告，支持text/json格式输出
"""

import datetime
import json
import platform
import psutil
import socket
import sys
from typing import Dict, Any, List

def generate_inspection_report(output_format: str = "text") -> Dict[str, Any]:
    """
    生成服务器巡检报告 - 优化版本
    
    Args:
        output_format: 输出格式，支持"text"或"json"
    
    Returns:
        dict: 巡检报告数据
    """
    try:
        # 收集系统基础信息
        report = {
            "巡检时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "服务器标识": {
                "主机名": platform.node(),
                "操作系统": platform.platform(),
                "内核版本": platform.uname().release,
                "系统架构": platform.architecture()[0]
            },
            "CPU信息": {
                "逻辑核心数": psutil.cpu_count(logical=True),
                "物理核心数": psutil.cpu_count(logical=False),
                "当前使用率(%)": psutil.cpu_percent(interval=1),
                "各核心使用率(%)": psutil.cpu_percent(interval=1, percpu=True)
            },
            "内存信息": {
                "总内存(GB)": round(psutil.virtual_memory().total / (1024**3), 2),
                "已用内存(GB)": round(psutil.virtual_memory().used / (1024**3), 2),
                "内存使用率(%)": psutil.virtual_memory().percent,
                "可用内存(GB)": round(psutil.virtual_memory().available / (1024**3), 2)
            },
            "磁盘信息": {
                "根分区使用率(%)": psutil.disk_usage('/').percent,
                "根分区总大小(GB)": round(psutil.disk_usage('/').total / (1024**3), 2),
                "根分区可用空间(GB)": round(psutil.disk_usage('/').free / (1024**3), 2)
            },
            "网络信息": {
                "网络接口": [],
                "IP地址信息": []
            },
            "系统负载": {
                "最近1分钟": os.getloadavg()[0] if hasattr(os, 'getloadavg') else "N/A",
                "最近5分钟": os.getloadavg()[1] if hasattr(os, 'getloadavg') else "N/A",
                "最近15分钟": os.getloadavg()[2] if hasattr(os, 'getloadavg') else "N/A"
            } if hasattr(os, 'getloadavg') else {"系统负载": "不支持"}
        }

        # 增强的网络信息收集
        net_if_addrs = psutil.net_if_addrs()
        interfaces_collected = set()
        
        for ifname, addrs in net_if_addrs.items():
            interface_info = {
                "接口名称": ifname,
                "IPv4地址": [],
                "IPv6地址": [],
                "MAC地址": ""
            }
            
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address != "127.0.0.1":
                    interface_info["IPv4地址"].append({
                        "地址": addr.address,
                        "掩码": addr.netmask,
                        "广播地址": addr.broadcast
                    })
                    report["网络信息"]["IP地址信息"].append({
                        "接口": ifname,
                        "类型": "IPv4",
                        "地址": addr.address
                    })
                elif addr.family == socket.AF_INET6:
                    interface_info["IPv6地址"].append({
                        "地址": addr.address,
                        "掩码": addr.netmask
                    })
                elif addr.family == psutil.AF_LINK:
                    interface_info["MAC地址"] = addr.address
            
            if interface_info["IPv4地址"] or interface_info["IPv6地址"]:
                report["网络信息"]["网络接口"].append(interface_info)
                interfaces_collected.add(ifname)

        # 收集磁盘分区信息
        try:
            disk_partitions = psutil.disk_partitions()
            report["磁盘分区详情"] = []
            for partition in disk_partitions:
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    report["磁盘分区详情"].append({
                        "设备": partition.device,
                        "挂载点": partition.mountpoint,
                        "文件系统": partition.fstype,
                        "总大小(GB)": round(usage.total / (1024**3), 2),
                        "使用率(%)": usage.percent
                    })
                except PermissionError:
                    continue  # 跳过无权限访问的分区
        except Exception as e:
            report["磁盘分区详情"] = f"收集失败: {str(e)}"

        return report

    except Exception as e:
        error_report = {
            "巡检时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "错误信息": f"巡检过程发生错误: {str(e)}",
            "建议": "请检查psutil库是否安装正确，或使用管理员权限运行"
        }
        return error_report

def save_report(report: Dict[str, Any], output_format: str) -> str:
    """保存报告到文件"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format == "json":
        filename = f"server_inspection_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
    else:
        filename = f"server_inspection_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== 服务器巡检报告 ===\n")
            f.write(f"生成时间：{report.get('巡检时间', 'N/A')}\n\n")
            
            for category, data in report.items():
                if category == "巡检时间":
                    continue
                    
                f.write(f"【{category}】\n")
                if isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, list):
                            f.write(f"  {key}:\n")
                            for item in value:
                                if isinstance(item, dict):
                                    for sub_key, sub_value in item.items():
                                        f.write(f"    - {sub_key}: {sub_value}\n")
                                else:
                                    f.write(f"    - {item}\n")
                        else:
                            f.write(f"  - {key}: {value}\n")
                else:
                    f.write(f"  {data}\n")
                f.write("\n")
    
    return filename

def print_text_report(report: Dict[str, Any]):
    """以文本格式打印报告"""
    print("=== 服务器巡检报告 ===")
    print(f"生成时间：{report.get('巡检时间', 'N/A')}\n")
    
    for category, data in report.items():
        if category == "巡检时间":
            continue
            
        print(f"【{category}】")
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    print(f"  {key}:")
                    for item in value:
                        if isinstance(item, dict):
                            for sub_key, sub_value in item.items():
                                print(f"    - {sub_key}: {sub_value}")
                        else:
                            print(f"    - {item}")
                else:
                    print(f"  - {key}: {value}")
        else:
            print(f"  {data}")
        print()

def main():
    """主函数"""
    # 解析命令行参数
    output_format = "text"
    if len(sys.argv) > 1 and sys.argv[1] in ["json", "text"]:
        output_format = sys.argv[1]
    
    print("🔍 正在收集服务器信息...")
    
    # 生成巡检报告
    report = generate_inspection_report(output_format)
    
    # 输出报告
    if output_format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)
    
    # 保存报告
    filename = save_report(report, output_format)
    print(f"📄 报告已保存到: {filename}")
    
    # 健康状态简要评估
    if "错误信息" not in report:
        mem_usage = report["内存信息"]["内存使用率(%)"]
        disk_usage = report["磁盘信息"]["根分区使用率(%)"]
        cpu_usage = report["CPU信息"]["当前使用率(%)"]
        
        print("💡 健康状态简要评估:")
        print(f"  - CPU使用率: {cpu_usage}% {'⚠️' if cpu_usage > 80 else '✅'}")
        print(f"  - 内存使用率: {mem_usage}% {'⚠️' if mem_usage > 85 else '✅'}")
        print(f"  - 磁盘使用率: {disk_usage}% {'⚠️' if disk_usage > 90 else '✅'}")

if __name__ == "__main__":
    main()
```

## 主要优化点：

### 1. **异常处理增强**
- 添加了完整的try-catch异常处理
- 对无权限访问的磁盘分区进行跳过处理

### 2. **信息收集增强**
- 增加系统架构、系统负载等信息
- 详细的网络接口信息（IPv4/IPv6/MAC地址）
- 完整的磁盘分区信息收集

### 3. **代码结构优化**
- 模块化函数设计，提高可读性和可维护性
- 添加类型注解
- 详细的文档字符串

### 4. **输出格式优化**
- 支持命令行参数指定输出格式
- 时间戳文件名，避免覆盖
- 更清晰的分层显示结构

### 5. **新增功能**
- 健康状态简要评估
- 更详细的错误提示和建议
- 支持各核心CPU使用率显示

### 使用方法：
```bash
# 文本格式输出（默认）
python server_inspection.py

# JSON格式输出
python server_inspection.py json
```
```
这个优化版本更适合生产环境使用，具有更好的稳定性和可扩展性。
```


## 4

tar -zcvf mqs-proxy.tar.gz tomcat-mqs-web
tar -zcvf tomcat-mqs-web.tar.gz tomcat-mqs-web

```shell
Your current local directory is
D:\Users\yebeta_m30026548_52\Documents\NetSarang Computer\6\Xshell\Sessions

Type `help' to browse available commnands.
sftp:/data01/ump/mqs-prod> dir
sftp: unknown command "dir"
sftp:/data01/ump/mqs-prod> ls
drwxr-xr-x    9 umpadmin umpgrp        203 Aug  8  2025 .
drwx------   14 umpadmin umpgrp       4096 Feb  9 16:31 ..
drwxr-xr-x    4 umpadmin umpgrp         65 Aug  8  2025 mqs-rest-api
drwx------    5 umpadmin umpgrp        173 Aug  8  2025 mqs-auditor-message-20250808143626
drwxr-xr-x    3 umpadmin umpgrp        108 Aug  8  2025 mqs-proxy-20250808143627
drwxr-xr-x    3 umpadmin umpgrp        108 Feb 24 11:06 mqs-proxy
drwx------    5 umpadmin umpgrp        173 Aug  8  2025 mqs-auditor-message
drwxr-xr-x    9 umpadmin umpgrp        220 Dec 17  2024 tomcat-mqs-web-20250808143648
drwxr-xr-x    9 umpadmin umpgrp        220 Dec 17  2024 tomcat-mqs-web
sftp:/data01/ump/mqs-prod> get mqs-proxy
Fetching /data01/ump/mqs-prod/mqs-proxy to mqs-proxy
sftp: error occurred while receiving a file
sftp:/data01/ump/mqs-prod> ls
drwxr-xr-x    9 umpadmin umpgrp        256 Feb 26 15:18 .
drwx------   14 umpadmin umpgrp       4096 Feb  9 16:31 ..
drwxr-xr-x    4 umpadmin umpgrp         65 Aug  8  2025 mqs-rest-api
drwx------    5 umpadmin umpgrp        173 Aug  8  2025 mqs-auditor-message-20250808143626
drwxr-xr-x    3 umpadmin umpgrp        108 Aug  8  2025 mqs-proxy-20250808143627
drwxr-xr-x    3 umpadmin umpgrp        108 Feb 24 11:06 mqs-proxy
drwx------    5 umpadmin umpgrp        173 Aug  8  2025 mqs-auditor-message
drwxr-xr-x    9 umpadmin umpgrp        220 Dec 17  2024 tomcat-mqs-web-20250808143648
drwxr-xr-x    9 umpadmin umpgrp        220 Dec 17  2024 tomcat-mqs-web
-rw-r--r--    1 root     root     39218875 Feb 26 15:16 mqs-proxy.tar.gz
-rw-r--r--    1 root     root     173117185 Feb 26 15:18 tomcat-mqs-web.tar.gz
sftp:/data01/ump/mqs-prod> get mqs-proxy.tar.gz
Fetching /data01/ump/mqs-prod/mqs-proxy.tar.gz to mqs-proxy.tar.gz
sftp: received 37.4 MB in 1.03 seconds
sftp:/data01/ump/mqs-prod> get tomcat-mqs-web.tar.gz
Fetching /data01/ump/mqs-prod/tomcat-mqs-web.tar.gz to tomcat-mqs-web.tar.gz
sftp: received 165 MB in 4.26 seconds
sftp:/data01/ump/mqs-prod> 

```
![2026-02-26_152259.png](pic20260226/2026-02-26_152259.png)


```shell
useradd -d /data01/ump -g 1001 umpadmin
```
Caused by: redis.clients.jedis.exceptions.JedisDataException: ERR invalid password


## 6

> 吊打面试官之Java ConcurrentLinkedQueue
> https://javabetter.cn/thread/ConcurrentLinkedQueue.html#%E8%8A%82%E7%82%B9%E7%B1%BBnode
> LinkedBlockingQueue与ConcurrentLinkedQueue的区别
> https://blog.csdn.net/lzxlfly/article/details/86710382
> ConcurrentLinkedQueue使用和方法介绍
> https://www.cnblogs.com/yangzhenlong/p/8359875.html

97（多选题）针对java.util.concurrent，以下说法正确的有（ABCD）


A.
ConcurrentLinkedQueue是基于CAS实现的无锁线程安全高性能队列


B.
ConcurrentLinkedQueue的HOPS(延迟更新的策略)是指间隔1次进行才利用CAS更新tail或head，减少CAS操作带来的损耗


C.
LinkedBlockingQueue是基于锁分离的线程安全的FIFO单链表


D.
ForkJoinPool的workQueue是队列通过哈希算法将竞争分散到各个队列上来降低单一队列上的过度竞争