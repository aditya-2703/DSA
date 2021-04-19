class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.start=None
    def push(self,data):
        # insertion at begining
        nn=Node(data)
        if self.start==None:
            self.start=nn
        else:
            nn.next=self.start
            self.start=nn
    def pop(self):
        # deletion at begining
        if self.start==None:
            print("LINKED LIST IS EMPTY")
        else:
            temp=self.start
            self.start=self.start.next
            temp=None

    def print(self):
        if self.start==None:
            print("LINKED LIST IS EMPTY")
        else:
            temp=self.start
            while temp:
                print(str(temp.data)+"\n")
                temp=temp.next

obj=stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
obj.pop()
obj.print()