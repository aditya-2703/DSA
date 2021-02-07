# Input:
# N = 4
# matrix[][] = {{1, 0, 2, -1},
#               {3, 0, 0, 5},
#               {2, 1, 4, -3},
#               {1, 0, 5, 0}}
# Output: 30
# Explanation:
# Determinant of the given matrix is 30.
# import builtins


def get_element(matrix,row,col):
    return [i[:col]+i[col+1:] for i in (matrix[:row]+matrix[row+1:])]
def Method_1(matrix):
    if len(matrix)==2:
        ans=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return ans
    result=0
    for i in range(len(matrix)):

        sign=(-1)**i
        div=Method_1(get_element(matrix,0,i))

        result+=(sign*matrix[0][i]*div)

    return result
        

if __name__ == '__main__':
    matrix=[[1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]]
    print(Method_1(matrix))
    