# Words - K Length Words - 2

# https://nados.io/question/words-k-length-words-2
# 1. You are given a word (may have one character repeat more than once).
# 2. You are given an integer k.
# 3. You are required to generate and print all k length words (of distinct chars) by using chars of the 
#      word.
# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.


def get_solution(i,uniq,uniq_set,ans):
    # base case when i reach to k
    if i>=k:
        print(ans)
        return
    # for each character in uniq string 
    for each_char in uniq:
        # if char is not included in any ans
        if each_char not in uniq_set:
            # mark
            uniq_set.add(each_char)
            # call
            get_solution(i+1,uniq,uniq_set,ans+each_char)
            # unmark
            uniq_set.remove(each_char)
     



if __name__ == '__main__':
    string = "abcabc"
    k = 2
    uniq = ""
    for i in string:
        if i not in uniq:
            uniq+=i
    get_solution(0,uniq,set(),"")
    