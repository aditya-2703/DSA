class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist():
    def __init__(self):
        self.start=None
    def insertion_beg(self,data):
        node=Node(data,self.start)
        self.start=node
    def insertion_end(self,data):
        if self.start==None:
            nn=Node(data,None)
            return 
    
        curr=self.start
        while curr.next:
            curr=curr.next
        curr.next=Node(data,None)
    def insertion_position(self,data,pos):
        if self.start==None:
            print("HERE LINKED LIST IS EMPTY NOW YOUR UPDATED LIST IS ")
            nn=Node(data,None)
        if pos==1:
            nn=Node(data,self.start)
            self.start=nn
        
        count=1
        curr=self.start
        while curr.next:
            count+=1
            curr=curr.next
            if count==pos:
                curr.next=Node(data,curr.next)
    def remove_beg(self):
        if self.start==None:
            print("LIST IS ALREADY EMPTY")
        if self.start.next == None:
            self.start=None    
        else:
            temp=self.start
            self.start=self.start.next
            temp=None
    def remove_end(self):
        curr=prev=self.start
        while curr.next:
            prev=curr
            curr=curr.next
        prev.next=None
    def remove_position(self,pos):
        
        if self.start==None:
            print("LIST IS ALREADY EMPTY")
        if self.start.next==None:
            self.start=None
        if pos==0:
            print("POSITION COUNT START FROM 1")
        else:
            curr=prev=self.start
            count=1
            while curr.next:
                prev=curr
                curr=curr.next
                count+=1
                if count==pos:
                    prev.next=curr.next
    def printl(self):
        if self.start==None:
            print("LINKED LIST IS EMPY")
        curr=self.start
        s=""
        while curr:
            s+=str(curr.data)+"-->"
            curr=curr.next
        print(s)
if __name__ == '__main__':
    obj=Linkedlist()
    k=0
    while k!=1:
        print("WHAT YOU WANT TO DO WITH LINKED LIST :\n THE OPTIONS ARE:\t INSERTING NODE (1)\t REMOVING NODE(2)\t CHECK HOW'S YOUR LIST LOOKS LIKE(3)")
        choice=int(input())
        if choice==1:
            print("YOUR CHOICE IS INSERTING NODE TO LINKED LIST: \n(1)INSERTING TO BEGINNING\t(2)INSERTING TO SPECIFIC POSITION\t(3)INSERTING TO END")
            c=int(input())
            if c==1:
                obj.insertion_beg(input())
                z=int(input("(1)CONTINUE OR EXIT(0)"))
                if z==0:
                    k==1
            if c==2:
                obj.insertion_position(input(),int(input()))
                z=int(input("(1)CONTINUE OR EXIT(0)"))
                if z==0:
                    k==1
            if c==3:
                obj.insertion_end(input())
                z=int(input("(1)CONTINUE OR EXIT(0)"))
                if z==0:
                    k==1
            else:
                print("INVALID INPUT")

        elif choice==2:
            print("YOUR CHOICE IS REMOVING NODE TO LINKED LIST:\n(1).REMOVING FROM BEGINING\t(2).REMOVING FROM SPECIFIC POSITION\t(3).REMOVING FROM END")
            c=int(input())
            if c==1:
                obj.remove_beg()
                z=int(input("(1)CONTINUE OR EXIT(0)"))
                if z==0:
                    k==1
            if c==2:
                obj.remove_position(int(input()))
                z=int(input("(1)CONTINUE OR EXIT(0)"))
                if z==0:
                    k==1
            if c==3:
                obj.remove_end()
                z=int(input("(1)CONTINUE OR EXIT(0)"))
                if z==0:
                    k==1
            else:
                print("INVALID INPUT")
        elif choice==3:
            obj.printl()
            z=int(input("(1)CONTINUE OR EXIT(0)"))
            if z==0:
                k==1
        else:
            print("INVALID INPUT")
