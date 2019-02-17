#Uses python3
import sys
import math

def calc_distance(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def brute_force_distance(x, y):
    min = sys.float_info.max
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            dist = calc_distance(x[i], y[i], x[j], y[j])
            if dist < min:
                min = dist

    return dist

def strip_closest(strip, d):
    min = d
    strip.sort(key=lambda x:x[1])

    myLen = len(strip)
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < min:
            dist = calc_distance(strip[j][0], strip[j][1], strip[i][0], strip[i][1])
            if dist < min:
                min = dist

            j += 1

    return min

def minimum_distance(x, y):
    #write your code here
    if len(x) <= 3:
        return brute_force_distance(x, y)

    mid = len(x)//2
    d1 = minimum_distance(x[:mid], y[:mid])
    d2 = minimum_distance(x[mid:], y[mid:])

    d = min(d1, d2)

    strip = []
    for i in range(len(x)):
        if abs(x[mid] - x[i]) < d:
            strip.append([x[i], y[i]])

    return min(d, strip_closest(strip, d))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    x, y = zip(*sorted(zip(x, y)))
    print("{0:.9f}".format(minimum_distance(x, y)))
