class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.start=None
    def enque(self,data):
        # insertion at end
        nn=Node(data)
        if self.start==None:
            self.start=nn
        else:
            temp=self.start
            while temp.next:
                temp=temp.next
            temp.next=nn
            nn.next=None
    def deque(self):
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


obj=Queue()
for i in range(6):
    obj.enque(i)
obj.deque()
obj.print()
