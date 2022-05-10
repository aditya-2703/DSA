# Trie 2.0 
#   -> insert word 
#   -> search word
#   -> remove word
#   -> search prefix
#   -> count word occurrence 
#   -> count prefix occurence
#   for each operation it takes o(n) time complexity where n is length of word

class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.children = [None]*26
        self.ends_count = 0
        self.prefix_count = 0 

class Trie:
    def __init__(self,root):
        self.root = root

    def insert_word_util(self,word):
        curr = self.root
        for i in word:
            index = ord(i)-97
            if curr.children[index]!=None:
                # increment prefix count
                curr.children[index].prefix_count+=1
                curr = curr.children[index]
            else:
                new_node = Trie_node(i)
                curr.children[index] = new_node
                # increment prefix count
                new_node.prefix_count+=1
                curr = curr.children[index]
        # increment the ends count
        curr.ends_count+=1

    def search_word_util(self,word):
        curr = self.root
        for i in word:
            index = ord(i)-97
            # if char present 
            if curr.children[index]!=None and curr.children[index].prefix_count>0:
                curr = curr.children[index]
            # if not present
            else:
                return False

        # is last char terminal
        return curr.ends_count>0

    def search_prefix_util(self,prefix):
        curr = self.root
        for i in prefix:
            index = ord(i)-97
            # if char present 
            if curr.children[index]!=None and curr.children[index].prefix_count>0:
                curr = curr.children[index]
            # if not present
            else:
                return False

        # is last char terminal
        return True

    def count_word_occ_util(self,word):
        if not self.search_word(word):
            return 0
        curr = self.root
        for i in word:
            index = ord(i)-97
            curr = curr.children[index]
        
        # return last char terminal ends with count
        return curr.ends_count

    def count_prefix_occ_util(self,prefix):
        if not self.search_prefix(prefix):
            return 0
        curr = self.root
        for i in prefix:
            index = ord(i)-97
            curr = curr.children[index]
        
        # return last char terminal ends with count
        return curr.prefix_count

    def remove_word_util(self,word):
        if not self.search_word(word):
            print("word not present")
            return False
        curr = self.root
        for i in word:
            index = ord(i)-97
            node = curr.children[index]
            node.prefix_count-=1 
            curr = node
        node.ends_count-=1
        return True



    # insert word
    def insert_word(self,word):
        self.insert_word_util(word)

    # search word
    def search_word(self,word):
        return self.search_word_util(word)
    
    # search prefix
    def search_prefix(self,prefix):
        return self.search_prefix_util(prefix)
    
    # count word occurrence
    def count_word_occ(self,word):
        return self.count_word_occ_util(word)
        
    # count prefix occurrence
    def count_prefix_occ(self,prefix):
        return self.count_prefix_occ_util(prefix)
    
    # remove word
    def remove_word(self,word):
        self.remove_word_util(word)


if __name__ == '__main__':
    root = Trie_node("R")
    obj = Trie(root)
    obj.insert_word("samsung")
    obj.insert_word("samsung")
    obj.insert_word("vivo")
    obj.remove_word("vivo")
    print(obj.count_word_occ("samsung"))
    print(obj.count_prefix_occ("viv"))


    