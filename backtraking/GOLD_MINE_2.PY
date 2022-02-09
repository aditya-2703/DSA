# Gold Mine Problem

# Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect. 
# https://www.geeksforgeeks.org/gold-mine-problem/

# Examples: 
# Input : mat[][] = {{1, 3, 3},
#                    {2, 1, 4},
#                   {0, 6, 4}};
# Output : 12 
# {(1,0)->(2,1)->(1,2)}

# Input: mat[][] = { {1, 3, 1, 5},
#                    {2, 2, 4, 1},
#                    {5, 0, 2, 3},
#                    {0, 6, 1, 2}};
# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)

# Input : mat[][] = {{10, 33, 13, 15},
#                   {22, 21, 04, 1},
#                   {5, 0, 2, 3},
#                   {0, 6, 14, 2}};
# Output : 83
def dfs(i,j,n,m,mat,visited,bag):
    if i<0 or j<0 or i>=n or j>=m or mat[i][j] == 0 or visited[i][j] == True:
        return 0
    visited[i][j] = True
    bag.append(mat[i][j])
    # up
    dfs(i-1,j,n,m,mat,visited,bag)
    # down
    dfs(i+1,j,n,m,mat,visited,bag)
    # left
    dfs(i,j-1,n,m,mat,visited,bag)
    # right
    dfs(i,j+1,n,m,mat,visited,bag)
    
def get_max_gold(n,m,mat):
    visited = [[False for i in range(m)]for i in range(n)]
    max_profit = -9999999
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and mat[i][j]!=0:
                bag = []
                dfs(i,j,n,m,mat,visited,bag)
                max_profit = max(max_profit,sum(bag))
    return max_profit

if __name__ == '__main__':
    n = 6
    m = 6
    mat = [[0, 1, 4, 2, 8 ,2],
        [4 ,3 ,6 ,5 ,0 ,4],
        [1 ,2 ,4 ,1 ,4 ,6],
        [2 ,0 ,7 ,3 ,2 ,2],
        [3 ,1 ,5 ,9 ,2 ,4],
        [2 ,7 ,0 ,8 ,5 ,1]]
    ans = get_max_gold(n,m,mat)
    print(ans)