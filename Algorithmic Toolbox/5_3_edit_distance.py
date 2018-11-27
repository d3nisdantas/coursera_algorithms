# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    #T = [[0] * (len(s)+1) for _ in range(len(t)+1)]
    # string s correspond to columns, t correspond to rows
    T = np.zeros([len(t)+1, len(s)+1], dtype=int)
    # fill up first row and column from [0 .. lengthOfWord]
    T[:, 0] = np.linspace(0, len(t), len(t)+1)
    T[0, :] = np.linspace(0, len(s), len(s)+1)

    for i in range(1, len(T)): #rows
        for j in range(1, len(T[0])): #columns
            diff = 1 if s[j-1] != t[i-1] else 0
            T[i][j] = min(T[i-1][j] + 1, T[i][j-1] + 1, T[i-1][j-1] + diff)

    return T[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
