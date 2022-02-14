# Permutations - Words - 1

# https://nados.io/question/permutations-words-1?zen=true
# 1. You are given a word (may have one character repeat more than once).
# 2. You are required to generate and print all arrangements of these characters. 

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
            #    force you but the intention is to teach a concept. Play in spirit of the question.
# Sample Input
# aabb

# Sample Output
# aabb
# abab
# abba
# baab
# baba
# bbaa


def get_solution(i,n,hashmap,ans):
    # base case when i reach to n 
    if i>=n:
        print(ans)
        return

    # for permutation we use the unique char and put 
    for char in hashmap:
        # if freq more than 0 means we have the char
        if hashmap[char]>0:
            # use the char 
            hashmap[char]-=1
            get_solution(i+1,n,hashmap,char+ans)
            # unmark or backtrack
            hashmap[char]+=1

if __name__ == '__main__':
    string = "aabb"
    hashmap = {word:string.count(word) for word in set(string)}
    get_solution(0,len(string),hashmap,"")
    