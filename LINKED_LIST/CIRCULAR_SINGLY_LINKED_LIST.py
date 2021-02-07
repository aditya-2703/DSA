class node:
    def __init__(self,data=None):
        self.next=None
        self.data=data
class Circular_linked_list:
    def __init__(self):
        self.start=None
    def insertion_begining(self,data):
        nn=node(data)
        if self.start==None:
            self.start=nn
            nn.next=self.start
        else:
            tmp=self.start
            while tmp.next!=self.start:
                tmp=tmp.next
            tmp.next=nn
            nn.next=self.start
            self.start=nn
    def insertion_end(self,data):
        nn=node(data)
        if self.start==None:
            self.start=nn
            nn.next=self.start
        else:
            tmp=self.start
            while (tmp.next)!=self.start:
                tmp=tmp.next
            tmp.next=nn
            nn.next=self.start
    def insetion_specific_location(self,pos,data):
        nn=node(data)
        if self.start==None:
            self.start=nn
            nn.next=self.start
        if pos==0:
            print("POSITION STARTS FROM 1")
        else:
            tmp=curr=self.start
            count=1
            while count!=pos:
                curr=tmp
                tmp=tmp.next
                count+=1
            curr.next=nn
            nn.next=tmp
    def remove_begining(self):
        if self.start==None:
            print("LINKED LIST IS ALREADY EMPTY")
        if self.start.next==self.start:
            self.start=None
        else:
            tmp=self.start
            while tmp.next!=self.start:
                tmp=tmp.next
            tmp.next=self.start.next
            self.start=tmp.next 
    def remove_end(self):
        if self.start==None:
            print("LINKED LIST IS ALREADY EMPTY")
        if self.start==self.start.next:
            self.start=None
        else:
            tmp=curr=self.start
            while tmp.next!=self.start:
                curr=tmp
                tmp=tmp.next
            curr.next=self.start
    def remove_specific_location(self,pos):
        if self.start==None:
            print("LINKED LIST IS ALREADY EMPTY")
        if self.start.next==self.start:
            self.start=None
        else:
            tmp=curr=self.start
            count=1
            while count!=pos:
                curr=tmp
                tmp=tmp.next
                count+=1
            curr.next=tmp.next
    def printl(self):
        if self.start==None:
            print("LINKED LIST IS ALREADY EMPTY")
        else:
            s=""
            tmp=self.start
            while tmp.next!=self.start:
                s+=str(tmp.data)+"-->"
                tmp=tmp.next
            s+=str(tmp.data)+"-->NULL"
            print(s)
if __name__ == '__main__':
    obj=Circular_linked_list()
    for i in reversed(range(1,5)):
        obj.insertion_begining(i)
    for i in range(5,10):
        obj.insertion_end(i)
    # obj.insetion_specific_location(3,33)
    # obj.remove_begining()
    # obj.remove_end()
    # obj.remove_end()
    obj.remove_specific_location(3)
    obj.printl()
    