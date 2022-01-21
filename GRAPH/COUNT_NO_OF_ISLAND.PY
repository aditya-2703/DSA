# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]]
# Output: 3


def get_island(row,col,visited,matrix):
    if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or matrix[row][col]==1 or visited[row][col]==True:
        return 
    visited[row][col]=True
    get_island(row-1,col,visited,matrix)
    get_island(row,col+1,visited,matrix)
    get_island(row,col-1,visited,matrix)
    get_island(row+1,col,visited,matrix)
    
def get_no_of_island(matrix):
    visited = [[False]*len(matrix[0])]*len(matrix)
    no_of_island = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0 and visited[i][j]==False:
                get_island(i,j,visited,matrix)
                no_of_island+=1
    return no_of_island

if __name__ == '__main__':
    matrix=[[0,0,1,1,1,1,1,1],
            [0,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,0],
            [1,1,0,0,0,1,1,0],
            [1,1,1,1,0,1,1,0],
            [1,1,1,1,0,1,1,0],
            [1,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,0]]
    island=get_no_of_island(matrix)
    print(island)