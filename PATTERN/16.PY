# 16.           1
#             1   1
#           1   2   1
#         1   3   3   1
#       1   4   6   4   1


# no_of_row = 0 1 2 3 4 (n times)
# out_space = 4 3 2 1 0 (n-row-1)
# C(line, i)   = line! / ( (line-i)! * i! ) 



def binomialCoeff(n, k) :
    if (k > n - k) :
        k = n - k
    res=1
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    return res



n=5
result=""
for row in range(n):
    out_space = n-row-1
    for i in range(out_space):
        print(" ",end="")
    
    for col in range(row+1):
        solution = binomialCoeff(row, col)
        print(solution,end=" ")
    print()    





