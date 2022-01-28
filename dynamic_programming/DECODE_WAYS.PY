# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


string = "22426"
n = len(string)

# with recursion
recursion_moves = 0
def decode_ways_recursion(string,i):
    global recursion_moves
    recursion_moves+=1
    if i==len(string):
        return 1
    first = string[i]
    if first == "0":
        return 0
    
    result = decode_ways_recursion(string,i+1)
    if i+2<=len(string) and int(string[i:i+2]) <= 26:
        result += decode_ways_recursion(string,i+2)
    return result
print(f"Ans is {decode_ways_recursion(string,0)} with moves {recursion_moves} in recursion")

# with dp -- memorization
dp_moves_memo = 0
def decode_ways_dp_memo(string,i,dp):
    global dp_moves_memo
    dp_moves_memo+=1
    if i==len(string):
        return 1
    first = string[i]
    if first == "0":
        return 0
    if dp[i]:
        return dp[i]
    result = decode_ways_dp_memo(string,i+1,dp)
    if i+2<=len(string) and int(string[i:i+2]) <= 26:
        result += decode_ways_dp_memo(string,i+2,dp)
    dp[i]=result
    return result
print(f"Ans is {decode_ways_dp_memo(string,0,[None]*n)} with moves {dp_moves_memo} in memorization")

# with dp -- tabulation
dp_moves_tab = 0
def decode_ways_dp_tab(string,n):
    global dp_moves_tab
    dp = [0]*(n)
    dp[0]=1
    for i in range(1,n):
        dp_moves_tab+=1
        for_last_one_str = dp[i-1]
        for_last_two_str = 1
        if i-2>=0:
            for_last_two_str = dp[i-2]
        # 00
        if dp[i]==0 and dp[i-1]==0:
            dp[i]=0
        # 10 - 231 0 , 23 10
        if dp[i]==0 and dp[i-1]!=0:
            if string[i-1]==1 or string[i-1]==2:
                dp[i] = for_last_two_str
        # 01 - 230 1 , 23 01
        if dp[i]!=0 and dp[i-1]==0:
            dp[i] = for_last_one_str
        # 11 , 22, 33
        else: 
            if int(string[i-1:i+1])<=26:
                dp[i] = for_last_one_str+for_last_two_str
            else:
                dp[i] = for_last_one_str
    return dp[-1]
print(f"Ans is {decode_ways_dp_tab(string,n)} with moves {dp_moves_tab} in memorization")

