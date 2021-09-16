# 12.  * * * * *
#       * * * *
#        * * *
#         * *
#          *
#          *
#         * *
#        * * *
#       * * * *
#      * * * * *

# n=5
# row_no = 0 1 2 3 4 5 6 7 8 9 (2*n times)
# stars  = 5 4 3 2 1 1 2 3 4 5 (n -row_no or row_no-n+1)
# space  = 0 1 2 3 4 4 3 2 1 0 (row_no or n-stars)
# print_char = " " and "*"
# formula : stars = n-row_no if n>=row_no else row_no-n+1
#         : space = row_no if n>=row_no else n-stars

n=5
for i in range(2*n):
    stars = n-i if i<n else i-n+1
    space = i if i<n else n-stars
    for i in range(space):
        print(" ",end="")
    for i in range(stars):
        print("* ",end="")
    print()
