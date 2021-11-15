# Climb Stairs With Variable Jumps
# 1. You are given a number n, representing the number of stairs in a staircase.
# 2. You are on the 0th step and are required to climb to the top.
# 3. You are given n numbers, where ith element's value represents - till how far from the step you 
#      could jump to in a single move.  
#      You can of course jump fewer number of steps in the move.
# 4. You are required to print the number of different paths via which you can climb to the top.
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
# 5


def qn_with_dp(arr,dp):

    dp[-1]=1
    for i in reversed(range(len(arr))):
        for j in range(1,arr[i]+1):
            if i+j<len(dp):
                if dp[i+j]!=None:
                    dp[i]+=dp[i+j]
    return dp[0]

arr = [3,3,0,2,1,2,4,2,0,0]
n= len(arr)
print(qn_with_dp(arr,[0]*(n+1)))