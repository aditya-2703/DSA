# Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

# Example 1:
# Input:
# N = 6
# arr[] = [3, 34, 4, 12, 5, 2]
# sum = 9
# Output: 1 
# Explanation: Here there exists a subset with
# sum = 9, 4+3+2 = 9.
# Example 2:
# Input:
# N = 6
# arr[] = [3, 34, 4, 12, 5, 2]
# sum = 30
# Output: 0 
# Explanation: There is no subset with sum 30.



arr = [3, 34, 4, 12, 5, 2, 24, 2, 2, 23, 2, 42, 45, 2, 5, 35]
target_sum = 25


# with recursion
total_recursion_moves = 0
def is_target_sum(arr,target_sum):
    global total_recursion_moves
    total_recursion_moves+=1
    if target_sum<0 or not arr:
        return 
    if target_sum==0:
        return True
    first = arr[0]
    rest = arr[1:]
    taken = is_target_sum(rest,target_sum-first)
    not_taken = is_target_sum(rest,target_sum)
    if taken or not_taken:
        return True
    return False
print(f"Ans is {is_target_sum(arr,target_sum)} with total moves in recursion {total_recursion_moves}")


# with dp
total_dp_moves = 0
def is_target_sum_dp(arr,target_sum):
    global total_dp_moves
    
    dp = [[False for i in range((target_sum+1))]for i in range(len(arr))] 
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            total_dp_moves+=1
            if j==0:
                dp[i][j]=True
            if i==0:
                if arr[i] == j:
                    dp[i][j]=True
            else:
                if arr[i]<j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
                if arr[i]==j:
                    dp[i][j]=True
                if arr[i]>j:
                    dp[i][j] = dp[i-1][j] 
    return dp[-1][-1]
print(f"Ans is {is_target_sum_dp(arr,target_sum)} with total moves in dp {total_dp_moves}")
