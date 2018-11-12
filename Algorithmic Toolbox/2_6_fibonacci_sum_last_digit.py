# Uses python3
import sys

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    pisano_array = [0, 1]

    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum = (sum + current) % 10
        pisano_array.append(sum)

        if previous == 0 and current == 1:
            pisano_period = i + 1
            return pisano_array[n%pisano_period]
    return sum


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
#    for i in range(120):
#        print(fibonacci_sum_naive(i), end = " ")
#        if i == 59:
#            print("\n")
