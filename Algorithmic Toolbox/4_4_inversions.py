# Uses python3
import sys

def merge(a, b):
    c = [0]*(len(a)+len(b))
    total = i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c[k] = a[i]
            k += 1
            i += 1
        else:
            c[k] = b[j]
            k += 1
            j += 1
            total += len(a) - i

    if i < len(a):
        c[k:] = a[i:]
    elif j < len(b):
        c[k:] = b[j:]

    return [c, total]

def merge_and_sort(a):
    if len(a) <= 1:
        return [a, 0]
    mid = len(a)//2
    L = a[:mid]
    R = a[mid:]

    [L_, total1] = merge_and_sort(L)
    [R_, total2] = merge_and_sort(R)

    [a, total3] = merge(L_,R_)
    total = total1 + total2 + total3

    return [a, total]

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    [c, total] = merge(a, b, left, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    [_, num] = merge_and_sort(a)

    print(num)
