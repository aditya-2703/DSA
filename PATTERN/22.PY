# 22.    1
#        0 1
#        1 0 1
#        0 1 0 1
#        1 0 1 0 1

# n=5
# row no = 0 1 2 3 4 (n-1 time)
# first  = 1 0 1 0 1 (even=1 odd=0)    

n=5
value=0
for row in range(n):
    if row&1==0:
        value=0
        print("1",end="")
    else:
        value=1
        print("0",end="")          
    for col in range(row):
        print(value,end="")
        value=value^1
    print()
        