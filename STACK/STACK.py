class stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,data):
        self.top+=1
        self.stack.append(data)
    def pop(self):
        if self.stack:
            self.top-=1
            self.stack.pop()
        return -1
    def peep(self):
        return self.stack[self.top]
    def clear(self):
        n=len(self.stack)
        for i in range(n):
            self.stack.pop()
    def printstack(self):
        for i in self.stack:
            print(i)

if __name__ == '__main__':
    obj=stack()
    for i in range(9):
        obj.push(i)
    for i in range(3):
        obj.pop()
    obj.printstack()
    obj.clear()
    obj.printstack()
