# N          N!
#  C   =  --------
#   R     (N-R)!R!
# 
# BEST CASE IF N==R OR R==0 RETURN 1

# METHOD 1 -- TAKES O(N*N) TIME AND O(1) SPACE COMPLEXITY (avoid stack concept)
def Method_1(n,r):
    if n==0:
        return 0
    if n==r or r==0:
        return 1
    else:
        return Method_1(n-1,r-1)+Method_1(n-1,r)

# METHOD 2 -- TAKES O(N*K) TIME ANS O(N*K) SPACE COMPLEXITY
def Method_2(n,r):
    matrix=[[0 for i in range(r+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(r+1):
            if j==i or j==0:
                matrix[i][j]=1
            else:
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]
    print(matrix[n][r])

# METHOD 3 -- TAKES O(N*R) TIME AND O(R) SPACE COMPLEXITY
def Method_3(n,r):
    matrix=[0 for i in range(r+1)]
    matrix[0]=1
    for i in range(1,n+1):
        j=r
        while j>0:
            matrix[j]=matrix[j-1]+matrix[j]
            j-=1
    print(matrix[r])
# METHOD 4 -- TAKES O(R) TIME AND O(1) SPACE COMPLEXITY
def Method_4(n,r):
    if r>n-r:
        r=n-r
    res=1
    for i in range(r):
        res*=(n-i)
        res//=(i+1)
    print(res)

if __name__ == '__main__':
    # print(Method_1(5,2))
    Method_2(5,2)
    Method_3(5,2)
    Method_4(5,2)