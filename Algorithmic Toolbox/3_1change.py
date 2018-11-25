# Uses python3
import sys


def get_change(m):
    coinCount = 0
    coinList = [10, 5, 1]

    for i in range(len(coinList)):
        while m - coinList[i] >= 0:
            m -= coinList[i]
            coinCount += 1

    return coinCount

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
