n = int(input())


def calculation():
    global n
    if n % 2 == 0:
        print("1" * (n // 2))
    else:
        print("7" + ((n - 3) // 2) * "1")


def main():
    calculation()

if __name__ == '__main__':
    main()
