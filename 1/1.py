n = int(input('Общее кол-во изделий: '))
m = int(input('Кол-во бракованных изделий: '))
arr = []


def marriage():
    for i in range(m):
        r = int(input('Номер изделия: '))
        arr.append(r)
        arr.sort()


def output():
    print(*arr, sep=',')


def main():
    marriage()
    output()


main()
