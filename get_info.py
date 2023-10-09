import uuid
import os
import platform
import socket
from datetime import datetime
from dateutil.tz import tzlocal

# 获取当前时区
pre_current_timezone = datetime.now(tzlocal()).strftime('%z')
current_timezone = (f"{pre_current_timezone}")
# 获取当前日期
pre_current_date = datetime.now().strftime('%Y-%m-%d')
current_date = (f"{pre_current_date}")
# 获取当前时间
pre_current_time = datetime.now().strftime('%H:%M')
current_time = (f"{pre_current_time}")
# 获取计算机名称
hostname = socket.gethostname()
# 获取mac地址
mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac_address = ":".join([mac[i:i+2] for i in range(0, 12, 2)])
# 获取当前目录名称
current_dir = os.getcwd()
folder_name = os.path.basename(current_dir)
# 获取操作系统平台类型
os_type = platform.system()
# 获取当前目录
current_directory = os.getcwd()
# 检查特定文件是否存在
filename = "default"
file_exists = os.path.isfile(os.path.join(current_directory, filename))
# 根据文件是否存在，改变file_exists的值
if file_exists:
    file_exists = "File_Exists"
else:
    file_exists = "File_NotExists"