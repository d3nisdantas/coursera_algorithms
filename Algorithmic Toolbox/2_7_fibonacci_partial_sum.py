# Uses python3
import sys

def fibonacci_sum_modified(prev, curr, m, n):
    if m == n:
        return curr
    previous = prev
    current = curr
    sum = 0
    pisano_array = [current]

    for i in range(n - m):
        previous, current = current, (previous + current) % 10
        sum = (sum + current) % 10
        pisano_array.append(sum)

        if previous == prev and current == curr:
            pisano_period = i + 1
            return pisano_array[n%pisano_period]

    return sum

def fibonacci_sum(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1
    sum      = 1
    pisano_array = [0, 1]

    for i in range(from_ - 1):
        previous, current = current, (previous + current) % 10
        sum = (sum + current) % 10
        pisano_array.append(sum)

        if previous == 0 and current == 1:
            pisano_period = i + 1
            return fibonacci_sum_modified(pisano_array[from_%pisano_period - 1], pisano_array[from_%pisano_period], from_, to)
    return fibonacci_sum_modified(pisano_array[from_ - 2], pisano_array[from_ - 1], from_, to)

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum = (sum + current) % 10
            print(sum, end=" ")
        current, next = next, (current + next) % 10

    return sum


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_sum(from_, to))
    # for i in range(120):
    #     print(fibonacci_partial_sum_naive(i, 2+i), end = " ")
    #     if i == 59:
    #        print("\n")