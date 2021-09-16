# 4.  1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5

# n=5
# row = 0 1 2 3 4 (n times)
# col = 1 2 3 4 5  row+1   (row times)
# print_char = col

n=5
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
    