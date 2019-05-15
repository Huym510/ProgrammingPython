def interact():
    print('welcome to stream world!')
    while True:
        try:
            reply = input('Enter a number:')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d 的平方是 %d" % (num, num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()