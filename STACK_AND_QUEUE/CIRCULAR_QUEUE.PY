class Queue:

  def __init__(self,size):
    self.queue=[None for i in range(size)]
    self.size=size
    self.ront=self.rer=-1
  def enqueue(self,unit):
    if (self.rer+1)%self.size==self.ront:
      print("QUEUE IS EMPTY")
    elif self.ront==-1:
      self.ront=0
      self.rer=0
      self.queue[self.rer]=unit
    else:
      self.rer=(self.rer+1)%self.size
      self.queue[self.rer]=unit
  def dequeue(self):
    if self.ront==-1:
      print("QUEUE IS EMPTY")
    elif self.rer==self.ront:
      tmp=self.queue[self.ront]
      self.ront=-1
      self.rer=-1
      return tmp
    else:
      self.ront=(self.ront+1)%self.size
      tmp=self.queue[self.ront]
      return tmp
  def printqueue(self):
    if self.ront==-1:
      print("QUEUE IS EMPTY")
    elif self.rer>=self.ront:
      for i in range(self.ront,self.rer+1):
        print(self.queue[i])
      


if __name__ == '__main__':
  ob=Queue(10)
  for i in range(10):  
    ob.enqueue(i)
  ob.dequeue()
  ob.dequeue()
  ob.dequeue()
  ob.dequeue()
  ob.printqueue()
  
