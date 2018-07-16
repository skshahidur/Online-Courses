# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0000
    # write your code here
    valueElement = [(round(j/i,4),i) for i,j in zip(weights, values)]
    valueElement.sort(key = lambda x: x[0], reverse=True)
    for k in range(len(valueElement)):
        i,j = valueElement[k]
        a = min(j, capacity)
        value = value + round(a*i,4)
        if capacity>0:
            capacity = capacity - a
        else : 
            break
    return round(value,4)



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))



#get_optimal_value(31, [53,22,37], [111,67,123])


