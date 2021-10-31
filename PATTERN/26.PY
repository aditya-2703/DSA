# 26.   1 1 1 1 1 1
#       2 2 2 2 2
#       3 3 3 3
#       4 4 4
#       5 5
#       6

# N=5
# row no  = 0 1 2 3 4 5 (0 to n)
# digit   = 1 2 3 4 5 6
# count   = 6 5 4 3 2 1

n=5
for row in range(n+1):
    digit = row+1
    count = n+1 - row

    print(f"{digit} "*count,end="")    
    print()
