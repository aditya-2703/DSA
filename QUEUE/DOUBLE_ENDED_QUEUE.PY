# Double ended queue
# is empty
#   - (front == -1) and (rear == -1)
# is full 
#   - (front == 0) and (rear == size-1)
#   - (rear+1 == front)
# insert rear 
#   - check full condition
#   - make both 0 from -1
#   - queue[rear] = data then rear=(rear+1)%size
# remove rear
#   - check empty condition
#   - keep rear -=1
#   - if rear goes to 0 then make it size -1 if there is space 
# remove front 
#   - check empty condition 
#   - keep front+=1 till rear
# insert front 
#   - check full condition 
#   - keep front -=1 till 0 then if there is space make it size-1
class De_queue:
    def __init__(self,size):  
        self.q = ["null"]  * size
        self.front=-1
        self.rear=-1
        self.size = size
    # return true if is empty
    def is_empty(self):
        if (self.front == -1 and self.rear==-1):
            return True
        return False
    # return true if is full
    def is_full(self):
        if (self.front == 0  and self.rear == self.size-1) or (self.rear+1 == self.front):
            return True
        return False
    # print queue
    def print_q(self):
        for i in range(self.size):
            print(self.q[i],end='-')
        print()
    # insert Rear
    def insert_rear(self,value):
        if self.is_full():
            return "Queue is full"
        if self.front == self.rear == -1:
            self.front = self.rear = 0
            self.q[self.rear]=value
        else:
            self.rear = (self.rear+1)%self.size
            self.q[self.rear] = value
    # remove from rear
    def remove_rear(self):
        if self.is_empty():
            return "Queue is empty"
        if self.rear == 0:
            self.q[self.rear]="null"
            self.rear = self.size -1 
        else:
            self.q[self.rear]="null"
            self.rear -= 1
    # insert from front 
    def insert_front(self,value):
        if self.is_full():
            print("Queue is full")
            return 
        if self.front == 0 and self.rear<self.size-1:
            self.front = self.size-1
            self.q[self.front]=value
        else:
            self.front-=1
            self.q[self.front]=value
    # remove from front
    def remove_front(self):
        if self.is_empty():
            print("Queue is empty")
            return 
        else:
            self.q[self.front]="null"
            self.front=(self.front+1)%self.size

if __name__ == '__main__':
    size_of_queue = 5
    obj = De_queue(size_of_queue)
    for i in range(5):
        obj.insert_rear(i)
    obj.print_q()
    obj.remove_front()
    obj.print_q()
    obj.remove_rear()
    obj.print_q()
    obj.insert_rear(4)
    obj.print_q()
    obj.insert_rear(5)
    obj.print_q()
    obj.remove_front()
    obj.print_q()
    obj.remove_front()
    obj.print_q()
    obj.remove_front()
    obj.print_q()