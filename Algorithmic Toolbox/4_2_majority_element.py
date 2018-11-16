# Uses python3
import sys
import random

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + int((right - left)/2)
    majLeft = get_majority_element(a[left:mid], 0, len(a[left:mid]))
    majRight = get_majority_element(a[mid:right], 0, len(a[mid:right]))

    if majLeft == majRight:
        return majLeft
    if majLeft != -1:
        if a.count(majLeft) > mid:
            return majLeft
    if majRight != -1:
        if a.count(majRight) > mid:
            return majRight

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    #test code
    # n = random.randint(1, 10)
    # n = int(1e5)
    # random.seed(10)
    # while 1:
    #     rep = random.randint(0, 1e9)
    #
    #     a = [rep]*int((n/2)-1) + [random.randint(0, 20) for _ in range(int(n/2)+1)]
    #     random.shuffle(a)
    #
    #     try:
    #         if get_majority_element(a, 0, n) != -1:
    #             print(a)
    #             break
    #     except:
    #         print (a)
    #         break

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
