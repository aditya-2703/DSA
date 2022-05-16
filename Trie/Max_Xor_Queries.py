# Max Xor Queries.
# https://www.codingninjas.com/codestudio/problems/max-xor-queries_1382020?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos

# You are given an array/list ‘ARR’ consisting of ‘N’ non-negative integers. You are also given a list ‘QUERIES’ consisting of ‘M’ queries, where the ‘i-th’ query is a list/array of two non-negative integers ‘Xi’, ‘Ai’, i.e ‘QUERIES[i]’ = [‘Xi’, ‘Ai’].
# The answer to the ith query, i.e ‘QUERIES[i]’ is the maximum bitwise xor value of ‘Xi’ with any integer less than or equal to ‘Ai’ in ‘ARR’.
# You should return an array/list consisting of ‘N’ integers where the ‘i-th’ integer is the answer of ‘QUERIES[i]’.

# Sample Input 1:
# 2
# 5 2
# 0 1 2 3 4
# 1 3
# 5 6
# 1 1
# 1
# 1 0  

# Sample Output 1:
# 3 7
# -1

# Explanation Of Sample Input 1:
# In the first test case, the answer of query [1, 3] is 3 because 1^2 = 3 and 2 <= 3,  and the answer of query [5, 6] is 7 because  5 ^ 2 = 7 and 2 <= 6.

# In the second test case, no element is less than or equal to 0 in the given array ‘ARR’.



class Trie_node:
    def __init__(self,data=None):
        self.data=data
        self.link = [None]*2
    
class Trie:
    def __init__(self):
        self.root = Trie_node("R")
    def insert_value(self,value):
        curr = self.root
        for i in range(31,-1,-1):
            index = (value>>i)  & 1
            if not curr.link[index]:
                curr.link[index]=Trie_node(i)
            curr = curr.link[index]
    def find_max(self,value):
        curr = self.root
        max_value = 0
        for i in range(31,-1,-1):
            index = (value>>i) & 1
            opposite = index ^ 1
            if curr.link[opposite]:
                max_value |= (1<<i)
                curr = curr.link[opposite]
            else:
                curr = curr.link[index]
        return max_value

def maxXorQueries(arr, query):
    arr.sort()
    hashmap = {}
    for i in range(len(query)):
        hashmap[f"{query[i]}"] = i
    query = sorted(query,key=lambda x: x[1])
    
    obj = Trie()

    i=0
    ans = [0]*len(query)
    for xor_value,limit in query:
        while i<len(arr) and arr[i]<=limit:
            value = arr[i]
            obj.insert_value(value)
            i+=1
        if i==0:
            index = hashmap[f"{[xor_value,limit]}"]
            ans[index] = -1
        else:
            index = hashmap[f"{[xor_value,limit]}"]
            ans[index] = obj.find_max(xor_value)

if __name__ == '__main__':
    arr = [0 ,1 ,2 ,3 ,4]
    query = [[1,3],[5,6]]
    maxXorQueries(arr,query)

    