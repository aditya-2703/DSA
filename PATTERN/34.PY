# 34.    E D C B A
#        D C B A
#        C B A
#        B A
#        A

#   or e = 69 = chr(64+5)

#  5 4 3 2 1
#  4 3 2 1
#  3 2 1 
#  2 1
#  1
# 

n=5
for row in range(n):

    start = n-row 
    end = 0

    for i in range(start,end,-1):
        char = chr(i+64)
        print(char,end=" ")
    
    print()