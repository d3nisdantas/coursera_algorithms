# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    index = 1

    for i in range(2, n):
        if numbers[i] > numbers[index]:
            index = i

    numbers[index], numbers[n-1] = numbers[n-1], numbers[index]
    index = 1

    for i in range(2, n-1):
        if numbers[i] > numbers[index]:
            index = i

    numbers[index], numbers[n - 2] = numbers[n - 2], numbers[index]

    return numbers[n-1]*numbers[n-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))