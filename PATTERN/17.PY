# 17.      1
#         212
#        32123
#       4321234
#        32123
#         212
#          1

# n=5
# row no   = 0 1 2 3 4 5 6 (n+2)
# outspace = 3 2 1 0 1 2 3 ((n+1)//2 to 0 and reverse) 
# 1st digit= 1 2 3 4 3 2 1 (row_no+1 if n+1//2 <= row_no n+1//2-outspace+1)

n=15
for row in range(n+2):
    out_space = (n+1)//2-row if (n+1)//2>=row else row-(n+1)//2
    for i in range(out_space):
        print(" ",end="")

    number = row+1 if (n+1)//2>=row else (n+1)//2-out_space+1
    for i in reversed(range(1,number+1)):
        print(i,end="")
    for i in range(2,number+1):
        print(i,end="")
        
    
    print()