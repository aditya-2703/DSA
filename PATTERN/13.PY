# 13.      *
#         * *
#        *   *
#       *     *
#      *********

# n=5
# row_no =  0 1 2 3 4 (n times)
# stars   = [1][2 2 2][9] 
# outspace= 4 3 2 1 0 (n-row_no-1)
# inspace = 0 1 3 5 0 (0 or 2*(row_no-1)+1)
# print_char = " " and "*"

n=5
for i in range(n):
    outspace =  n-i-1
    for j in range(outspace):
        print(" ",end=" ")
    if i==0:
        print("*",end=" ")
    elif i==n-1:
        stars = 2*n-1
        for j in range(stars):
            print("*",end=" ")
    else:
        inspace = 2*(i-1)+1
        print("*",end=" ")
        for j in range(inspace):
            print(" ",end=" ")
        print("*",end=" ")
    print()
    
    
    