import math

a = int(input('a: '))
b = int(input('b: '))
x = int(input('x: '))
y = int(input('y: '))
res = 0


def diagonal():
    global x, y, res
    gcd = math.gcd(x, y)
    x /= gcd
    y /= gcd
    res = min(a/x, b/y)


def output():
    print(f"{int(res*x)} {int(res*y)}")


def main():
    diagonal()
    output()


main()
