import math

n = int(input('Длина брусков: '))
a = int(input('Длина боковых сторон обравления дверей: '))
b = int(input('Длина верхней стороны обравления дверей: '))
res = []


def result():
    square = ((a*2)+b)*2
    i = square/n

    res.append(math.ceil(i))


def output():
    print(res[0])


def main():
    result()
    output()


main()
