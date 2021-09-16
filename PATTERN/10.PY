# 10.      *
#         * *
#        * * *
#       * * * *
#      * * * * *

# n=5
# row_no = 0 1 2 3 4 (n times)
# space  = 4 3 2 1 0 (n-row_no-1)
# star   = 1 2 3 4 5
# print_char = " " and "*"

n=5
for i in range(n):
    space = n-1-i
    star = i+1
    for i in range(space):
        print(" ",end="")
    for i in range(star):
        print("* ",end="")
    print()
