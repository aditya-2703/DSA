# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

cost = [10,15,20]

# with recursion
total_recursion_moves = 0
def most_cost_cs(cost,i,n,total_cost):
    global total_recursion_moves
    total_recursion_moves+=1
    if i>n:
        return 999999
    if i==n:
        return total_cost
    else:
        cost1 = most_cost_cs(cost,i+1,n,total_cost+cost[i])
        cost2 = most_cost_cs(cost,i+2,n,total_cost+cost[i])
        min_cost = min(cost1,cost2)
        return min_cost

ans = min(most_cost_cs(cost,0,len(cost),0),most_cost_cs(cost,1,len(cost),0))
print(f"Ans is {ans} in total recursion moves of {total_recursion_moves}")
 

# with dp
total_dp_moves = 0
def most_cost_dp(cost):
    global total_dp_moves
    dp=[0]*(len(cost)+1)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2,len(cost)):
        total_dp_moves+=1
        min_cost = min(dp[i-1],dp[i-2])
        total_cost = cost[i]+min_cost
        dp[i] = total_cost

    dp[-1] = min(dp[-2],dp[-3])
    return dp[-1]

print(f"Ans is {most_cost_dp(cost)} in total recursion moves of {total_dp_moves}")

