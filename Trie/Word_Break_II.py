# Word Break II
# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118800/offering/1381354

# Problem Statement
# You are given a non-empty string S containing no spaces’ and a dictionary of non-empty strings (say the list of words). You are supposed to construct and return all possible sentences after adding spaces in the originally given string ‘S’, such that each word in a sentence exists in the given dictionary.
# Note :
# The same word in the dictionary can be used multiple times to make sentences.
# Assume that the dictionary does not contain duplicate words.



class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.child = [None]*26
        self.end = False
class Trie:
    def __init__(self):
        self.root = Trie_node()
    def insert(self,word):
        curr = self.root
        for i in word:
            index = ord(i)-97
            if not curr.child[index]:
                curr.child[index] = Trie_node()
            curr = curr.child[index]
        curr.end = True
    def search(self,word):
        curr = self.root
        for i in word:
            index = ord(i)-97
            if not curr.child[index]:
                return False
            curr = curr.child[index]
        return curr.end
    
    def solve_util(self,ans,query,ans_):
        if not query:
            ans.append(ans_)
            return 
        
        for i in range(len(query)):
            prefix = query[:i+1]
            rest  = query[i+1:]
            if self.search(prefix):
                self.solve_util(ans,rest,ans_+prefix+" ")

    def solve(self,query):
        ans = []
        self.solve_util(ans,query,"")
        return ans
def wordBreak(query,arr):
    obj = Trie()
    for i in arr:
        obj.insert(i)
    result = obj.solve(query)
    return result
if __name__ == '__main__':
    arr = ["god", "is", "now" ,"no" ,"where", "here"]
    query = "godisnowherenowhere"
    
    arr = ["mobile", "samsung", "sam", "sung", "man", "mango" ,"icecream" ,"and" ,"go", "i", "love", "ice", "cream"]
    query = "iloveicecreamandmango"
    ans = wordBreak(query ,arr)
    print(ans)