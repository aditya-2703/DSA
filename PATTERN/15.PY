# 15.      *
#         * *
#        *   *
#       *     *
#      *       *
#       *     *
#        *   *
#         * *
#          *

# n=5
# row_no   = 0 1 2 3 4 5 6 7 8  (2*n - 1 times)
# stars    = [1][2 2 2 2 2 2 2][1] 
# outspace =[4 3 2 1] 0 [1 2 3 4]  (n-1-row_no  or row_no-n+1)
# inspace  =[0][1 3 5 7 5 3 1][0] (0 or 2*(row_no-1)+1 or 2*(((2*n)-2)-row_no-1) + 1)
# print_char = " " and "*"


n=5
for i in range(2*n-1):
    out_space = n-1-i if i<n else i-n+1
    for j in range(out_space):
        print(" ",end="")                 

    if i==0 or i==2*n-2:
        print("*",end="")

    else:
        in_space = 2*(i-1)+1  if i<n else 2*(((2*n)-2)-i-1) + 1
        print("*",end="")
        for j in range(in_space):
            print(" ",end="")
        print("*",end="")
    print()