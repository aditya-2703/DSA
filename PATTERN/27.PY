# 27.   1 2 3 4  17 18 19 20
#         5 6 7  14 15 16
#           8 9  12 13
#             10 11

# N=4
# row no  = 0 1 2 3 (0 to n)
# total_digit = 1 to 20 (1 to n*5)

n=6
counter = 1
previous = True
for i in range(n):

    outer_space = 2*i
    print(" "*outer_space,end="")
    
    for j in range(1,n-i+1):
        print(counter,end=" ")
        counter+=1
    
    print(" ",end="")
    if previous==True:
        for j in range(n-i):
            value = (5*4)-n+(j+1)
            print(value,end=" ")
            previous = value
        previous -= (n-i)
    else:
        init_value = previous - (n-i)
        for j in range(n-i):
            value = init_value+1
            print(value,end=" ")
            init_value+=1
            previous = value
        previous -= (n-i)
        
    print()