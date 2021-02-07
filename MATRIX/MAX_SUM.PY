# Input:
# n = 4, m = 4
# M[][] = {{0 1 1 0},
#          {1 1 1 1},
#          {1 1 1 1},
#          {1 1 0 0}}
# Output: 8
# Explanation: For the above test case the
# matrix will look like
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# the max size rectangle is 
# 1 1 1 1
# 1 1 1 1
# and area is 4 *2 = 8.

# Expected Time Complexity : O(n*m)
# Expected Auixiliary Space : O(m)

def Method_1(matrix):
    n=len(matrix)
    m=len(matrix[0])
    count=0
    a=0
    b=m-1
    i=0
    while i<n:
        if matrix[i][a]==0 or matrix[i][b]==0:
            continue
        else:
            count+=(b-a)+1
            continue
    print(count)
if __name__ == '__main__':
    matrix= [[0,1,1,0],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,0,0]]
    Method_1(matrix)
    