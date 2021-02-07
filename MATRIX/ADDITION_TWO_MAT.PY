# Input:
# n1 = 2, m1 = 3
# A[][] = {{1, 2, 3},
#          {4, 5, 6}}

# n2 = 2, m2 = 3
# B[][] = {{1, 3, 3},
#          {2, 3, 3}}

# Output: 2 5 6 6 8 9
# Explanation:
# The summation matrix of A and B is:
# res[][] = {{2, 5, 6},
#            {6, 8, 9}}


# METHOD 1 -- TAKES O(M*N) TIME AND O(M*N) SPACE COMPLEXITY
def Method_1(mat1,mat2):
    res=[[0 for i in range(len(mat1[0]))]for i in range(len(mat1))]
    if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
        return []
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            res[i][j]=mat1[i][j]+mat2[i][j]
    return res



if __name__ == '__main__':
    mat1=[[1, 2, 3],[4, 5, 6]]
    mat2=[[1, 3, 3],[2, 3, 3]]
    print(Method_1(mat1,mat2))