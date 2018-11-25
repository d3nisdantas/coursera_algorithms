# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    list_fib = [0, 1]

    for i in range(n-1):
        #print(current)
        previous, current = current, (previous + current) % m
        list_fib.append(current)

        if previous == 0 and current == 1:
            pisano_period = i+1
            #print(pisano_period)
            #return n % pisano_period
            return list_fib[n % pisano_period]%m

    return current

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
