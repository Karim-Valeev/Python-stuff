def printer(str, num):
    print(dir(num), '\n')
    print(dir(str), '\n')
    str = str.lower()
    print(dir(str), '\n')
    print(str)


printer("Hello world!", 1)
