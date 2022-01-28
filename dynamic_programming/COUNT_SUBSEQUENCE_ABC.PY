# Given a string, count number of subsequences of the form aibjck, i.e., it consists of i ’a’ characters, followed by j ’b’ characters, followed by k ’c’ characters where i >= 1, j >=1 and k >= 1. 
# Note: Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.
# Expected Time Complexity: O(n)
# Examples: 
 
# Input  : abbc
# Output : 3
# Subsequences are abc, abc and abbc
# Input  : abcabc
# Output : 7
# Subsequences are abc, abc, abbc, aabc
# abcc, abc and abc

# with recursion
string = "aaabcbcc"

def is_perfect_sequence(string):
    if not string:
        return False
    char = string[0]
    if "a" in string and "b" in string and "c" in string:    
        for i in range(1,len(string)):
            if ord(char)<=ord(string[i]):
                char = string[i]
                continue
            else:
                return False
        return True
    else:
        return False

        
# with recursion
total_recursion_moves = 0
def get_sub_sequence_recursion(string,i,code):
    global total_recursion_moves
    total_recursion_moves+=1
    if i>len(string):
        return 0
    if i==len(string):
        if is_perfect_sequence(code):
            return 1
        return 0
    is_taken = get_sub_sequence_recursion(string,i+1,code+string[i])
    is_not_taken = get_sub_sequence_recursion(string,i+1,code)
    return is_taken+is_not_taken
ans = get_sub_sequence_recursion(string,0,"")
print(f"Ans is {ans} with moves {total_recursion_moves} in recursion")



# with dp
total_dp_moves = 0
def get_sub_sequence_dp(string):
    global total_dp_moves
    a = 0
    ab = 0
    abc = 0

    for i in string:
        total_dp_moves+=1
        if i=="a":
            a = 2*a + 1
        elif i=="b":
            ab = 2*ab + a
        elif i=="c":
            abc = 2*abc + ab
    return abc
print(f"Ans is {get_sub_sequence_dp(string)} with moves {total_dp_moves} in recursion")
