class Node(): 
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list():
    def __init__(self):
        self.start=None
        self.tail=None
    def get_len(self):
        count=0
        temp=self.start
        while temp:
            count+=1
            temp=temp.next
        return count
    def isempty(self):
        if self.start==None:
            print('Linked list is empty')
    def add_end(self,value):
        nn=Node(value)
        if self.start==None:
            self.start=nn
            self.tail=nn
        else:

            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=nn
            self.tail=nn
    def add_beg(self,value):
        nn=Node(value)
        if self.start==None:
            self.start=nn
        else:
            nn.next=self.start
            self.start=nn
    def rem_pos(self,position):
        index=0
        prev=None
        curr=self.start
        while index!=position:
            prev=curr
            curr=curr.next
            index+=1
        prev.next=curr.next
        curr=None
    def print_linked_list(self):
        if self.start:
            temp=self.start
            linked_list=""
            while temp!=None:
                linked_list+=str(temp.data)+"->"
                temp=temp.next
            linked_list+="None"
            print(linked_list)
        else:
            print("Linked list is empty")

# --------------------------------------------------------------------------------------------------
# Given a single linked list of size M, your task is to complete the function sumOfLastN_Nodes(), which should return the sum of last N nodes of the linked list.
# Input:
# The function takes two arguments as input, the reference pointer to the head of the linked list and the an integer N.
# There will be T test cases and for each test case the function will be called seperately.
# Output:
# For each test case output the sum of last N nodes of the linked list.

# Constraints:
# 1<=T<=100
# 1<=N<=M<=1000

# Example:
# Input:
# 2
# 6 3
# 5 9 6 3 4 10
# 2 2
# 1 2

# Output:
# 17
# 3

# Explanation:
# Testcase 1: Sum of last three nodes in the linked list is 3 + 4 + 10 = 17.


# METHOD -1 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_1(linked_list,k):
    length=linked_list.get_len()
    index=length-k

    # we find our poit from where we have to sum
    point=0
    temp=linked_list.start
    while point!=index:
        temp=temp.next
        point+=1
    
    #now we got our point so simply sum the rest of list element
    result=0
    while temp:
        result+=temp.data
        temp=temp.next 
    print(result)

if __name__ == '__main__':
    arr=[5,9,6,3,4,10]
    k=2
    linked_list=Linked_list()
    for i in arr:
        linked_list.add_end(i)
    Method_1(linked_list,k)