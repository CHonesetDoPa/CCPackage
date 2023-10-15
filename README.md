# CCPackage

CCPackage是一个打包工具，它采用读取当前运行环境数据并自动解密的方式，以此保护用户在某些可能被内容审查的网盘中的内容。它可以加密并防止网盘运营商删除用户的文件。

## 可用加密参数
|数据|变量|示例|加密计算优先级|加密参数|
|----|----|----|----|----|
|操作系统|os_type|Linux|1|o|
|时区|current_timezone|+0000|2|z|
|日期|current_date|2222-12-12|3|d|
|时间|current_time|22:22|4|t|
|主机名|hostname|PC-Work|5|h|
|MAC地址|mac_address|00:FF:FF:FF:FF:FF|6|m|
|当前目录名|folder_name|Work_Folder|7|n|
|"default"文件是否存在|file_exists|File_Exists|8|f|

# 使用CCPackage
#### 按照系统版本下载适合你的二进制文件
|文件名称|系统版本|作用|链接|
|----|----|----|----|
|CPK_Encrypt.exe|Windows|加密一个文件|[CPK_Encrypt.exe](https://github.com/CHonesetDoPa/CCPackage/releases/download/Ver1.0/CPK_Encrypt.exe)|
|CPK_Package.exe|Windows|打包加密好的文件|[CPK_Package.exe](https://github.com/CHonesetDoPa/CCPackage/releases/download/Ver1.0/CPK_Package.exe)|
|CPK_Encrypt.run|Linux|加密一个文件|[CPK_Encrypt.run](https://github.com/CHonesetDoPa/CCPackage/releases/download/Ver1.0/CPK_Encrypt.run)|
|CPK_Package.run|Linux|打包加密好的文件|[CPK_Package.run](https://github.com/CHonesetDoPa/CCPackage/releases/download/Ver1.0/CPK_Package.run)|

#### 加密并打包一个文件 (Windows环境下)
1. 打开命令行，浏览到你下载CCPackage的文件夹下
2. 运行 `CPK_Encrypt.exe -encrypt {你要的加密参数(ozdthmnf)}`来建立加密的文件
3. 当询问文件路径时，输入**需要加密的文件的文件名或路径**，被加密的文件后都带着`.enc`文件扩展名，比如`00015.png.enc`
4. 运行 `CPK_Package.exe`来建立加密的文件，当询问文件路径时，输入**被加密的文件的文件名或路径**，被加密的文件后都带着`.enc`文件扩展名，比如`00015.png.enc`
5. 在新出现的dist目录下就是自解包执行文件，默认名字为`PackageDecryptionRoutine.exe`，推荐更改文件名为其他值

#### 加密并打包一个文件 (Linux环境下)(Ubuntu22.04LTS下可用，其他系统未经过测试)
1. 打开命令行，浏览到你下载CCPackage的文件夹下
2. 给`CPK_Encrypt.run`和`CPK_Package.run`执行权限  
    > chmod +x CPK_Encrypt.run  
    > chmod +x CPK_Package.run
3. 运行 `CPK_Encrypt.run -encrypt {你要的加密参数(ozdthmnf)}`来建立加密的文件
4. 当询问文件路径时，输入**需要加密的文件的文件名或路径**，被加密的文件后都带着`.enc`文件扩展名，比如`00015.png.enc`
5. 运行 `CPK_Package.run`来建立加密的文件，当询问文件路径时，输入**被加密的文件的文件名或路径**，被加密的文件后都带着`.enc`文件扩展名，比如`00015.png.enc`
6. 在新出现的dist目录下就是自解包执行文件，默认名字为`PackageDecryptionRoutine.exe`，推荐更改文件名为其他值

# 源码安装
## 所需环境/软件
0. git(用于拉取本软件)
1. Python 3.10或以上(推荐3.10，其他版本可能会出现无法预料的问题)  
2. pip或anaconda  
## 如何源码安装使用CCPackage(通过pip)
1. 打开终端，克隆本仓库并进入CCPackage文件夹
2. 运行`pip install -r requirement.txt` 来安装依赖包
3. 运行`python Encryption.py -encrypt {你要的加密参数}`来建立加密的文件
4. 运行`python package_poc.py`
5. 当询问文件路径时，输入**被加密的文件的文件名或路径**，被加密的文件都带着`.enc`文件扩展名，比如`00015.png.enc`
6. 在新出现的dist目录下就是自解包执行文件，默认名字为`PackageDecryptionRoutine.exe`，推荐改掉文件名，不过是可选的
7. 可以直接执行该文件，程序会自动解密可执行文件内部的加密包，并且输出到当前目录，带着原文件的文件名
## 如何源码安装使用CCpackage(通过anaconda)
1. 打开终端，克隆本仓库并进入CCPackage文件夹
2. 运行`conda create --name myenv`和`conda activate myenv`来创建conda环境并激活
3. 运行`conda install --file package.txt`来安装依赖包
4. 运行`python Encryption.py -encrypt {你要的加密参数}`来建立加密的文件
5. 运行`python package_poc.py`
6. 当询问文件路径时，输入**被加密的文件的文件名或路径**，被加密的文件都带着`.enc`文件扩展名，比如`00015.png.enc`
7. 在新出现的dist目录下就是自解包执行文件，默认名字为`PackageDecryptionRoutine.exe`，推荐改掉文件名，不过是可选的
8. 可以直接执行该文件，程序会自动解密可执行文件内部的加密包，并且输出到当前目录，带着原文件的文件名

# 许可证 
[Unlicense license](https://unlicense.org/) 
# 致谢 
[QTnull](https://github.com/qtnull)