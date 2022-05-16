# Implement a Phone Directory
# https://www.geeksforgeeks.org/implement-a-phone-directory/

# Given a list of contacts which exist in a phone directory. The task is to implement search query for the phone directory. The search query on a string ‘str’ displays all the contacts which prefix as ‘str’. One special property of the search function is that, when a user searches for a contact from the contact list then suggestions (Contacts with prefix as the string entered so for) are shown after user enters each character.
# Note : Contacts in the list consist of only lower case alphabets./
# Example:
# Input : contacts [] = {“gforgeeks” , “geeksquiz” }
#         Query String = “gekk”

# Output : Suggestions based on "g" are 
#          geeksquiz
#          gforgeeks

#          Suggestions based on "ge" are 
#          geeksquiz

#          No Results Found for "gek" 

#          No Results Found for "gekk" 

class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.child = [None]*26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Trie_node("R")
    def insert(self,word):
        curr = self.root
        for i in word:
            index = ord(i) - 97
            if not curr.child[index]:
                curr.child[index]=Trie_node(i)
            curr = curr.child[index]
        curr.is_end=True
    def search(self,word):
        curr = self.root
        for i in word:
            index = ord(i) - 97
            if not curr.child[index]:
                return False
            curr = curr.child[index]
        return curr.is_end
    def get_sugg(self,temp,curr,ans):
        if curr.is_end:
            temp.append(ans)
        for i in curr.child:
            if i:
                ans+=i.data
                self.get_sugg(temp,i,ans)
                ans = ans[:-1]
def phoneDirectory(arr,q):
    # write code here
    obj = Trie()
    for i in arr:
        obj.insert(i)

    prefix = ""
    ans = []
    prev = obj.root
    for i in q:
        index = ord(i) - 97
        prefix+=i
        # if node is null
        if not prev.child[index]:
            break
        # else explore all the node's suggestion and add to ans
        curr = prev.child[index]
        temp = []
        obj.get_sugg(temp,curr,prefix)
        ans.append(temp)
        # update node
        prev = curr 
    return ans
if __name__ == '__main__':
    arr = ["cod" ,"coding","codding" ,"code" ,"coly"]
    qList = "coding"
    ans = phoneDirectory(arr,qList)
    for i in ans:
        print(*i)
