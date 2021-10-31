# 35.    1      1
#        12    21
#        123  321
#        12344321

# n=5

n=5

for row in range(n):

    start = 1
    end = row+1

    for i in range(start,end):
        print(i,end="")
    
    inner_space = 2*(n-row-1)
    print(" "*inner_space,end="")

    for i in reversed(range(start,end)):
        print(i,end="")

    print()

