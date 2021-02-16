# REVERSE LINKED LIST 
# 1-->2-->3-->4-->5
# 5-->4-->3-->2-->1
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.start=None
    def insert_end(self,data):
        node=Node(data)
        if self.start==None:
            self.start=node
            return 
        temp=self.start
        while temp.next:
            temp=temp.next
        temp.next=node
    def print(self):
        temp=self.start
        data=""
        while temp!=None:
            data+=str(temp.data)+"->"
            temp=temp.next
        print(data)
    def Reverse(self):
        curr=self.start
        prev=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.start=prev
if __name__ == '__main__':
    obj=linked_list()

    for i in range(11):
        obj.insert_end(i)
        # obj.print()
    obj.Reverse()
    obj.print()
