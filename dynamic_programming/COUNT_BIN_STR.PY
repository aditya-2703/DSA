# Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.

# Examples: 
# Input:  N = 2
# Output: 3
# The 3 strings are 00, 01, 10

# Input: N = 3
# Output: 5
# The 5 strings are 000, 001, 010, 100, 101

# with recursion
n = 6
total_recursion_moves = 0
def is_consicutive(string):
    not_allowed = "1"
    if len(string)==2:
        if string[0]==not_allowed and string[1]==not_allowed:
            return True
        else:
            return False
    for i in range(len(string)-1):
        if string[i]==not_allowed and string[i+1]==not_allowed:
            return True
    return False
def get_bin_str_recursion(n,i,string):
    global total_recursion_moves
    total_recursion_moves+=1
    if is_consicutive(string):
        return 0
    if i==n:
        # print(string)
        return 1
    zero_taken = get_bin_str_recursion(n,i+1,string+"0")
    one_taken = get_bin_str_recursion(n,i+1,string+"1")
    return zero_taken+one_taken
print(f"Ans is {get_bin_str_recursion(n,0,'')} with {total_recursion_moves} moves in recursion ")

# with dp
total_dp_moves = 0
def get_bin_str_dp(n):
    global total_dp_moves
    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)
    dp0[1]=1
    dp1[1]=1
    for i in range(2,n+1):
        total_dp_moves+=1
        dp1[i] = dp0[i-1]+dp1[i-1]
        dp0[i] = dp1[i-1]
    return dp1[-1]+dp0[-1]
print(f"Ans is {get_bin_str_dp(n)} with {total_dp_moves} moves in dp ")


