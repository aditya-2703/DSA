# Flood Fill

# 1. You are given a number n, representing the number of rows.
# 2. You are given a number m, representing the number of columns.
# 3. You are given n*m numbers, representing elements of 2d array a. The numbers can be 1 or 0 only.
# 4. You are standing in the top-left corner and have to reach the bottom-right corner. 
# Only four moves are allowed 't' (1-step up), 'l' (1-step left), 'd' (1-step down) 'r' (1-step right). You can only move to cells which have 0 value in them. You can't move out of the boundaries or in the cells which have value 1 in them (1 means obstacle)
# 5. Complete the body of floodfill function - without changing signature - to print all paths that can be used to move from top-left to bottom-right.

# Note1 -> Please check the sample input and output for details
# Note2 -> If all four moves are available make moves in the order 't', 'l', 'd' and 'r'

# input
# n = 3  ,m = 3
# [[0, 0, 0,]
# [1, 0, 1,]
# [0, 0, 0,]]

# output
# rddr


def flood_fill(matrix,i,j,n,m,visited,path):
    if i<0 or j<0 or i>=n or j>=m or visited[i][j]==True or matrix[i][j]==1:
        return 
    if i==n-1 and j==m-1:
        print(path)
        return 
    # mark 
    visited[i][j] = True
    # top 
    flood_fill(matrix,i-1,j,n,m,visited,path+"t")
    # left
    flood_fill(matrix,i,j-1,n,m,visited,path+"l")
    # down
    flood_fill(matrix,i+1,j,n,m,visited,path+"d")
    # right
    flood_fill(matrix,i,j+1,n,m,visited,path+"r")
    # unmark
    visited[i][j] = False 
    


if __name__ == '__main__':
    n = 3
    m = 3
    matrix = [[0,0,0],[1,0,0],[0,0,0]]
    visited = [[False for i in range(m)]for i in range(n)]
    flood_fill(matrix,0,0,n,m,visited,"")