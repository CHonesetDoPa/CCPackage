# 导入库 
from get_info import *

# 清空临时文件
# 打开文件
clear_file = open("temp.tmp", "w")
# 关闭文件
clear_file.close()

print(current_timezone)
print(current_date)
print(current_time)
print(hostname)
print(mac_address)
print(folder_name)
print(os_type)
print(file_exists)