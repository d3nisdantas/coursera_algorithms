#Uses python3
import numpy as np

import sys

def lcs2(a, b):
    #write your code here
    T = np.zeros([len(b), len(a)], dtype=int)
    # fill up first row and column from [0 .. lengthOfWord]

    longgest = 0
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                maxSeq = 1
                for k in range(i - 1, -1, -1):
                    if a[k] < a[i]:

                        # check on column k from row j-1 until 0 if there's already a maxSeq > 1
                        for l in range(j - 1, -1, -1):
                            if T[l][k] > 0:
                                #the first T > 0 found should be the largest
                                maxSeq = T[l][k] + 1 if T[l][k] + 1 > maxSeq else maxSeq
                                break

                T[j][i] = maxSeq if maxSeq > T[j][i] else T[j][i]
                longgest = T[j][i] if T[j][i] > longgest else longgest

    return longgest

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
