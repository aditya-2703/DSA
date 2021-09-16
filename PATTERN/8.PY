# 8.      *
#        ***
#       *****
#      *******
#     *********

# n=5
# row_no = 0 1 2 3 4 (n times)
# col_no = 1 3 5 7 9 (2*row)
# stars  = 1 3 5 7 9 (col_no)
# space  = 5 4 3 2 1 (n-row_no)

n=5
for i in range(n):
    stars = 2*i + 1
    space = n-i
    for i in range(space):
        print(" ",end=" ")
    for i in range(stars):
        print("*",end=" ")
    print()