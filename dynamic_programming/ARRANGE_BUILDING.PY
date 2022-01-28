# 1. You are given a number n, which represents the length of a road. The road has n plots on it's each side.
# 2. The road is to be so planned that there should not be consecutive buildings on either side of the road.
# 3. You are required to find and print the number of ways in which the buildings can be built on both side of roads.
# Input Format
# A number n
# Output Format
# A number representing the number of ways in which the buildings can be built on both side of roads.

# Sample Input
# 6
# Sample Output
# 441


# with recursion
n = 6
total_recursion_moves = 0
def is_consicutive(string):
    not_allowed = "B"
    if len(string)==2:
        if string[0]==not_allowed and string[1]==not_allowed:
            return True
        else:
            return False
    for i in range(len(string)-1):
        if string[i]==not_allowed and string[i+1]==not_allowed:
            return True
    return False
def get_bil_arrange_recursion(n,i,string):
    global total_recursion_moves
    total_recursion_moves+=1
    if is_consicutive(string):
        return 0
    if i==n:
        # print(string)
        return 1
    zero_taken = get_bil_arrange_recursion(n,i+1,string+"B")
    one_taken = get_bil_arrange_recursion(n,i+1,string+"S")
    return zero_taken+one_taken
print(f"Ans is {get_bil_arrange_recursion(n,0,'')**2} with {total_recursion_moves} moves in recursion ")


# with dp
total_dp_moves = 0
def get_bil_arrange_dp(n):
    global total_dp_moves
    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)
    dp0[1]=1
    dp1[1]=1
    for i in range(2,n+1):
        total_dp_moves+=1
        dp1[i] = dp0[i-1]+dp1[i-1]
        dp0[i] = dp1[i-1]
    return (dp1[-1]+dp0[-1])**2
print(f"Ans is {get_bil_arrange_dp(n)} with {total_dp_moves} moves in recursion ")

