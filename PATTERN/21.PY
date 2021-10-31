# 21.    1
#        2  3
#        4  5  6
#        7  8  9  10
#        11 12 13 14 15

# n=5
# row  no = 0 1 2 3 4 (n-1 times)


n=5
value=1
for row in range(n+1): 
    for j in range(row):
        print(value,end=" ")
        value+=1
    print()