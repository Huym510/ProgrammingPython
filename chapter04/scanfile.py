def scanner(name, function):
    file = open(name, 'r')  # 创建文件对象
    while True:
        line = file.readline()
        if not line:    # 判断是都到文件末尾
            break
        function(line)  # 调用函数
    file.close()
