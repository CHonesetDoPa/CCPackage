# CCPackage

CCPackage是一个打包工具，它采用读取当前运行环境数据并自动解密的方式，以此保护用户在某些可能被内容审查的网盘中的内容。它可以加密并防止网盘运营商删除用户的文件。

## 可选输入参数
|数据|变量|示例|
|----|----|----|
|当前目录的一个文件名|filename|default|
## 可用输出参数
|数据|变量|示例|
|----|----|----|
|操作系统|os_type|Linux|
|时区|current_timezone|+0000|
|日期|current_date|2222-12-12|
|时间|current_time|22:22|
|主机名|hostname|PC-Work|
|MAC地址|mac_address|00:FF:FF:FF:FF:FF|
|当前目录名|folder_name|Work_Folder|
|文件是否存在|file_exists|True|