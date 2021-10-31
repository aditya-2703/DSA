# 24.    *        *
#        **      **
#        * *    * *
#        *  *  *  *
#        *   **   *
#        *   **   *
#        *  *  *  *
#        * *    * *
#        **      **
#        *        *

# n=5
#  0 1 2 3 4 
#  0 0 1 2 3
#  8 6 4 2 0
#  (i-1)*i

n=10
def print_increasing(row):
    print("*",end="")
    
    inner_space = 0 if row<=1 else row-1
    print(" "*inner_space,end="")
    
    if row!=0:
        print("*",end="")

    second_inner_space = 2*((n-1)-row)
    print(" "*second_inner_space,end="")

    print("*",end="")

    third_inner_space = 0 if row<=1 else row-1
    print(" "*third_inner_space,end="")
    
    if row!=0:
        print("*",end="")
def print_decreasing(row):
    print("*",end="")

    inner_space = n-row-2 if n-row-1>0 else 0
    print(" "*inner_space,end="")

    if row!=n-1:
        print("*",end="")

    inner_second_space = row*2
    print(" "*inner_second_space,end="")

    print("*",end="")
    
    inner_third_space = n-row-2 if n-row-1>0 else 0
    print(" "*inner_third_space,end="")

    if row!=n-1:
        print("*",end="")

    print()


def print_pattern():
    for row in range(n):
        
        print_increasing(row)
        print()

    for row in range(n):
        print_decreasing(row)

print_pattern()
