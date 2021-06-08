class Node(): 
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list():
    def __init__(self):
        self.start=None
        self.tail=None
    def get_len(self):
        temp=self.start
        count=0
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

    def add_pos(self,value,position):
        index=0 
        prev=None
        curr=self.start
        nn=Node(value)
        while index!=position:
            prev=curr
            curr=curr.next
            index+=1
        prev.next=nn
        nn.next=curr

    def rem_beg(self):
        if self.start==None:
            print("Linked List is empty")
        else:
            temp=self.start
            self.start=temp.next
            temp=None

    def rem_end(self):
        if self.start:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
            self.tail=temp
        else:
            self.isempty()

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

    def reverse(self,head):
        self.start=head
        prev=None
        curr=self.start
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.start=prev
        return self.start
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

# ----------------------------------------------------------------------------------------
# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false

# METHOD -1 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# HERE WE CREATE ANOTHER LINKED LIST AND REVERSE IT AND CHECH ONE BY ONE IF IT IS SAME OR NOT 
def copy(new_ll,original_ll):
    temp=original_ll.start
    while temp:
        new_ll.add_end(temp.data)
        temp=temp.next
def Method_1(linked_list):
    new_linked_list=Linked_list()
    copy(new_linked_list,linked_list)

    # now our new linked list is ready so will reverse it 
    new_linked_list.start=new_linked_list.reverse(new_linked_list.start)
    # now this new linked list is reverse  now so will check

    isPalindrome = True
    New=new_linked_list.start
    Ori=linked_list.start

    while New:
        if New.data==Ori.data:
            New=New.next
            Ori=Ori.next
        else:
            isPalindrome=False
            break
    
    return isPalindrome

# METHOD 2 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# HERE WE SET  OUR POINTER TO MIDDLE AND THEN REVERSE LINKED LIST FROM MIDDLE TO END THEN CHECK WEATHER IT IS PALINDROME OR NOT

def Method_2(linked_list):
    slow=fast=linked_list.start
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    
    curr2=slow.next
    # now my curr2 reversed and now it became 12321 to 12312
    curr2=linked_list.reverse(curr2)
    
    curr1=linked_list.start
    while curr2:
        if curr1.data==curr2.data:
            curr1=curr1.next
            curr2=curr2.next
        else:
            return False
    return True

if __name__ == '__main__':
    arr=[1,2,2,1]
    linked_list=Linked_list()
    for i in arr:
        linked_list.add_end(i)
    print(Method_1(linked_list))
    print(Method_2(linked_list))











