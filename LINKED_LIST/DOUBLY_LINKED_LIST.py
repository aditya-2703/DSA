class node:
    def __init__(self,data=None,prev=None):
        self.data=data
        self.prev=prev
        self.next=None
class Doublylinkedlist:
    def __init__(self):
        self.start=None
    def insertion_beg(self,data):
        nn=node(data,None)
        if self.start==None:
            self.start=nn
        else:
            nn.next=self.start
            self.start=nn
            self.start.next.prev=nn
    def insertion_end(self,data):
        nn=node(data,None)
        if self.start==None:
            self.start=nn
        else:
            tmp=self.start
            while tmp.next:
                tmp=tmp.next
            tmp.next=nn
            nn.prev=tmp
            nn.next=None
    def insertion_specificlocation(self,pos,data):
        nn=node(data,None)
        count=1
        if pos==0:
            print("POSITION STARTS FROM 1")
        if pos==1:
            nn.next=self.start
            self.start=nn
            self.start.next.prev=nn
        else:
            tmp=curr=self.start
            while count!=pos:
                curr=tmp
                tmp=tmp.next
                count+=1
            curr.next=nn
            nn.next=tmp
            nn.prev=curr
            tmp.prev=nn
    def remove_beggining(self):
        if self.start==None:
            print('LINKED LIST IS ALREADY EMPTY')
        if self.start.next==None:
            self.start=None
        else:
            tmp=self.start
            self.start=self.start.next
            self.start.prev=None
            tmp=None
    def remove_end(self):
        if self.start==None:
            print("LINKED LIST IS EMPTY")
        if self.start.next==None:
            self.start=None
        else:
            tmp=self.start
            while tmp.next.next:
                tmp=tmp.next
            tmp.next=None
    def remove_specificposition(self,pos):
        if self.start==None:
            print("LINKED LIST IS EMPTY")
        if pos==1:
            self.start=None
        else:
            count=1
            curr=erl=self.start
            while count!=pos:
                curr=erl
                erl=erl.next
                count+=1
            curr.next=erl.next
            erl.next.prev=curr
    def printlinkedlist(self):
        if self.start==None:
            print("LINKED LIST IS EMPTY")
        else:
            tmp=self.start
            s=""
            while tmp:
                s+=str(tmp.data)+"-->"
                tmp=tmp.next
            s+="NULL"
            print(s)
if __name__ == '__main__':
    obj=Doublylinkedlist()
    for i in reversed(range(1,6)):
        obj.insertion_beg(i)
    for i in range(6,11):
        obj.insertion_end(i)
    obj.insertion_specificlocation(3,33)
    obj.remove_beggining()
    obj.remove_end()
    obj.remove_specificposition(2)
    obj.printlinkedlist()