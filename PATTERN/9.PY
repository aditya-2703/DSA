# 9.  *********
#      *******
#       *****
#        ***
#         *

# n=5
# row_no = 0 1 2 3 4 (n times)
# stars  = 9 7 5 3 1 (2*(n-row_no)-1)
# space  = 0 1 2 3 4 
# print_char = " " and "*"

n=5
for i in range(n):
    space = i
    stars = 2*(n-i)-1
    for i in range(space):
        print(" ",end=" ")
    for i in range(stars):
        print("*",end=" ")
    print()