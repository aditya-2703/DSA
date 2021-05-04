# Example 1:

# Input:
# LinkedList: 1->2->2->4->5->6->7->8
# Output: 2 1 4 2 6 5 8 7
# Explanation: After swapping each pair
# considering (1,2), (2, 4), (5, 6).. so
# on as pairs, we get 2, 1, 4, 2, 6, 5,
# 8, 7 as a new linked list.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class List:
    def __init__(self):
        self.start=None
    def make_list(self,data):
        nn=Node(data)
        if self.start==None:
            self.start=nn
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.next=nn
        nn.next=None
    # ---------------------------------------------
    def swap_pair(self):
        count=0
        even_head=even=Node(0)
        odd_head=odd=Node(1)
        temp=self.start
        while temp!=None:
            count+=1
            if count%2==0:
                even.next=temp
                even=even.next
            else:
                odd.next=temp
                odd=odd.next
            temp=temp.next
        print("even head")
        tp=even_head.next
        while tp!=None:
            print(tp.data,end="->")
            tp=tp.next
        print("\nodd head")
        tp=odd_head.next
        while tp!=None:
            print(tp.data,end="->")
            tp=tp.next
    # ----------------------------------------------
    def print_list(self):
        temp=self.start
        s=""
        while temp!=None:
            s+=str(temp.data)+"->"
            temp=temp.next
        s+="None"
        print(s)
if __name__ == '__main__':
    obj=List()
    for i in range(1,7):
        obj.make_list(i)
    obj.print_list()
    obj.swap_pair()