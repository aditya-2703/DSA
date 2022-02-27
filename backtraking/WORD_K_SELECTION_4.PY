# Words - K Length Words - 4

# https://nados.io/question/words-k-length-words-4
# 1. You are given a word (may have one character repeat more than once).
# 2. You are given an integer k.
# 3. You are required to generate and print all k length words by using chars of the word.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't force you but the intention is to teach a concept. Play in spirit of the question.

# spots on level
def get_solution(i,uniq_string,hashmap,k,ans,level):
    # goal case
    if k==0:
        print(ans)
        return 
    
    # for each index till new char to last
    for index in range(level,len(uniq_string)):
        char = uniq_string[index]
        # if freq of char more than 0 
        if hashmap[char]>0:
            # mark
            hashmap[char]-=1
            # call
            get_solution(i+1,uniq_string,hashmap,k-1,ans+char,index)
            # unmark
            hashmap[char]+=1

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
    get_solution(0,uniq_str,hashmap,k,"",0)
    