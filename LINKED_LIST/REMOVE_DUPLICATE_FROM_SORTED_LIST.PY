class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.start=None
        self.tail=None
    def get_len(self):
        count=0
        temp=self.start
        while temp:
            temp=temp.next
            count+=1
        return count
    def add_beg(self,data):
        nn=Node(data)
        if self.start==None:
            self.start=nn
            self.tail=nn
        else:
            nn.next=self.start
            self.start=nn
    def add_end(self,value):
        nn=Node(value)
        if self.start==None:
            self.start=nn
            self.tail=nn
        else:
            temp=self.start
            while temp.next:
                temp=temp.next
            temp.next=nn
            self.tail=nn
    def rem_beg(self):
        if self.start==None:
            print("linked list empty")
        else:
            temp=self.start
            self.start=self.start.next
            temp=None
    def rem_end(self):
        if self.start==None:
            print("linked list empty")
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            self.tail=temp
    def print_linked_list(self):
        temp=self.start
        while temp:
            print(temp.data,end="->")
            temp=temp.next
# ---------------------------------------------------------------------------
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# METHOD -1 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# HERE WE MAKE AN NEW LINKED LIST AND INSERT THE DULICATE ELEMENT
def Method_1(linked_list):
    New_linked_list=Linked_list()
    New_linked_list.add_end(linked_list.start.data)

    curr1=linked_list.start.next
    curr2=New_linked_list.start

    while curr1:
        if curr1.data!=curr2.data:
            New_linked_list.add_end(curr1.data)
            curr2=curr2.next
        curr1=curr1.next

    New_linked_list.print_linked_list()

# METHOD -2 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# HERE WE APPLY SAME APPROACH WHICH WE SAW ABOVE BUT WE DO NOT CREATE AN  NEW LINKED LIST INSTEAD OF THAT WE DO ALL OPERATIONS IN ONE LINKED LIST
def Method_2(linked_list):
    prev=linked_list.start
    curr=linked_list.start.next

    while curr:
        if prev.data!=curr.data:
            prev.next=curr
            curr=curr.next
            prev=prev.next
        else:
            curr=curr.next
    # this is for it we have [......,3,3,3,3,3] and prev point to 3 then current has not pointer because it reach to end so we just connect prev with current
    # so it became prev.next=curr  .....3->None
    prev.next=curr
    linked_list.print_linked_list()
if __name__ == '__main__':
    linked_list=Linked_list()
    arr=[0,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
    for i in arr:
        linked_list.add_end(i)
    Method_1(linked_list) 
    Method_2(linked_list)