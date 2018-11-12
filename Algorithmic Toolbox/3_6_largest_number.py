#Uses python3

import sys

def joinNum(a, b):
    return int(str(a)+str(b))

def largest_number(a):
    #write your code here
    for i in range(1,len(a)):
        key = a[i]

        j = i-1
        while j >= 0 and joinNum(a[j], key) < joinNum(key, a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

    return "".join(a)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
