# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
 


# METHOD -1 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY

# HERE WILL USE TWO STACKS WHERE ONE IS NORMAL STACK 
# ANOTEHR ONE IS MIN STACK WHERE WE ONLY PUSH CURRENT SMALLER ELEMENT
# POP - IF WE HAVE TO POP AND BOTH TOP OF VALUE OF NORMAL AND MIN STACK ARE EQUAL WILL POP FROM BOTH STACK SO THAT IT NOT GIVES FALSE VALUE 
# PUSH - IN PUSH OPERATION WILL PUSH ALL ELEMENT TO NORMAL STACK BUT PUSHES ONLY CURRENT SMALLER ELEMENT TO MIN STACK SO THAT GET MINIMUM FUNCTION WILL RETURN CURRENT MINIMUM VALUE FROM MIN STACK
from Easy_str import main


class Stack:
    def __init__(self):
        # NOMRAL STACK
        self.stack=[]
        # TOP OF NORMAL STACK
        self.top=-1
        # MIN STACK
        self.minstack=[]
        # TOP OF MIN STACK
        self.minstack_top=-1
    # RETURNS TOP OF NORMAL STACK
    def peep(self):
        return self.stack[self.top]
    # RETURN TOP OF MIN STACK
    def minstack_peep(self):
        return self.minstack[self.minstack_top]
    def push(self,value):
        # IF STACK IS NOT EMPTY
        if self.stack:
            # IF CURR VALUE IS NOT SMALLER 
            if value>=self.minstack_peep():
                self.top+=1
                self.stack.append(value)
            # IF CURR VALUE IS SMALLER
            else:
                self.top+=1
                self.stack.append(value)
                self.minstack_top+=1
                self.minstack.append(value)
        # IF STACK IS EMPTY WE PUSH VALUE TO BOTH MIN AND NORMAL BECAUSE CURRENTLY THERE IS ONLY ONE ELEMENT AND IT IS MINIMUM FOR CURRENT STATE
        else:
            self.top+=1
            self.stack.append(value)
            self.minstack_top+=1
            self.minstack.append(value)
    def pop(self):
        # IF STACK IS NOT EMPTY
        if self.stack:
            # IF WE POP THE SMALLER VALUE WHICH IS PRESENT IN MIN STACK THAN WE HAVE TO REMOVE FROM BOTH MIN STACK AND NORMAL AS WELL
            # OTHER WISE MIN STACK GIVES US FALSE RESULT
            if self.peep()==self.minstack_peep():
                # POP FROM NORMAL STACK
                self.stack.pop()
                self.top-=1
                # POP FROM MIN STACK
                self.minstack.pop()
                self.minstack_top-=1
            self.top-=1
            self.stack.pop()
        # IF STACK IS EMPTY
        return -1
    
    # IT RETURNS CURRENT MINIMUM VALUE FROM MIN STACK IF IS NOT EMPTY ELSE IT WILL RETURN -1
    def get_min(self):
        if self.minstack:
            return self.minstack_peep()
        return -1
        

if __name__ == '__main__':
    method_1 = Stack()
    