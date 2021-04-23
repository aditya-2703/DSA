class InfixToPostfix:
    
    def __init__(self,n):
        self.top=-1
        self.array=[]
        self.output=[]
        self.capacity=n
        self.precidence={'+':1,'-':1,'*':2,'/':2,'^':3}
    def isEmpty(self):
        return True if self.top==-1 else False
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"
    def push(self,element):
        self.top+=1
        self.array.append(element)
    def peek(self):
        return self.array[-1]
    def isnotGreater(self,i):
        try:
            a=self.precidence[i]
            b=self.precidence[self.peek()]
            return True if a<=b else False 
        except KeyError:
            return False
    def isOperand(self,element):
        return element.isalpha()
    def conversion(self,expresion):
        
        for i in expresion:
            if self.isOperand(i):
                self.output.append(i)
            elif i=='(':
                self.push(i)
            elif i==')':
                while ((not self.isEmpty()) and (self.peek()!='(')):
                    a=self.pop()
                    self.output.append(a)
                if ((not self.isEmpty()) and (self.peek()!='(')):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.isnotGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())

        print("".join(self.output))
if __name__ == '__main__':

    exp = "a+b*(c^d-e)^(f+g*h)-i"
    obj=InfixToPostfix(len(exp))
    obj.conversion(exp)



