# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    i = 1
    while n > 0:
        if i <= n and (i + 1 <= n - i or n - i == 0):
            summands.append(i)
            n -= i
        # else:
            # n += summands.pop()
        i += 1


    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
