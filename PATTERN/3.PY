# 3.  *****
#     ****
#     ***
#     **
#     *

# n=5
# row_no = 0 1 2 3 4     (n times)
# col_no = 5 4 3 2 1     (n-row_no times)
# formula :  col_no = n - row_no
# print_char = "*"

n=5

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()