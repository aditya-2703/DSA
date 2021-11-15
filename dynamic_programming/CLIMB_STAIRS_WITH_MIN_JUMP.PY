# 1. You are given a number n, representing the number of stairs in a staircase.
# 2. You are on the 0th step and are required to climb to the top.
# 3. You are given n numbers, where ith element's value represents - till how far from the step you 
#      could jump to in a single move.  You can of-course fewer number of steps in the move.
# 4. You are required to print the number of minimum moves in which you can reach the top of 
#      staircase.
# Note -> If there is no path through the staircase print null.
# Input Format
# A number n
# .. n more elements
# 10
# 3
# 3
# 0
# 2
# 1
# 2
# 4
# 2
# 0
# 0

# Output Format
# A number representing the number of ways to climb the stairs from 0 to top.
# 4

def get_min(arr):
    min_element = 99999
    for i in arr:
        if i!=None:
            min_element = min(i,min_element)
    return min_element if min_element!=99999 else None
def qn_with_dp(arr,dp):
    dp[-1]=0
    for i in reversed(range(len(arr))):
        if arr[i]>0:
            min_element = 9999
            for j in range(1,arr[i]+1):
                # if i+j<len(dp):
                if dp[i+j]!=None:
                    min_element = min(dp[i+j],min_element)
            if min_element!=9999:
                dp[i] = 1+min_element
    return dp[0]

arr = [3,3,0,2,1,2,4,2,0,0]
n= len(arr)
print(qn_with_dp(arr,[None]*(n+1)))