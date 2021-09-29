# 20.    ****
#        *  *
#        *  *
#        *  *
#        ****

# n=5
# row_no = 0 1 2 3 4 
# star   = 4 2 2 2 4 (n-1 or (n-1)//2)

n=5
for i in range(n):
    if i==0 or i==n-1:
        if n&1==0:
            print("*"*((n)//2+1),end="")
        else:
            print("*"*((n)//2+2),end="")
    else:
        star  = (n-1)//2
        print("*",end="")
        print(" "*star,end="")
        print("*",end="")
    print()