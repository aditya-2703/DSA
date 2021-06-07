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


# --------------------------------------------------------------------------------------------

# Given a Singly Linked List of size N, delete all alternate nodes of the list.

# Example 1:
# Input:
# LinkedList: 1->2->3->4->5->6
# Output: 1->3->5
# Explanation: Deleting alternate nodes
# results in the linked list with elements
# 1->3->5.


# METHOD -1 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# HERE MAKE NEW LINKED LIST AND ONLY INSERT ALTERNATE ELEMENTS
def Method_1(linked_list):
    # for alternate
    index=0 
    curr=linked_list.start
    new_linked_list=Linked_list()
    while curr:
        if index%2==0:
            new_linked_list.add_end(curr.data)
        index+=1
        curr=curr.next
    new_linked_list.print_linked_list()

# METHOD -2 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# here we use two pointer and remove alternate 
def Method_2(linked_list):
    prev=linked_list.start
    curr=linked_list.start.next
    length=linked_list.get_len()
    if length%2!=0:
        while curr.next:
            prev.next=curr.next
            prev=curr
            curr=prev.next
    else:
        while curr:
            prev.next=curr.next
            prev=curr
            curr=prev.next
    linked_list.print_linked_list()
    
    
if __name__ == '__main__':
    linked_list = Linked_list()
    for i in range(1,11):
        linked_list.add_end(i)
    Method_1(linked_list)    
    Method_2(linked_list)

