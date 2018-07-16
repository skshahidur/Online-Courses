# Uses python3
import sys

# =============================================================================
# class moneyChange(object):
#     
#     def __init__(self, value, den1=1, den2=5, den3=10):
#         self.den1 = den1
#         self.den2 = den2
#         self.den3 = den3
#         self.value = value
#         
#     def getNumber(self):
#         sortedDen = sorted([self.den1, self.den2, self.den3])
#         biggest = sortedDen[2]
#         second = sortedDen[1]
#         coinsRequired = 0
#         coinsRequired = coinsRequired + self.value//biggest
#         rem1 = self.value%biggest
#         if rem1 != 0:
#             coinsRequired = coinsRequired + rem1//second
#             rem2 = rem1%second
#             coinsRequired = coinsRequired + rem2
#         return(coinsRequired)
# 
# def get_change(m):
#     #write your code here
#     moneyChangeValue = moneyChange(m)
#     n = moneyChangeValue.getNumber()
#     return n
# =============================================================================

def get_change(m):
     #write your code here
     coinsRequired = 0
     coinsRequired = coinsRequired + m//10
     rem1 = m%10
     if rem1 != 0:
         coinsRequired = coinsRequired + rem1//5
         rem2 = rem1%5
         coinsRequired = coinsRequired + rem2
     return coinsRequired

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))








