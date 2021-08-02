# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for all n days. 
# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.
# Example 1:
# Input: 
# N = 7, price[] = [100 80 60 70 60 75 85]
# Output:
# 1 1 1 2 1 4 6
# Explanation:
# Traversing the given input span for 100 
# will be 1, 80 is smaller than 100 so the 
# span is 1, 60 is smaller than 80 so the 
# span is 1, 70 is greater than 60 so the 
# span is 2 and so on. Hence the output will 
# be 1 1 1 2 1 4 6.

# METHOD 1 TAKES O(N) TIME AND O(N) SPACE COMPLEXTIY
# HERE WE USE SAME APPROACH LIKE NEXT GREATER ELEMENT
# POP
# ANSWER
# PUSH
# WILL POP UNTILL LARGER ELEMENT COMPARE TO CURRENT ELEMENT ELSE WILL PUSH


def Method_1(arr):
    stack = []
    result = [0]*len(arr)
    result[0] = 0+1
    stack.append(0)
    for i in range(len(arr)):
        # pop till we find greater than curr
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()        
        # there is two condition after while 
        # stack is empty
        # stack is not empty
        # if stack is empty then index+1 is answer
        if not stack:
            result[i]=i+1
        # if stack is not empty then answer = current - top_of_stack
        else:
            result[i] = i - stack[-1]
        # will push all the time 
        stack.append(i)
    print(result)


if __name__ == '__main__':
    N=7
    price = [100 ,80, 60, 70, 60, 75, 85]
    Method_1(price)
    