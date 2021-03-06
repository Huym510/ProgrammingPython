'''自定义分页脚本'''


def more(text, numlines=15):
    lines = text.splitlines()  # 效果等同于split('\n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y', 'Y']: break


if __name__ == '__main__':
    import sys


    # more(open("./readme.txt").read(), 2)
    more(open(sys.argv[1]).read(), 10)
