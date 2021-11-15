# Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect. 
# Examples: 

# Input : mat[][] = [[1, 3, 3],
#                    [2, 1, 4],
#                   [0, 6, 4]];
# Output : 12 
# [(1,0)->(2,1)->(1,2)]
# Input: mat[][] = [ [1, 3, 1, 5],
#                    [2, 2, 4, 1],
#                    [5, 0, 2, 3],
#                    [0, 6, 1, 2]];
# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)
# Input : mat[][] = [[10, 33, 13, 15],
#                   [22, 21, 04, 1],
#                   [5, 0, 2, 3],
#                   [0, 6, 14, 2]];
# Output : 83


matrix = [[1, 3, 3],[2, 1, 4],[0, 6, 4]]
matrix = [[10, 33, 13, 15],[22, 21, 4, 1],[5, 0, 2, 3],[0, 6, 14, 2]]
matrix  = [ [1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]]
n = len(matrix)
m = len(matrix[0])

# with recursion
total_recursion_moves = 0 
def gold_digger(matrix,row,col,n,m):
    global total_recursion_moves
    total_recursion_moves+=1
    if row<0 or row>n or col<0 or col>m:
        return 0  
    if col == m:
        return matrix[row][col]
    
    right = gold_digger(matrix,row,col+1,n,m)
    right_up = gold_digger(matrix,row-1,col+1,n,m)
    right_down = gold_digger(matrix,row+1,col+1,n,m)
    return matrix[row][col]+max(right,right_up,right_down)
def get_max_gold_recursion(matrix,n,m):

    max_gold = -999999
    for i in range(len(matrix)):
        curr_gold = gold_digger(matrix,i,0,n-1,m-1) 
        max_gold = max(max_gold,curr_gold)
    return max_gold
# print(f"Ans is {get_max_gold_recursion(matrix,n,m)} with recursion total moves {total_recursion_moves}")


# with dp
total_dp_moves = 0
def get_max_gold_dp(matrix,n,m):
    global total_dp_moves
    dp = [[0 for i in range(m)] for i in range(n)]

    
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if j==m-1:
                dp[i][j] = matrix[i][j] 
            elif i==0:
                additional_cost = max(dp[i][j+1],dp[i+1][j+1])
                dp[i][j] = additional_cost + matrix[i][j]
            elif i==n-1:
                additional_cost = max(dp[i][j+1],dp[i-1][j+1])
                dp[i][j] = additional_cost + matrix[i][j]
            else:
                additional_cost = max(dp[i-1][j+1],dp[i][j+1],dp[i+1][j+1])
                dp[i][j] = additional_cost + matrix[i][j]
    result = -999999
    for i in range(n):
        result =  max(result,dp[i][m-1]) 

    for i in dp:
        print(i)
    return result

print(f"Ans is {get_max_gold_dp(matrix,n,m)} with dp total moves {total_dp_moves}")
