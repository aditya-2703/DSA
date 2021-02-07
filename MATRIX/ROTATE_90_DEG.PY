# Input:
# N = 3 
# matrix[][] = {{1, 2, 3},
#               {4, 5, 6}
#               {7, 8, 9}}
# Output: 
# Rotated Matrix:
# 3 6 9
# 2 5 8
# 1 4 7

# METHOD 1 -- TAKES0(N*N) TIME AND O(N) SPACE COMPLEXITY
def Method_1(matrix):
    temp=[[0 for i in range(len(matrix))]for i in range(len(matrix))]
    if len(matrix)==1:
        return matrix[0]
    else:
        n=len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp[i][j]=matrix[j][n-i-1]
                
        return temp

# METHOD 2 -- TAKES0(N*N) TIME AND O(1) SPACE COMPLEXITY
# HERE WE RUN CYCLES TO ROTATE 90 DEF LIKE IF MATRIX IS 4*4 THEN NO OF CYCLE IS 4//2 IS 2
# IT MEANS FIRST WE MANAGE AND MAKE OUTER ELEMENTS ROTATED AND THEN INNER
# FOR ROTATE :
# FIRST WE GO RIGHT TO TOP [i][j]<-[j][n-i] where n is len(matrix)-1
# THEN WE GO BOTTOM TO RIGHT [j][n-i]<-[n-i][n-j]
# THEN WE GO LEFT TO BOTTOM [n-i][n-j]<-[n-j][i]
# AT LAST WE PLACE OUR [n-j][i]<-[i][j]
# SAME GOES TO INNER MATRIX 
def Method_2(matrix):
    n=len(matrix)-1
    for i in range(len(matrix)//2):
        for j in range(i,n-i):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][n-i]#1
            matrix[j][n-i]=matrix[n-i][n-j]#2
            matrix[n-i][n-j]=matrix[n-j][i]#3
            matrix[n-j][i]=temp#4

    return matrix
if __name__ == '__main__':
    matrix=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    print(Method_2(matrix))
