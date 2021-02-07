class stack:
    def push(self,data):
        global stack
        stack.append(data)
    def pop(self):
        global stack
        stack.pop()
    def printstack(self):
        for i in stack:
            print(i)

if __name__ == '__main__':
    obj=stack()
    stack=[]
    for i in range(9):
        obj.push(i)
    for i in range(3):
        obj.pop()
    obj.printstack()
        