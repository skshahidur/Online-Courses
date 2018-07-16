# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    fibDict = {}
    for i in range(n+1):
        if i <= 1:
            fibDict[i] = i
        else:
            fibDict[i] = (fibDict[i-1] + fibDict[i-2])%10
    return(fibDict[n])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
