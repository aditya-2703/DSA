# 1. You are given a number n, representing the count of coins.
# 2. You are given n numbers, representing the denominations of n coins.
# 3. You are given a number "amt".
# 4. You are required to calculate and print the number of permutations of the n coins using which the 
#      amount "amt" can be paid.

# Note1 -> You have an infinite supply of each coin denomination i.e. same coin denomination can be 
#                   used for many installments in payment of "amt"
# Note2 -> You are required to find the count of permutations and not combinations i.e.
#                   2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same 
#                   combination. You should treat them as 3 and not 1.

# Sample Input
# coins =[4,2,3,5,6]
# amount = 7
# Sample Output
# 5

coins =[2,3,5,6]
amount = 7

# with recursoin
total_recursion_moves = 0
def permutations_with_recursion(coins,amount,coins_str):
    global total_recursion_moves 
    total_recursion_moves +=1
    if amount<0:
        return 
    if amount==0:
        return [coins_str]
    total_ways = []
    for i in coins:
        ans = permutations_with_recursion(coins,amount-i,coins_str+[str(i)])
        if ans:
            for i in ans:
                total_ways.append(i)
    return total_ways
print(f"Ans is {len(permutations_with_recursion(coins,amount,[]))} with total moves in recursion {total_recursion_moves}")

# with dp
total_dp_moves = 0
def permutations_with_dp(coins,amount):
    global total_dp_moves
    dp = [0]*(amount+1)
    dp[0]=1
    for i in range(len(dp)):
        for coin in coins:
            total_dp_moves+=1
            if i>=coin:
                if i-coin>=0:
                    dp[i]+=dp[i-coin]
    return dp[-1]
print(f"Ans is {permutations_with_dp(coins,amount)} with total moves in dp {total_dp_moves}")
