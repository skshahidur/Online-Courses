# Uses python3
## Exponential order
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

## order n but with dictionary approach
def fibOptimized(m):
    myDictionary = dict()
    myDictionary.update({0:0})
    myDictionary.update({1:1})
    print(myDictionary)
    if m in myDictionary.keys():
        print("Found")
        return myDictionary[m]
    else :
        for i in range(m+1):
            if i not in myDictionary.keys():
                myDictionary.update({i:myDictionary[i-1]+myDictionary[i-2]})
                del myDictionary[i-2]
                pass
            pass
        pass
    
    print(myDictionary)
    return myDictionary[m]

fibOptimized(5)

## order n but with list approach
def fibFinalOptimized(m):
    myList = list()
    myList.append(0)
    myList.append(1)
    print(myList)
    
    if m==0:return myList[0]
    if m==1:return myList[1]
    
    for i in range(2,m+1):
        myList.append(myList[0] + myList[1])
        del myList[0]
        print(myList)
    
    return myList[1]

print(fibFinalOptimized(10))
