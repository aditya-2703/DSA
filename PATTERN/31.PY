# 31.      4 4 4 4 4 4 4  
#          4 3 3 3 3 3 4   
#          4 3 2 2 2 3 4   
#          4 3 2 1 2 3 4   
#          4 3 2 2 2 3 4   
#          4 3 3 3 3 3 4   
#          4 4 4 4 4 4 4  

# n=5
# 0 1 2 3
# 5 3 1 0
# n-(i)*2 
n=8

def print_increasing(row):
    curr_start_range = n-1
    curr_end_range = n-row
    curr_digit = n-row

    for i in reversed(range(curr_end_range,curr_start_range+1)):
        print(i,end="")
    
    innner_space = n-(2*(row-2))
    print(f"{curr_digit}"*innner_space,end="")

    if row==n-1:
        for i in range(curr_end_range+1,curr_start_range+1):
            print(i,end="")
    else:
        for i in range(curr_end_range,curr_start_range+1):
            print(i,end="")

    print()
def print_decreasing(row):
    
    curr_start_range = n-1
    curr_end_range = row
    curr_digit = n-row

    for i in reversed(range(curr_end_range+1,curr_start_range+1)):
        print(i,end="")
    
    innner_space = (2*(row))-1
    print(f"{row+1}"*innner_space,end="")

    if row==n-1:
        for i in range(curr_end_range+1,curr_start_range+1):
            print(i,end="")
    else:
        for i in range(curr_end_range+1,curr_start_range+1):
            print(i,end="")

    print()



def print_patter(n):
    for row in range(1,n):
        print_increasing(row)
    for row in range(1,n-1):
        print_decreasing(row)

print_patter(n)