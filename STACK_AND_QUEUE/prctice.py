class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.rear=-1
        self.front=-1
        self.size=size
    def enque(self,element):
        if (self.rear+1)%self.size==self.front:
            print("QUEUE IS ALREADY FULL")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=element
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
    def deque(self):
        if self.front==-1:
            print("QUEUE IS ALREADY EMPTY")
        elif self.front==self.rear: 
            print(f"element {self.queue[self.front]}deleted")
            self.front=-1
            self.rear=-1
        else:
            temp=self.queue[self.front] 
            self.front=(self.front+1)%self.size
            print(f"element {temp} deleted")
    def printqueue(self):
        if self.front==-1:
            print("QUEUE IS EMPTY")
        elif self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
        else:
            for i in range(self.front,self.size):
                print(self.queue[i])
            for i in range(0,self.rear+1):
                print(self.queue[i])
if __name__ == '__main__':
        
    q=Queue(6)
    for i in range(0,5):
        q.enque(i)
    q.deque()
    q.printqueue()