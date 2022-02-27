# Words - K Selection - 3

# https://nados.io/question/words-k-selection-3?zen=true
# 1. You are given a word (may have one character repeat more than once).
# 2. You are given an integer k.
# 2. You are required to generate and print all ways you can select k characters out of the word.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't force you but the intention is to teach a concept. Play in spirit of the question.


def get_solution_method_1(i,string,hashmap,k,ans):
    # if k<0 means the string is > k
    if k<0:
        return 
    # at base level
    if i>=len(string):
        # if k==0 means we find all combinations
        if k==0:
            print(ans)
        return 
    first = string[i]
    # take one by one each uniqe character
    for char in range(hashmap[first],-1,-1):
        # take the all character string number of it's frequency time
        curr_char = first * char
        # call after taking this curr_char
        get_solution_method_1(i+1,string,hashmap,k-char,ans+f"{curr_char}")


# pick no pick method
# if we pick this character reduce freq
# if we do not pick this character take another one 
def get_solution_method_2(i,uniq_str,hashmap,k,ans):
    if k<0:
        return 
    if i>=len(uniq_str):
        if k==0:
            print(ans)
        return 
    first = uniq_str[i]
    if hashmap[first]>0:
        hashmap[first]-=1
        get_solution_method_2(i,uniq_str,hashmap,k-1,ans+first)
        hashmap[first]+=1
    get_solution_method_2(i+1,uniq_str,hashmap,k,ans)
    

if __name__ == '__main__':
    string = "aabbbccdde"
    k = 3
    uniq_str = ""
    hashmap = {}
    for i in string:    
        if i not in uniq_str:
            uniq_str+=i
            hashmap[i]=1
        else:
            hashmap[i]+=1
    get_solution_method_1(0,uniq_str,hashmap,k,"")
    get_solution_method_2(0,uniq_str,hashmap,k,"")
    