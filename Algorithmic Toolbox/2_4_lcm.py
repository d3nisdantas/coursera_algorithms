# Uses python3
import sys

def gcd(a, b):
    temp = a % b
    if temp == 0:
        return b

    return gcd(b, temp)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    gcdResult = gcd(max([a, b]), min([a, b]))

    print ( ((a//gcdResult)*b))

