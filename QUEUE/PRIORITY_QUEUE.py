class PRIORITY:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        max=0
        for i in range(len(self.queue)):
            if self.queue[i]>=self.queue[max]:
                max=i
        item=self.queue[max]
        del self.queue[max]
        return item
    def printqueue(self):
        print(*self.queue)
if __name__ == '__main__':
    obj=PRIORITY()
    obj.enqueue(11)
    obj.enqueue(12)
    obj.enqueue(31)
    obj.enqueue(14)
    obj.enqueue(15)
    obj.enqueue(81)
    obj.printqueue()
    print(obj.dequeue())
    print(obj.dequeue())
    obj.printqueue()
    