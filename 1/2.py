a = input('Введите 1 число: ')
b = input('Введите 2 число: ')


def amount():
    x = a.count('*')+(a.count('.')*1)+(a.count('|')*5)
    y = b.count('*')+(b.count('.')*1)+(b.count('|')*5)
    print(x+y)


def main():
    amount()


if __name__ == '__main__':
    main()
