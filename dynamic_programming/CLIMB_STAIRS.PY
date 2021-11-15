# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 or 3 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

n=20

total_moves_for_recursion = 0

# recursion
def qn_with_recursion(n):
    global total_moves_for_recursion
    if n<0:
        return 0
    if n==0:
        return 1

    total_moves_for_recursion+=1
    num1 = qn_with_recursion(n-1)
    num2 = qn_with_recursion(n-2)
    num3 = qn_with_recursion(n-3)

    return num1+num2+num3

print(qn_with_recursion(n))


total_moves_for_dp = 0
# dp 
def qn_with_dp(n,dp):
    global total_moves_for_dp
    if n<0:
        return 0
    if n==0:
        return 1 
    if dp[n]:
        return dp[n]
    
    total_moves_for_dp+=1
    num1 = qn_with_dp(n-1,dp)
    num2 = qn_with_dp(n-2,dp)
    num3 = qn_with_dp(n-3,dp)

    total = num1+num2+num3 
    dp[n]=total

    return total


print(qn_with_dp(n,[None]*(n+1)))

print(f"total moves for recursion is {total_moves_for_recursion} and total moves for dp is {total_moves_for_dp}")