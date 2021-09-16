# 5.  *
#     **
#     ***
#     ****
#     *****
#     ****
#     ***
#     **
#     *

# n=5
# total row = 9  = 2*n - 1
# row_no = 0 1 2 3 4 5 6 7 8
# col_no = 1 2 3 4 5 4 3 2 1
# formula : col_no = row_no+1 if row_no<=n else row_no-=1
# print_char = "*"

n=5
for i in range(1,2*n+1):
    col_no = i if i<=n else 2*n-i
    for j in range(col_no):
        print("*",end=" ")
    print()
        