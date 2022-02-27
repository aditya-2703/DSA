# Words - K Length Words - 1

# https://nados.io/question/words-k-length-words-1
# 1. You are given a word (may have one character repeat more than once).
# 2. You are given an integer k.
# 3. You are required to generate and print all k length words (of distinct chars) by using chars of the 
#      word.



# uniq characters in level
def get_solution(i,k,uniq_str,ans,counter):
    # when all possible result are reach 
    if i==len(uniq_str):
        # pick our ans ans print
        if counter == k:
            print("".join(ans).replace("0",""))
        return 
    
    # take uniq char
    char = uniq_str[i]
    # put that char to all possible places
    for index in range(len(ans)):
        if ans[index]=="0":
            # mark
            ans[index] = char
            # call
            get_solution(i+1,k,uniq_str,ans,counter+1)
            # unmark
            ans[index] = "0"
    # if we do not include that char
    get_solution(i+1,k,uniq_str,ans,counter)


if __name__ == '__main__':
    string = "aabbbccdde"
    k = 3
    uniq_str= ""
    for i in string:
        if i not in uniq_str:
            uniq_str += i
    ans  = ["0" for i in range(len(uniq_str))]
    get_solution(0,k,uniq_str,ans,0)