# Postman安装

## 1.Postman安装

> 【工具分享】免登陆版postman
> https://3ms.huawei.com/km/groups/3956009/blogs/details/22028993

使用说明
下载提供的 Postman 10.13.6 64位免登陆版本。
解压下载的文件。
运行 Postman 应用程序，开始使用。
注意事项
本资源为旧版本，可能不包含最新功能和安全更新。
请确保操作系统为64位，以保证软件的正常运行。
参照下面的wiki禁用自动更新，否则会升级到新版，新版需要登陆

## 2.禁止Postman自动更新

> 禁止Postman自动更新
> https://3ms.huawei.com/km/groups/3956009/blogs/details/22060359?l=zh-cn



关闭 Postman：确保 Postman 已经完全退出。

打开安装目录：

右键点击 Postman 的桌面快捷方式，选择“打开文件所在的位置”。

或者直接在资源管理器地址栏输入：%localappdata%\Postman 并回车。

找到更新程序：

进入 app-x.x.x (版本号文件夹) 或者直接在当前目录下寻找名为 Update.exe 的文件。

注意：通常该文件位于 %localappdata%\Postman 根目录下，或者是 packages 文件夹内。

替换/锁定更新程序：

删除 原有的 Update.exe 文件。

新建 一个同名的空文件（例如新建一个文本文档，重命名为 Update.exe，注意要修改后缀名）。

右键点击这个新文件 -> 属性 -> 勾选 “只读” -> 确定。

(可选)：如果看到 Squirrel.exe，也可以对其进行同样的操作。

原理：Postman 启动时会尝试调用 Update.exe。由于把它替换成了假的只读文件，更新进程会启动失败，从而达到禁止更新的目的。