# Words - K Selection - 1

# https://nados.io/question/words-k-selection-1
# 1. You are given a word (may have one character repeat more than once).
# 2. You are given an integer k.
# 2. You are required to generate and print all ways you can select k distinct characters out of the 
#      word.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.

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

def get_solution(start,uniqstr,k,ans,count):
    # base case when index:start reaches to len(uniqstr)
    if start>=len(uniqstr):
        # we only want the k items so print : k
        if k==count:
            print(ans)
        return 
    
    # take character by index
    char = uniqstr[start]
    # if we include that character : call
    get_solution(start+1,uniqstr,k,ans+char,count+1)
    # if we do not include that character : call
    get_solution(start+1,uniqstr,k,ans,count)

if __name__ == '__main__':
    string = "aabbbccdde"
    hashmap = set()
    uniq = ""
    for i in string:
        if i not in hashmap:
            uniq+=i
            hashmap.add(i)
    k = 3
    get_solution(0,uniq,k,"",0)
    