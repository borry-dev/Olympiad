n = int(input())
res = 0


def calculation():
    global res, n
    if n >= 3:
        t = n//3

        res = str(7)*int(t)
        n -= t*3
        if n == 2:
            res += "1"
    elif n == 2:
        res = 1


def output():
    print(int(res))


def main():
    calculation()
    output()


main()
