# 32.    E
#        D E
#        C D E       
#        B C D E
#        A B C D E

#        or  1 = chr(64 + 1) = A

#        5
#        4 5
#        3 4 5       
#        2 3 4 5
#        1 2 3 4 5


# n=5
n=5

for row in range(n):

    range_digit_start = n-row
    range_digit_end = n+1

    for i in range(range_digit_start,range_digit_end):
        alphabet = chr(i+64)
        print(alphabet,end=" ")
    
    print()
