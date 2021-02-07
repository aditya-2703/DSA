# INPUT
# 1 0 0
# 0 0 0 
# 0 0 1
# MAKE ONE'S ROW AND COLUMN 1
# OUTPUT
# 1 1 1
# 1 0 1
# 1 1 1

def fill_row_col(row,col,matrix):
    for i in range(len(matrix)):
        if matrix[row][i]==0:
            matrix[row][i]=1
    for j in range(len(matrix)):
        if matrix[j][col]==0:
            matrix[j][col]=1
            
# METHOD 1 -- O(N^3) TIME AND O(N^N) SPACE COMPLEXITY (if n(row) == m(col))
def Method_1(matrix):
    newmatrix=[[0 for i in range(len(matrix))]for i in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col]==1:
                fill_row_col(row,col,newmatrix)
            
    return newmatrix

def fill_row_col_min_one(row,col,matrix):
    for i in range(len(matrix)):
        if matrix[row][i]==0:
            matrix[row][i]=-1
    for j in range(len(matrix)):
        if matrix[j][col]==0:
            matrix[j][col]=-1

# METHOD 2 -- O(N^3) TIME AND O(1) SPACE COMPLEXITY
def Method_2(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col]==1:
                fill_row_col_min_one(row,col,matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==-1:
                matrix[i][j]=1
    return matrix

# METHOD 3 -- O(N^2) TIME ANS O(N) SPACE COMPLEXITY
def Method_3(matrix):
    row=[0]*len(matrix)
    col=[0]*len(matrix[0])
    n=len(row)
    m=len(col)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=1
    return matrix
if __name__ == '__main__':
    matrix=[[1,0,0],
            [0,0,1],
            [0,0,0]]
    mat=Method_3(matrix)
    for i in mat:
        print(i)