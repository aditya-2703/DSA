# 18.   **********
#       ****  ****
#       ***    ***
#       **      **
#       *        *
#       *        *
#       **      **
#       ***    ***
#       ****  ****
#       **********

# n=5
# row_no  =  0 1 2 3 4  5 6 7 8 9 (n*2)
# in_space = 0 2 4 6 8  8 6 4 2 0 (row*2 if row<=n-1 else (2*n-row)+((2*n)-2)-row)

n=15
for row in range(2*n):
    if row==0 or row==2*n-1:
        print("*"*(2*n),end="")
    else:
        in_space = row*2 if row<=n-1 else 2*((2*n)-row-1)
        top = (2*n - in_space)//2
        print("*"*top,end="")
        print(" "*in_space,end="")
        bottom = (2*n - in_space)//2
        print("*"*bottom,end="")
    print()