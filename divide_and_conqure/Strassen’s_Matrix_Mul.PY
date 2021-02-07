# SIMPLE METRIX MULTIPLICATION WHICH TAKES O(N*N*N) TIME COMPLEXITY
def simple_matrix_mul(M,N):
     
    result_mat=[[0 for i in range(len(N))]for i in range(len(N))]
    for i in range(len(N)):
        for j in range(len(N)):
            for k in range(len(N)):
                result_mat[i][j]+=M[i][k]*N[k][j]

    for i in range(len(N)):
        print(result_mat[i])

# simple_matrix_mul(M,N)


# SECOND METHOD WHICH IS CALLED STRESSEN'S MATRIX WHICH TAKES O(N*N*N) TIME COMPLEXITY

M = [[1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
 
N = [[1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3],
    [4, 4, 4, 4]] 
