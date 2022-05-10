# Trie 1
#   -> Insert word 
#   -> Search word
# o(n) time-complexity o(n) space complexity (n is len of word) for both


class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self,root):
        self.root = root

    def is_contains(self,char,root):
        # if is lowercase then 97 ascii
        return char in root.children

    def insert_word_util(self,word,root):
        # if we exhausted all words just return
        if not word:
            root.is_end=True
            return 
        # if the word contains or not contains
        char = word[0]
        rest = word[1:]
        flag =  self.is_contains(char,root)
        # if contains 
        if flag:
            root = root.children[char]
        # if not contains then insert new 
        else:
            new_node=Trie_node(char)
            root.children[char]=new_node
            root = root.children[char]
        # make a call
        self.insert_word_util(rest,root)

    # insert word
    def insert_word(self,word,root):
        self.insert_word_util(word,root)
    
    # search word
    def search_word(self,word,root):
        # if we explore all char in word 
        # last char is also an terminal so we find the word
        for i in word:
            flag = self.is_contains(i,root)
            if flag:
                root = root.children[i]
            else:
                return False
        return root.is_end


if __name__ == '__main__':
    root = Trie_node("R")
    trie_obj = Trie(root) 
    trie_obj.insert_word("hello",root)
    trie_obj.insert_word("hello hi",root)
    trie_obj.insert_word("hell",root)
    trie_obj.insert_word("heyy",root)
    trie_obj.insert_word("horse",root)
    trie_obj.insert_word("application",root)
    trie_obj.insert_word("app",root)
    trie_obj.insert_word("applaus",root)

    is_present = trie_obj.search_word("hello hi",root)
    print(is_present)
    