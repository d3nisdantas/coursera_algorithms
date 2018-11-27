# Uses python3
import sys

def optimal_sequence(n):
    numOperations = [0]*(n+1)
    prev = [-1]*(n+1)
    sequence = []

    numOperations[1] = 0
    prev[1] = 0

    for num in range(2, n+1):
        numOperations[num] = numOperations[num - 1] + 1
        prev[num] = num - 1
        if num % 3 == 0 and numOperations[num // 3] + 1 < numOperations[num]:
                numOperations[num] = numOperations[num // 3] + 1
                prev[num] = num // 3
        if num % 2 == 0 and numOperations[num // 2] + 1 < numOperations[num]:
            numOperations[num] = numOperations[num // 2] + 1
            prev[num] = num // 2

    prevNumIndex = prev[-1]
    sequence.append(n)
    while prevNumIndex > 0:
        sequence.append(prevNumIndex)
        prevNumIndex = prev[prevNumIndex]

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
