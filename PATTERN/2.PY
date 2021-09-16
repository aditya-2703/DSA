# 2.  *
#     **
#     ***
#     ****
#     *****

# n=5
# row_no = 0 1 2 3 4 (n times)
# col_no = 1 2 3 4 5  row+1   (row times)
# print_char = "*"

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    