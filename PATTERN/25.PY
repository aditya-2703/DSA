# 25.       *****
#          *   *
#         *   *
#        *   *
#       *****


# n=5

n=15
for row in range(n):
    outer_space = (n-1)-row
    print(" "*outer_space,end="")

    print("*",end="")

    if row==0 or row==n-1:
        print("*"*(n-2),end="")

    inner_spcae = n-2
    if row!=0 and row!=n-1:
        print(" "*inner_spcae,end="")

    print("*",end="")
    print()