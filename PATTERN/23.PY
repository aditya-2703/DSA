# 23.        *      *
#          *   *  *   *
#        *      *      *



# n=3
# row no  = 0 1 2 
# outspace= 4 2 0  
# col no  = 2 1 0 1 2 1 0 1 2 (3*n)
# outspace= 2 1 0

n=3

for i in range(n):
    outer_space =  2*((n-1)-i)
    print(" "*outer_space,end="")

    print("*",end="")

    inner_space = ((n)*i)
    print(" "*inner_space,end="")

    if i!=0:
        print("*",end="")

    inner_second_space = ((n)*(n-i-1) - i)
    print(" "*inner_second_space,end="")

    if i!=n-1:
        print("*",end="")

    inner_third_space = ((n)*i)
    print(" "*inner_third_space,end="")
    
    if i!=0:
        print("*",end="")


    print()




