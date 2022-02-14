# Words - K Selection - 2

# https://nados.io/question/words-k-selection-2
# Sample Input
# aabbbccdde
# 3

# Sample Output
# abc
# abd
# abe
# acd
# ace
# ade
# bcd
# bce
# bde
# cde



def get_solution(i,level,unique_str,k,ans):
    # base case when i reach to k : filled k boxes
    if i>=k:
        print(ans)
        return 
    
    # loop for previous char_pos +1 to n so that repetition not allowed
    for ind in range(level+1,len(unique_str)):
        box = unique_str[ind]
        # call for next pos
        get_solution(i+1,ind,unique_str,k,ans+box)

if __name__ == '__main__':
    string = "aabbccdde"
    k = 3
    hashmap = {}
    unique_str = ""
    for i in string:
        if i not in hashmap:
            hashmap[i] = -1
            unique_str += i
    get_solution(0,-1,unique_str,k,"")
    