# 27.   1 2 3 4  17 18 19 20
#         5 6 7  14 15 16
#           8 9  12 13
#             10 11

# N=4
# row no  = 0 1 2 3 (0 to n)
# total_digit = 1 to 20 (1 to n*5)

n=5
counter_normal = 1
counter_reverse = (n)*(n-1)
for i in range(n+1):

    outer_space = 2*i
    print(" "*outer_space,end="")
    digit_range = n-i-1
        
    for j in range(digit_range):
        print(f"{counter_normal} ",end="")
        counter_normal+=1
    print(" ",end="")
    
    start = counter_reverse-digit_range+1
    end = counter_reverse+1
    for j in range(start,end):
        print(f"{j} ",end="")
        counter_reverse-=1
    
    print()
