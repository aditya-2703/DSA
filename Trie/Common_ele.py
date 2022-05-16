# Common Elements

# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118800/offering/1381351?leftPanelTab=1
# Given two 1-dimensional arrays containing strings of lowercase alphabets, print the elements that are common in both the arrays i.e. the strings that are present in both the arrays.
# Note:
# An element of one array can be mapped only to one element of the array. For example :

# Array 1 = {“ab”, “dc”, “ab”, “ab”}
# Array 2 = {“dc”, “ab”, “ab”} 

# The common elements for the above example will be “dc”, “ab”, and “ab”. 

class Trie_node:
	def __init__(self,data=None):
		self.data = data
		self.child = [None]*26
		self.is_end = False
		self.count = 0
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
		curr.count+=1
	def search(self,word):
		curr = self.root
		for i in word:
			index = ord(i) - 97
			if not curr.child[index]:
				return False
			curr = curr.child[index]
		return curr.is_end and curr.count>0
	def dlt(self,word):
		curr = self.root
		for i in word:
			index = ord(i) - 97
			curr = curr.child[index]
			if not curr:
				return 
		curr.count-=1
		if curr.count==0:
			curr.is_end = False

def findCommonElements(arr1, arr2):
	obj = Trie()
	for i in arr1:
		obj.insert(i)
	ans = []
	for i in arr2:
		if obj.search(i):
			ans.append(i)
		obj.dlt(i)
	return ans

if __name__ == '__main__':
    arr1 = ["ab","dc","ab","ab"]
    arr2 = ["dc","ab","ab"]
    ans = findCommonElements(arr1,arr2)
    print(ans)

































#   Fast input.
def takeInput():

    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    arr1 = list(stdin.readline().strip().split(" "))
    arr2 = list(stdin.readline().strip().split(" "))

    return arr1, arr2, n, m


def printAnswer(ans):
    for x in ans:
        print(x, end=" ")
    print()


#   Main.
T = int(stdin.readline().strip())
for i in range(T):
    arr1, arr2, n, m = takeInput()
    ans = findCommonElements(arr1, arr2, n, m)
    printAnswer(ans)
