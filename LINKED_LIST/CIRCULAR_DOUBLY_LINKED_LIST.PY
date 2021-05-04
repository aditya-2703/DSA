class node:
    def __init__(self,prev=None,data=None):
        self.next=None
        self.data=data
        self.prev=prev
class Cicular_doubly_linked_list:
    def __init__(self):
        self.start=None
    def insertion_begining(self,data):
        nn=node(None,data)
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
            tmp.next=nn.prev
    def printlinkedlist(self):
        if self.start==None:
            print('LINKED LIST IS EMPTY')
        else:
            tmp=self.start
            s=""
            while tmp.next!=self.start:
                s+=str(tmp.data)+"-->"
                tmp=tmp.next
            s+=str(tmp.data)+"-->NULL"
            print(s)

if __name__ == '__main__':
    obj=Cicular_doubly_linked_list()
    for i in reversed(range(1,5)):
        obj.insertion_begining(i)
    obj.printlinkedlist()
