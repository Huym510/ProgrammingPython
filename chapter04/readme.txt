chapter04-文件和目录工具

1. 'w'模式打开文件时，如果文件不存在，python会创建这个文件；如果文件已经存在，那么它会清除文件的当前内容

2. 无论语句是否发生异常，确保文件能够顺利关闭，有两种方法：
   第一种：with open(filename, 'w') as my_file:
                ...process my_file...
   第二种：try:
               ...process my_file...
          finally:
                my_file.close()
   with仅应用于上下文管理器协议的对象，try/finally允许任意异常情况下的任意退出操作

3. file.read()
        返回一个字符串，包含保存在文件中的所有字符
   file.read(N)
        返回一个字符串，包含文件中接下来的N个字符
   file.readline()
        读取下一个\n之前的内容，并返回一个行字符串
   file.readlines()
        读取整个文件并返回一个行字符串列表


