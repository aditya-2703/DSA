# 6.       *
#         **
#        ***
#       ****
#      *****

# n=5
# row_no = 0 1 2 3 4 (n times)
# col_no = 1 2 3 4 5  (row_no+1 times) 
# print_char = spaces ->" " * (4,3,2,1,0) or (n-row_no)
# print_char = stars -> "*"  (1,2,3,4,5) or (col_no)

n=5
for i in range(n):
    spaces=n-i
    stars = i+1 
    for i in range(spaces):
        print(" ",end=" ")
    for i in range(stars):
        print("*",end=" ")
    print()    