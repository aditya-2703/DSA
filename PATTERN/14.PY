# 14.  *********
#       *     *
#        *   *
#         * *
#          *

# n=5
# row_no  = 0 1 2 3 4 (n times)
# stars   = [9][2 2 2][1]
# outspace= 0 1 2 3 4 (row_no)
# inspace = [0][5 3 1][0] n-(2*(row_no-1)-1)+1
# print_char = " " and "*"


n=5
for i in range(n):
    outspace = i
    for j in range(outspace):
        print(" ",end=" ")
    if i==0:
        for j in range(2*n-1):
            print("*",end=" ")
    elif i<n-1:
        inspace= n-(2*(i-1))
        print("*",end=" ")
        for j in range(inspace):
            print(" ",end=" ")
        print("*",end=" ")
    else:
        print("*",end=" ")
    print()