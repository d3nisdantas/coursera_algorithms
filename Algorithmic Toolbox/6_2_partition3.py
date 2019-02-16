# Uses python3
import sys
import itertools
import random

def partition31(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def optimal_weight(W, w):
    # write your code here
    # in this problem the proportion value to weight is 1 to 1
    # therefore only array w is necessary
    T = [[[None]*(W+1) for _ in range(len(w)+1)] for _ in range(3)]

    for k in range(3):
        for u in range(W+1):
            T[k][0][u] = 0

    for k in range(3):
        for i in range(1, len(w)+1):
            for u in range(0, W+1):
                T[k][i][u] = T[k][i-1][u]
                if u >= w[i-1]:
                    T[k][i][u] = max(T[k][i][u], T[k][i-1][u - w[i-1]] + w[i-1]) # second w[i-1] corresponds to value
        if k != 2:
            for u in range(W + 1):
                T[k+1][0][u] = T[k][len(w)][u]
            for i in range(len(w)+1):
                T[k+1][i][0] = T[k][i][W]

    return [T[2][len(w)][W], T[1][len(w)][W], T[0][len(w)][W]]

def partition3(A):
    totalValue = sum(A)

    if totalValue % 3 != 0:
        return 0

    sacks = optimal_weight(totalValue//3, A)
    return sum(sacks) == totalValue


if __name__ == '__main__':
    #input = sys.stdin.read()

    random.seed = 1000
#
    A = [None]*18
    while(1):
        n = random.randint(1, 10)
        for i in range(n):
            A[i] = random.randint(1, 30)

    #    n, *A = list(map(int, input.split()))
        A = [15, 26, 1, 16, 20]
        n = len(A)
        if partition3(A[0:n]) != partition31(A[0:n]):
            print(A[0:n])

