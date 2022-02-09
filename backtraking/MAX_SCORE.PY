# Maximum Score Words Formed by Letters

# Given a list of words, list of  single letters (might be repeating) and score of every character.
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

# Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.

# Recursion include exclude method 
def get_max_score(word_arr,alpha_arr,freq_arr,alpha_score_arr):
    if not word_arr:
        return 0
    
    take_first = word_arr[0]
    rest = word_arr[1:]

    exclude = 0 + get_max_score(rest,alpha_arr,freq_arr,alpha_score_arr)
    
    temp_sum = 0 
    is_valid = True
    for i in take_first:
        index = ord(i) - 97
        if freq_arr[index]==0:
            is_valid = False
        freq_arr[index]-=1
        temp_sum  += int(alpha_score_arr[index])
        
    include = 0
    if is_valid:
        include = temp_sum  + get_max_score(rest,alpha_arr,freq_arr,alpha_score_arr)    

    for i in take_first:
        index = ord(i) - 97
        freq_arr[index]+=1
    
    return max(include,exclude)



if __name__ == '__main__':
    word_count = 4
    word_arr = ["dog" ,"cat" ,"dad" ,"good"]
    alpha_count = 9
    alpha_arr = [ "a" ,"b" ,"c" ,"d" ,"d" ,"d" ,"g" ,"o" ,"o"]
    alphabets_score = "1 0 9 5 0 0 3 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0".split(" ")
    freq_arr = [0]*27
    for i in alpha_arr:
        index = ord(i)-97
        freq_arr[index] += 1

    ans = get_max_score(word_arr,alpha_arr,freq_arr,alphabets_score)
    print(ans)
