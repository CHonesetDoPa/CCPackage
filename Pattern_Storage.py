def Pattern_Storage(_Pattern_Storage_):
    # 创建并打开一个新文件进行写入
    with open('Encryption_Mode', 'w') as file:
    # 写入内容到文件中
        file.write(_Pattern_Storage_)
        print("Encryption_Mode Writted.")