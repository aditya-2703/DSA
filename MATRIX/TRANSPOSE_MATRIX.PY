# Input:
# N = 4
# mat[][] = {{1, 1, 1, 1},
#            {2, 2, 2, 2}
#            {3, 3, 3, 3}
#            {4, 4, 4, 4}}
# Output: 
# {{1, 2, 3, 4},  
#  {1, 2, 3, 4}  
#  {1, 2, 3, 4}
#  {1, 2, 3, 4}} 

# METHOD 1 -- TAKES O(N*N) TIME ANS O(1) SPACE COMPLEXITY
def Method_1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i<=j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    print(matrix)

if __name__ == '__main__':
    matrix=[[1,1,1,1],
            [2,2,2,2],
            [3,3,3,3],
            [4,4,4,4]]
    print(Method_1(matrix))
