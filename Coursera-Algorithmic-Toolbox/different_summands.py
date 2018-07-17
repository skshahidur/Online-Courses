# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    if n>0:
        summands.append(1)
        n = n-1
        while n >= 1:
            if n>summands[-1]:
                summands.append(summands[-1]+1)
            else: 
                summands[-1] = summands[-1] + n
                break
            n = n - summands[-1]
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')


# =============================================================================
# a = [1,2,3,4]
# a[-1] = a[-1]+1
# 
# 
# s = []
# s.append(s[-1]+1)
# 
# s[]
# 
# optimal_summands(23)
# 
# =============================================================================

