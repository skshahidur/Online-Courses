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
    

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
