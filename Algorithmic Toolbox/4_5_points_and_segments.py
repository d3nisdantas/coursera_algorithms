# Uses python3
import sys
import random

def binary_search(a, low, high, key, type):
    if high < low:
        return low - 1
    mid = (low + (high - low)//2)

    # if key == a[mid]:
    #     return mid
    if key < a[mid]:
        return binary_search(a, low, mid - 1, key, type)
    elif key > a[mid]:
        return binary_search(a, mid + 1, high, key, type)
    elif type == 0:
        #the search ends up returning the index corresponding to the
        #last equal element
        return binary_search(a, mid + 1, high, key, type)
    else: #type == 1
        #the search ends up returning the index corresponding to the
        #first equal element

        return binary_search(a, low, mid - 1, key, type)


def fast_count_segments(starts, ends, points):
    # algorithm based on: n(A U B) = n(A) + n(B) - n(A intersection B)
    cnt = [0] * len(points)
    #write your code here
    starts.sort()
    ends.sort()
    i  = 0
    numOfSegments = len(starts)
    for p in points:
        smaller_equal = binary_search(starts, 0, numOfSegments-1, p, 0) + 1
        bigger_equal = numOfSegments - (binary_search(ends, 0, numOfSegments-1, p, 1) + 1)
        cnt[i] = (smaller_equal + bigger_equal) - numOfSegments
        i += 1

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

    #test code
    # p = random.randint(1, 20)
    # p = 20
    # random.seed(1)
    # while True:
    #     s = random.randint(2, 20)
    #     points = [random.randint(0, 20) for _ in range(p)]
    #     segments = [random.randint(0, 20) for _ in range(2*s)]
    #     # segments = [segments[:s], segments[s:2*s-1]]
    #
    #     starts = [0]*s
    #     ends = [0]*s
    #
    #     for i in range(s):
    #         if segments[2*i] <= segments[2*i + 1]:
    #             starts[i] = segments[2*i]
    #             ends[i] = segments[2*i + 1]
    #         else:
    #             starts[i] = segments[2*i + 1]
    #             ends[i] = segments[2*i]
    #
    #     cnt1 = fast_count_segments(starts, ends, points)
    #     cnt2 = naive_count_segments(starts, ends, points)
    #
    #     for i in range(len(cnt1)):
    #         if cnt1[i] != cnt2[i]:
    #             print(p[i])
    #             print(starts)
    #             print(ends)

