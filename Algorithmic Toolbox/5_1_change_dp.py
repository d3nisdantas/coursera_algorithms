# Uses python3
import sys

def get_change(money):
    #write your code here
    numCoins = [0] * 5 #possible coins: 1, 3, 4
    myCoins = [1, 3, 4]

    for m in range(1, money + 1):
        minCoins = 1000
        for coin in [1, 3, 4]:
            if m >= coin:
                if minCoins > numCoins[(m - coin) % (len(numCoins))] + 1:
                    minCoins = numCoins[(m - coin) % (len(numCoins))] + 1

        numCoins[m%len(numCoins)] = minCoins


    return minCoins

if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
