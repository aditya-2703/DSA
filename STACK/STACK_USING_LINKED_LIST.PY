# STACK USING LINKED LIST 
# HERE IN ORDER TO IMPLEMENT STACK USING LINKED LIST 
# PUSH --> INSERT FROM FRONT OR BEGINNING
# POP --> REMOVE FROM LAST OR BEGINNING 
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.start=None
    def push(self,value):
        nn=Node(value)
        if self.start==None:
            self.start=nn 
        else:
            nn.next=self.start
            self.start=nn
    def print_stack(self):
        temp=self.start
        list_string=""
        while temp!=None:
            list_string+=str(temp.value)+"->"
            temp=temp.next           
        list_string+="None"
        print(list_string)
    def pop(self):
        if self.start==None:
            return "Linked List is empty"
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            self.start=temp.next
            temp=None

if __name__ == "__main__":
    obj=Stack()
    for i in range(1,11):
        obj.push(i)
    for i in range(9):
        obj.print_linked_list()
        obj.pop()