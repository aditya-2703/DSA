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
def set_cyclic_linked_list(linked_list,pos):
    index=0
    temp=linked_list.start
    while index!=pos:
        index+=1
        temp=temp.next  
    # we gotch our temp
    linked_list.tail.next=temp  

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# METHOD 1- TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# HERE WILL USE HASHMAP AND TAKE EACH VISITED NODE IN HASHMAP SO THAT IF SOME NODE REPEAT WE CAN SAY THERE IS A LOOP
def Method_1(linked_list):
    hashtable=[]
    ifLoop=False
    temp=linked_list.start
    result=None
    while temp:
        if temp.data in hashtable:
            ifLoop = True
            result=temp.data
            break
        else:
            hashtable.append(temp.data)
        temp=temp.next
    return ifLoop,result
    
# METHOD 2- TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# IF LINKED LIST DOES NOT HAVE LOOP THEN IF WE TAKE FAST AND SLOW POINTER WHERE SLOW SKIPS ONE AND FAST SKIPS TWO STEPS THEN THEY DON'T MEET BECAUSE LINKED LIST DOES NOT HAVE ANY LOOP SO FAST REACH TO END AND ALWAYS SLOW IS PREVIOUS TO FAST
# BUT ::::: IF THERE IS LOOP IN LINKED LIST AND WE DO THIS APPROACH FAST AND SLOW POINTER SO WHAT HAPPENS IS BECAUSE OF LOOP AT SOME POINT FAST AND SLOW MEETS EACH OTHER YOU CAN MEASUER IT BY YOURSELF  BY TAKING AN EXAMPLE 
# STEPS:
# WE DETECT LOOP BY ABOVE LOGIC
# NOW WE PUT FIRST POINTER TO HEAD OF LINKED LIST
# WE INCREMENT BOTH WHERE BOTH MEETS THAT IS OUR POINT WHERE LOOP STARTS

def Method_2(linked_list):
    slow=linked_list.start.next
    fast=linked_list.start.next.next
    isLoop=True
    while slow!=fast and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    if not fast or not slow:
        isLoop=False
        return isLoop,None
    slow=linked_list.start
    while fast!=slow:
        fast=fast.next
        slow=slow.next
    return isLoop,slow.data

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# SECOND APPROACH FOR O(N) TIME AND O(1) SPACE COMPLEXITY
# AS I TOLD THE LOGIC OF MEETING FAST AND SLOW REMAINS BUT AFTER THAT WHAT WILL DO IS FIRST WE FIND THE LENGTH OF CYCLE HOW WE FIND IT WE KNOW THAT NOW FAST AND SLOW IS ON SAME POINT SO WILL INCREMENT ONE OF THEM TILL IT MEET SECOND ONE AND FIND IT'S LENGTH AND AFTER THAT WILL DO IS WE TAKE TWO POINTER LEFT AND RIGHT WITH LENGTH DIFFERENCE 
# MEANS IF LENGTH IS 5 THEN LEFT POINT TO HEAD AND RIGHT POINT TO 5TH NODE  OF LIST AND INCREMENT BOTH SO AT ONE TIME THEY MEET EACH OTHER AND THAT'S  MEETING POINT IS OUR ANSWER 
# STEPS 
# FIND MEETING POINT
# FIND LENGTH OF CYCLE
# WITH THE HELP OF LEFT AND RIGHT WRAP THE WHOLE CYCLE AND RETURN MEETING POINT
def Method_3(linked_list):
    slow=linked_list.start.next
    fast=linked_list.start.next.next
    isLoop=True
    while slow!=fast and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    if not fast or not slow:
        isLoop=False
        return isLoop,None
    
    # There is a loop so now will find our length of cycle
    cycle_len = 1
    slow=slow.next
    while slow!=fast:
        slow=slow.next
        cycle_len+=1
    # we got our length so now will wrap whole cycle with left and right
    left=linked_list.start
    right=linked_list.start
    index=0
    while index!=cycle_len:
        right=right.next
        index+=1
    while left!=right:
        left=left.next
        right=right.next
    return isLoop,left.data
if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9]
    pos=3
    linked_list=Linked_list()
    for i in arr:
        linked_list.add_end(i)
    # our cyclic linked list is set with this below function
    set_cyclic_linked_list(linked_list,pos)
    
    print(Method_1(linked_list))    
    print(Method_2(linked_list))
    print(Method_3(linked_list))