# 导入库
from get_info import *
import argparse
import sys
import hashlib
from Crypto.Cipher import AES

# 清空临时文件
clear_file = open("temp.tmp", "w")
clear_file.close()

print("Get System Information\n")
print("|OS_TYPE:", os_type)
print("|TIMEZONE:", current_timezone)
print("|DATE:", current_date)
print("|TIME:", current_time)
print("|HOSTNAME:", hostname)
print("|MAC_ADDRESS:", mac_address)
print("|FOLDER_NAME:", folder_name)
print("|FILE_EXISTS:", file_exists, "\n")
# 命令行介绍
parser = argparse.ArgumentParser(description="CCPackage is a packaging tool that reads current runtime environment data and automatically decrypts it in order to protect users' content on certain cloud storage platforms where content censorship is possible. It encrypts and prevents cloud storage operators from deleting user files.")
# 自定义一个验证函数，检查输入字符串是否包含允许的字符


def validate_encrypt(value):
    allowed_chars = set('ozdthmnf')
    if any(char not in allowed_chars for char in value):
        raise argparse.ArgumentTypeError(
            f'Invalid characters in -encrypt argument')
    return value


parser = argparse.ArgumentParser(description='My Python App')

# 添加命令行参数，并指定验证函数
parser.add_argument('-encrypt', nargs='?', const=True, metavar='string',
                    help='encrypt parameters', type=validate_encrypt)

args = parser.parse_args()

# 判断是否输入了参数
if args.encrypt:
    encrypt_value = args.encrypt
else:
    encrypt_value = None
    print("\n No Encryption Mode,Exit \n ")
    sys.exit()


File_name_input = input(
    "Enter The File Name You Want To Encrypt.\n File name:")
print("\n")
Encryption_Mode = encrypt_value
# 寻找的字符串列表
target_strings = ["o", "z", "d", "t", "h", "m", "n", "f"]
# 创建一个字典，用于存储字符串
string_bool_map = {
    "o": "os_type",
    "z": "current_timezone",
    "d": "current_date",
    "t": "current_time",
    "h": "hostname",
    "m": "mac_address",
    "n": "folder_name",
    "f": "file_exists"
}
# 创建一个空列表用于存储匹配的结果
result = []
# 预处理变量
o_exists = False
z_exists = False
d_exists = False
t_exists = False
h_exists = False
m_exists = False
n_exists = False
f_exists = False
# 遍历目标字符串列表
for target in target_strings:
   # 检查目标字符串是否存在
    if target in Encryption_Mode:
        # 获取对应的布尔值，并添加到结果列表中
        result.append(string_bool_map.get(target))
        locals()[f"{target}_exists"] = string_bool_map.get(target)
        exec(f"{target}_exists = True")
# 输出结果
print("Encryption Information:")
print("|OS_TYPE:", o_exists)
print("|TIMEZONE:", z_exists)
print("|DATE:", d_exists)
print("|TIME:", t_exists)
print("|HOSTNAME:", h_exists)
print("|MAC_ADDRESS:", m_exists)
print("|FOLDER_NAME:", n_exists)
print("|FILE_EXISTS:", f_exists, "\n")
print("|ENCRYPT_MODE:", result, "\n")
print("Starting Encrypting Program...\n")

pre_encrypt_info = ""
Separator = "X"

if o_exists:
    # 执行o_exists为True时的代码块
    pre_encrypt_info = os_type
    pass

if z_exists:
    # 执行z_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + current_timezone
    pass

if d_exists:
    # 执行d_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + current_date
    pass

if t_exists:
    # 执行t_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + current_time
    pass

if h_exists:
    # 执行h_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + hostname
    pass

if m_exists:
    # 执行m_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + mac_address
    pass

if n_exists:
    # 执行n_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + folder_name
    pass

if f_exists:
    # 执行f_exists为True时的代码块
    pre_encrypt_info = pre_encrypt_info + Separator + file_exists
    pass

print("Pre_Encrypt_Info:",pre_encrypt_info)


# 创建一个SHA-256哈希对象
hash_object = hashlib.sha256()
# 将字符串编码为字节字符串
input_bytes = pre_encrypt_info.encode("utf-8")
# 更新哈希对象的输入数据
hash_object.update(input_bytes)
# 获取SHA-256哈希值
sha256_hash = hash_object.hexdigest()

print("Hash:",sha256_hash)

def encrypt_file(filename, password):
    with open(filename, 'rb') as file:
        plaintext = file.read()

    cipher = AES.new(password, AES.MODE_EAX)
    nonce = cipher.nonce

    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # 以同样的文件名加上 .enc 后缀保存加密后的文件
    encrypted_filename = filename + '.enc'
    with open(encrypted_filename, 'wb') as file:
        [file.write(x) for x in (nonce, tag, ciphertext)]

    print("文件加密完成！加密文件名为:", encrypted_filename)

# 调用函数进行加密
filename = File_name_input
passwd = sha256_hash
encrypt_file(filename, passwd)