# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

coins = [1,2,5]
amount = 5

# with recursion
total_recursion_moves = 0
def combinations_with_recursion(coins,amount,coins_str):
    global total_recursion_moves 
    total_recursion_moves +=1
    if amount<0:
        return 
    if amount==0:
        return [coins_str]
    total_ways = []
    for i in coins:
        ans = combinations_with_recursion(coins,amount-i,coins_str+[str(i)])
        if ans:

            for i in ans:
                i.sort()
                if i not in total_ways:
                    total_ways.append(i)
    return total_ways
print(f"Ans is {len(combinations_with_recursion(coins,amount,[]))} with total moves in recursion {total_recursion_moves}")

# with dp
total_dp_moves = 0
def combinations_with_dp(coins,amount):
    global total_dp_moves
    dp = [0 for i in range(amount+1)]
    dp[0]=1
    for coin in coins:
        for i in range(coin,len(dp)):
            total_dp_moves+=1
            if i-coin>=0:
                dp[i] = dp[i-coin] + dp[i]

    return dp[-1]
print(f"Ans is {combinations_with_dp(coins,amount)} with total moves in dp {total_dp_moves}")

