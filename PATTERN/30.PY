# 30.         1
#           2 1 2
#         3 2 1 2 3
#       4 3 2 1 2 3 4
#     5 4 3 2 1 2 3 4 5

# n=5
n=5

for row in range(n):
    outer_space = 2*(n-row-1)
    print(" "*outer_space,end="")

    range_digit = row+1
    for i in reversed(range(1,range_digit)):
        print(i,end=" ")

    for i in range(2,range_digit):
        print(i,end=" ")

    print()