# SORTED ARRAY
# Input:
# n = 3, m = 3, x = 62
# matrix[][] = {{ 3, 30, 38},
#               {36, 43, 60},
#               {40, 51, 69}}
# Output: 0
# Explanation:
# 62 is not present in the matrix, 
# so output is 0.

# METHOD 1 -- O(N*M) TIME AND O(1) SPACE COMPLEXITY 
def Method_1(matrix,x):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==x:
                return 1
    return 0

# METHOD 2 -- 0(N) TIME AND O(1) SPACE COMPLEXITY
def Method_2(matrix,x):
    n=len(matrix)
    m=len(matrix[0])
    i=0
    j=m-1
    while i<n and j>=0:
        if matrix[i][j]==x:
            return 1
        elif matrix[i][j]>x:
            j-=1
        else:
            i+=1
    return 0





if __name__ == '__main__':
    matrix=[[3, 30, 38],
            [36, 43, 60],
            [40, 51, 69]]
    print(Method_2(matrix,62))