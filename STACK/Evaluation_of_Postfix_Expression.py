# Given string S representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like *, /, + and -.
# Example 1:
# Input: S = "231*+9-"
# Output: -4
# Explanation:
# After solving the given expression, 
# we have -4 as result.

class Postfix_evaluation:
    def __init__(self):
        self.top=-1
        self.stack=[]
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    def push(self,element):
        self.top+=1
        self.stack.append(element)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
    def peep(self):
        return self.stack[-1]
    def isdigit(self,i):
        return i.isdigit()
    def conversion(self,exp):
        for i in exp:
            if self.isdigit(i):
                self.push(int(i))
            else:
                if i=="+":
                    val1=self.pop()
                    val2=self.pop()
                    res=val2+val1
                    self.push(res)
                elif i=="-":
                    val1=self.pop()
                    val2=self.pop()
                    res=val2-val1
                    self.push(res)
                elif i=="*":
                    val1=self.pop()
                    val2=self.pop()
                    res=val2*val1
                    self.push(res)
                elif i=="/":
                    val1=self.pop()
                    val2=self.pop()
                    res=val2//val1
                    self.push(res)
        return self.stack

if __name__ == '__main__':
    expression="231*+9-"
    obj=Postfix_evaluation()
    print(*obj.conversion(expression))

    