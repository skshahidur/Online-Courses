# Uses python3
def calc_fib(n):
    fibDict = {}
    for i in range(n+1):
        if i <= 1:
            fibDict[i] = i
        else:
            fibDict[i] = fibDict[i-1] + fibDict[i-2]
    return(fibDict[n])

n = int(input())
print(calc_fib(n))
