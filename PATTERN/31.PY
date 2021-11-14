# 31.      4 4 4 4 4 4 4  
#          4 3 3 3 3 3 4   
#          4 3 2 2 2 3 4   
#          4 3 2 1 2 3 4   
#          4 3 2 2 2 3 4   
#          4 3 3 3 3 3 4   
#          4 4 4 4 4 4 4  

n=4
def print_pattern(n):
    row = 2*n-1
    col = 2*n-1 
    for i in range(row):
        for j in range(col):
            digit =  n-min(min(i,j),min(row-i-1,col-j-1))
            print(digit,end=" ")
        print()

print_pattern(n)
