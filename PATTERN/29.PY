# 29.      
#        *        *
#        **      **
#        ***    ***
#        ****  ****
#        **********
#        ****  ****
#        ***    ***
#        **      **
#        *        *

# n=5
n=15

def print_increasing(row):
    count_star = (row+1)
    print("*"*count_star,end="")

    inner_space = 2*(n-1-row)
    print(" "*inner_space,end="")

    print("*"*count_star,end="")


    print()
def print_decreasing(row):
    count_star = (n-row-1)
    print("*"*count_star,end="")

    inner_space = 2*(row+1)
    print(" "*inner_space,end="")

    print("*"*count_star,end="")


    print()

def print_pattern(n):
    for row in range(n):
        print_increasing(row)

    for row in range(n):
        print_decreasing(row)

print_pattern(n)