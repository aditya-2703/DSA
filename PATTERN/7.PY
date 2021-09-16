# 7.   *****
#       ****
#        ***
#         **
#          *

# n=5
# row_no = 0 1 2 3 4 (n times)
# col_no = 1 2 3 4 5 (row+1 times)
# space  = 0 1 2 3 4 (row_no)
# stars  = 5 4 3 2 1 (n-col_no)
# print_char = "*" and  " "

n=5
for i in range(n):
    space = i
    stars = n-i 
    for i in range(space):
        print(" ",end=" ")
    for i in range(stars):
        print("*",end=" ")
    print()