# Permutations - Words - 2

# https://nados.io/question/permutations-words-2
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


def get_solution(i,string,n,hashmap,ans):
    # base case when i reach to n 
    if i>=n:
        curr_ans = "".join(ans)
        print(curr_ans)
        return

    # for permutation we use the unique char 
    # put char on any location which is not filled 
    char = string[i]
    location = hashmap[char]
    for j in range(location+1,len(ans)):
        if ans[j]=="0":
            hashmap[char] = j
            ans[j] = char
            get_solution(i+1,string,n,hashmap,ans)
            ans[j] = "0"
            hashmap[char] = -1



if __name__ == '__main__':
    string = "aabb"
    hashmap = {word:-1 for word in set(string)}
    get_solution(0,string,len(string),hashmap,["0"]*len(string))
    