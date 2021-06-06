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
# Given the head of a linked list, rotate the list to the right by k places.

# ONE-ROTATION: 5->1->2->3->4
# SECOND-ROTATION: 4->5->1->2->3

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# METHOD-1 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_1(linked_list,k):
    # we do k times shifting 
    for i in range(k):
        # delete from last
        value=linked_list.tail.data
        linked_list.rem_end()
        
        # add to begin
        linked_list.add_beg(value)

if __name__ == '__main__':
    linked_list=Linked_list()
    arr=[1,2,3,4,5]
    k=2
    for i in arr:
        linked_list.add_end(i)
    Method_1(linked_list,k)

    temp=linked_list.start
    while temp:
        print(temp.data,end="->")
        temp=temp.next