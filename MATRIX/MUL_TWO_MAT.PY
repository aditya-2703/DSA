# Input:
# n1 = 3, m1 = 2
# A[][] = {{4, 8},
#          {0, 2}
#          {1, 6}}
# n2 = 2, m2 = 2
# B[][] = {{5, 2},
#          {9, 4}}
# Output: 92 40 18 8 59 26
# Explanation:
# Matrices are of size 3 x 2 and 2 x 2 which 
# results in 3 x 2 matrix with elements as:
# res[][] = {{92, 40},
#            {18, 8}
#            {59, 26}}

# METHOD 1 -- TAKES O(N1*M2*N2) TIME ANS O(N1*M2) SPACE COMPLEXITY
def Method_1(mat1,mat2):
    n1=len(mat1)
    n2=len(mat1[0])
    m1=len(mat2)
    m2=len(mat2[0])
    if n2!=m1:
        return []
    else:
        res=[[0 for i in range(m2)]for i in range(n1)]
        for i in range(n1):
            for j in range(m2):
                for k in range(n2):
                    res[i][j]+=mat1[i][k]*mat2[k][j]
        return res

if __name__ == '__main__':
    mat1=[[4, 8],[0, 2],[1, 6]]
    mat2=[[5, 2],[9, 4]]
    print(Method_1(mat1,mat2))
    