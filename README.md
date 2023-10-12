# CCPackage

CCPackage是一个打包工具，它采用读取当前运行环境数据并自动解密的方式，以此保护用户在某些可能被内容审查的网盘中的内容。它可以加密并防止网盘运营商删除用户的文件。

## 可选输入参数
|数据|变量|示例|
|----|----|----|
|当前目录的一个文件名|filename|default|
## 可用输出参数
|数据|变量|示例|加密计算优先级|命令行代号|
|----|----|----|----|----|
|操作系统|os_type|Linux|1|o|
|时区|current_timezone|+0000|2|z|
|日期|current_date|2222-12-12|3|d|
|时间|current_time|22:22|4|t|
|主机名|hostname|PC-Work|5|h|
|MAC地址|mac_address|00:FF:FF:FF:FF:FF|6|m|
|当前目录名|folder_name|Work_Folder|7|n|
|文件是否存在|file_exists|True|8|f|

## 如何打包成自解包执行文件
1. 打开命令行，浏览到`CCPackage`根目录下
2. 启用虚拟环境 (VENV) （如果有的话）
3. 运行`python Encryption.py -encrypt {你要的加密参数}`来建立加密的文件
4. 运行`python package_poc.py`
5. 当询问文件路径时，输入**被加密的文件的文件名或路径**，被加密的文件都带着`.enc`文件扩展名，比如`00015.png.enc`
6. 在新出现的dist目录下就是自解包执行文件，默认名字为`PackageDecryptionRoutine.exe`，推荐改掉文件名，不过是可选的
7. 可以直接执行该文件，程序会自动解密可执行文件内部的加密包，并且输出到当前目录，带着原文件的文件名