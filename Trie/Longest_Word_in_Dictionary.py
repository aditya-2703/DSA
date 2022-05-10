# Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/

# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

# Example 1:
# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".



class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.children = [None]*26
        self.is_end  = False

class Trie:
    def __init__(self):
        self.root = Trie_node("R")

    # insert word
    def insert_word(self,word):
        curr = self.root
        for i in word:
            index = ord(i) - 97
            if curr.children[index]:
                curr= curr.children[index]
            else:
                curr.children[index] = Trie_node(i)
                curr= curr.children[index]
        curr.is_end = True
    # search in word in that manner that every traversal make sure that it's is_end flag is true
    def search_word(self,word):
        curr = self.root
        for i in word:
            index = ord(i)-97
            if (curr.children[index]!=None) and curr.children[index].is_end:
                curr= curr.children[index]
            else:
                return False
        return True

def longestWord(words):
    obj = Trie()    
    ans = ""
    for word in words:
        obj.insert_word(word)
    
    for word in words:
        flag = obj.search_word(word)
        if flag:
            
            if len(ans)<len(word):
                ans = word
            if len(ans)==len(word):
                if word<ans:
                    ans = word
    return ans

if __name__ == '__main__':
    words = ["a","banana","app","appl","ap","apply","apple"]
    print(longestWord(words))