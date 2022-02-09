# Word Break

# https://leetcode.com/problems/word-break/
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
 
# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

def get_solution(list_word,string,ans):

    if not string:
        print(ans)
        return 

    for i in range(len(string)):
        prefix = string[:i+1]
        rest = string[i+1:]
        old_ans = ans 
        if prefix in list_word:
            ans = old_ans + prefix+" "
            get_solution(list_word,rest,ans)
            ans = old_ans



if __name__ == '__main__':                
    list_word = ["i", "like", "pep", "coding", "pepper", "eating", "mango", "man" ,"go", "in", "pepcoding"]
    string = "ilikepeppereatingmangoinpepcoding"

    get_solution(list_word,string,"")

    # micro soft hi ring
    # micro soft hiring
    # microsoft hi ring
    # microsoft hiring