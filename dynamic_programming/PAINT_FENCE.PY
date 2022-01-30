# Painting Fence 

# Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. Since answer can be large return it modulo 10^9 + 7.
# Examples:

# Input : n = 2 k = 4
# Output : 16
# We have 4 colors and 2 posts.
# Ways when both posts have same color : 4 
# Ways when both posts have diff color :
# 4(choices for 1st post) * 3(choices for 
# 2nd post) = 12

# Input : n = 3 k = 2
# Output : 6


# O(N) time and O(N) space complexity
def get_fence_color_dp(n,k):
    dp = [[0 for i in range(n)]for i in range(2)]
    dp[0][2-2] = k
    dp[1][2-2] = k*(k-1)
    for i in range(3,n+1):
        last_two_same = dp[0][i-3]
        last_two_diff = dp[1][i-3]
        total = last_two_same + last_two_diff
        dp[0][i-2] = last_two_diff
        dp[1][i-2] = total*(k-1)
    return dp[0][-2] + dp[1][-2]

# O(N) time and O(1) space complexity
def get_fence_color_dp_opti(n,k):
    last_two_same = k*1
    last_two_diff = k*(k-1)
    total = last_two_diff+last_two_same
    for i in range(3,n):
        last_two_same = last_two_diff*1
        last_two_diff = total * (k-1)
        total = last_two_diff + last_two_same
    return total

if __name__ == '__main__':
    n = 8
    k = 3
    ans_dp = get_fence_color_dp(n,k)
    ans_op = get_fence_color_dp(n,k)
    
    print(f"Ans is {ans_dp} with using extra space ")
    print(f"Ans is {ans_op} without using extra space ")
