# 28.      *
#         * *
#        * * *
#       * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *

# n=5
n=15

def print_increasing(row):
    outer_space = n-row
    print(" "*outer_space,end="")

    print("* "*row,end="")

    print()
def print_decreasing(row):
    outer_space = row+1
    print(" "*outer_space,end="")

    print("* "*(n-row-1),end="")

    print()

def print_pattern(n):
    for row in range(n+1):
        print_increasing(row)
    for row in range(n):
        print_decreasing(row)

print_pattern(n)