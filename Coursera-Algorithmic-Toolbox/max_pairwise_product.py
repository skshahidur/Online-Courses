# python3


def max_pairwise_product(numbers):
    
    firstMax = max(numbers)
    allIndex = [i for i,j in enumerate(numbers) if j == firstMax]
    
    if len(allIndex)>1:
        return(firstMax*firstMax)
    else :
        numbers.remove(firstMax)
        secondMax = max(numbers)
        return(firstMax*secondMax)
        
# =============================================================================
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                               numbers[first] * numbers[second])
# 
# =============================================================================
    

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))



