# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    sorted_list = sorted(zip(weights, values), key=lambda x: -x[1]/x[0])
    totalValue = 0

    for i in range(len(sorted_list)):
        partToTake = min(sorted_list[i][0], capacity)
        capacity -= partToTake
        itemPartValue = partToTake*sorted_list[i][1]/sorted_list[i][0]
        totalValue += itemPartValue

    return totalValue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
