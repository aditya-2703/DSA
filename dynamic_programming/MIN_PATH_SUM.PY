# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


# recursion
grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[1,2,3],[4,5,6]]
start = [0,0]
n,m = len(grid)-1,len(grid[0])-1
end = [n,m]

total_recursion_moves = 0
def get_min_path_sum(grid,start,end):
    global total_recursion_moves
    total_recursion_moves+=1

    if start[0]==end[0] and start[1]==end[1]:
        return grid[end[0]][end[1]]
        
    down = right = 999999
    if start[1]<end[1]:
        right = get_min_path_sum(grid,[start[0],start[1]+1],end)

    if start[0]<end[0]:        
        down = get_min_path_sum(grid,[start[0]+1,start[1]],end)

    return grid[start[0]][start[1]]+min(down,right)

print(f"Ans {get_min_path_sum(grid,start,end)} with total {total_recursion_moves} moves in recursion")

total_dp_moves = 0
def get_min_path_sum_dp(grid):

    global total_dp_moves
    dp = [[99999]*len(grid[0])]*len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total_dp_moves+=1

            cost = grid[i][j]
            if i==0 and j==0:
                dp[i][j]=cost
            elif i==0:
                paths_sum = cost + dp[i][j-1]
                dp[i][j] = paths_sum
            elif j==0:
                paths_sum = cost + dp[i-1][j]
                dp[i][j] = paths_sum
            else:
                paths_sum = cost + min(dp[i-1][j],dp[i][j-1])
                dp[i][j] = paths_sum
    return dp[-1][-1]

print(f"Ans {get_min_path_sum_dp(grid)} with total {total_dp_moves} moves in dp")



