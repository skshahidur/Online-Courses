# Uses python3
import sys

def gcd_naive(a, b):
    if a>b:
        c = a%b
        if c == 0:
            return(b)
        else:
            return(gcd_naive(b,c))
    else:
        c = b%a
        if c == 0:
            return(a)
        else:
            return(gcd_naive(a,c))
    
def lcm_naive(a, b):
    a1 = gcd_naive(a,b)
    b1 = int(a/a1)
    b2 = int(b/a1)
    return((a1*b1*b2))
    

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


