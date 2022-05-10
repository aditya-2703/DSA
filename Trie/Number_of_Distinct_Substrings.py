# Count number of Distinct Substring in a String
# https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos
# Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) of the given string. You should implement the program using a trie.

# Examples: 
# Sample Input 1 :
# 2
# sds
# abc

# Sample Output 1 :
# 6
# 7

# Explanation Of Sample Input 1 :
# In the first test case, the 6 distinct substrings are { ‘s’,’ d’, ”sd”, ”ds”, ”sds”, “” }
# In the second test case, the 7 distinct substrings are {‘a’, ‘b’, ‘c’, “ab”, “bc”, “abc”, “” }.



class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.children = [None]*26

class Trie:
    def __init__(self):
        self.root = Trie_node("R")
    def insert_word(self,word):
        curr = self.root
        total_word  = 0
        for i in word:
            index=ord(i)-97
            if curr.children[index]==None:
                total_word+=1
                curr.children[index] = Trie_node(i)
            curr = curr.children[index]
        return total_word
    

def get_sub_count(string):
    obj = Trie()
    n = len(string)
    ans = 1
    for i in range(n):
        for j in range(i+1,n+1):
            substring = string[i:j]
            ans+=obj.insert_word(substring)
    return ans
if __name__ == '__main__':
    string = "abab"
    result = get_sub_count(string)
    print(result)
