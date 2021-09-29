# 19.    *        *
#        **      **
#        ***    ***
#        ****  ****
#        **********
#        ****  ****
#        ***    ***
#        **      **
#        *        *

# n=5
# limit = 2*n-1
# row_no   = 0 1 2 3 4 5 6 7 8 (limit)
# in_space = 8 6 4 2 0 2 4 6 8 (limit-2*row_no if limit>=row_no else 2*(row_no-n+1))

n=25
limit = (2*n)-1
for row in range(limit):
    in_space = abs(limit-1-2*row)if limit>=row else 2*(row-n+1)
    stars = (2*n - in_space)//2
    print("*"*stars,end="")
    print(" "*in_space,end="")
    print("*"*stars)