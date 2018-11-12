# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda x: x[0])

    i = 0
    while i < len(segments):
        firstPoint = segments[i][0]
        lastPoint = segments[i][1]
        j = i + 1
        while j < len(segments):
            if segments[j][0] >= firstPoint and segments[j][0] <= lastPoint:
                firstPoint = segments[j][0]
                lastPoint = min(lastPoint, segments[j][1])
                j += 1
            else:
                break
        points.append(firstPoint)
        i = j
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')