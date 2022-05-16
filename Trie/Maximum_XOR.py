# Maximum XOR

# https://www.codingninjas.com/codestudio/problems/maximum-xor_973113?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos
# You are given two arrays of non-negative integers say ‘arr1’ and ‘arr2’. Your task is to find the maximum value of ( ‘A’ xor ‘B’ ) where ‘A’ and ‘B’ are any elements from ‘arr1’ and ‘arr2’ respectively and ‘xor’ represents the bitwise xor operation.

# Sample Input 1:
# 1
# 7 7
# 6 6 0 6 8 5 6
# 1 7 1 7 8 0 2

# Sample Output 1:
# 15

# Explanation of sample input 1:
# First testcase:
# Possible pairs are (6, 7), (6, 8), (6, 2), (8, 7), (8, 8), (6, 2). And 8 xor 7 will give the maximum result i.e. 15


# insert all element of arr1 in trie as bit-wise
# traverse from arr2 ele and find oposite bit of that num in trie and add

class Trie_node:
    def __init__(self,data=None):
        self.data = data
        self.link = [None]*2

class Trie:
    def __init__(self):
        self.root = Trie_node("R")
    def insert_num(self,num):
        curr = self.root
        for i in range(31,-1,-1):
            index = (num>>i) & 1
            if not curr.link[index]:
                curr.link[index] = Trie_node(i)
            curr = curr.link[index]
    def find_max(self,xor_value):
        curr = self.root
        max_value = 0
        for i in range(31,-1,-1):
            index = (xor_value>>i) & 1
            opposite  = index ^ 1
            if curr.link[opposite]:
                max_value = max_value | (1<<i)
                curr = curr.link[opposite]
            else:
                curr = curr.link[index]
        return max_value


def maxXOR(n, m, arr1, arr2):
    
    obj = Trie()
    for i in arr1:
        obj.insert_num(i)
    
    max_value = 0
    for i in arr2:
        curr_value = obj.find_max(i)
        max_value = max(max_value,curr_value)
    return max_value

if __name__ == '__main__':
    
    n = 7 
    m = 7
    arr1 = [6, 6, 0, 6, 8, 5, 6]
    arr2 = [1, 7, 1, 7, 8, 0, 2]
    ans = maxXOR(n,m,arr1,arr2)
    print(ans)