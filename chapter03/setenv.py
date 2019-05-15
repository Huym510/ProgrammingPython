import os


print('setenv...', end='')
print(os.environ['USER'])  # 输出当前shell的变量值

os.environ['USER'] = 'Brian'    # 在后台运行os.putenv
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'   # 传递更新值到衍生程序
os.system('python echoenv.py')  # 链接的c语言库模块

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())
