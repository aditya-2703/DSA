# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
 


# METHOD -2 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY

# HERE WILL USE JUST ONE STACKS AND ONE VARIABLE
# HERE WILL ENCRYPT OUR CURRENT MINIMUM VALUE AND PUSH TO STACK AND WHENEVER WE HAVE TO POP THAT ENCRYPTED VALUE WILL DECRYPT IT
# POP - IF WE HAVE TO POP AND THE VALUE WHICH WILL POP IS ENCRYPTED VALUE THAN WILL POP THAT VALUE AND ALSO DECRYPT IT TO GET PREVIOUS SMALLER ELEMENT
# PUSH - IN PUSH OPERATION WILL PUSH ALL ELEMENT TO NORMAL STACK WHENEVER WILL FIND CURRENT SMALLER ELEMENT THEN WILL ASSIGN IT TO MIN VARIABLE AND PUSH AFTER  ENCRYPTION INTO STACK

# ENCRYPTION - VALUE+(VALUE-MIN)
# DECRYPTION - 2*VALUE - MIN

class Stack:
    def __init__(self):
        # NOMRAL STACK
        self.stack=[]
        # TOP OF NORMAL STACK
        self.top=-1
        # MIN VAR
        self.minele=9999
    # RETURNS TOP OF NORMAL STACK
    def peep(self):
        return self.stack[self.top]
    # RETURN TOP OF MIN STACK
    def push(self,value):
        # IF STACK IS NOT EMPTY
        if self.stack:
            # IF CURR VALUE IS NOT SMALLER 
            if value>=self.minele:
                self.top+=1
                self.stack.append(value)
            # IF CURR VALUE IS SMALLER
            else:
                # encrypt value
                encrypt = value+value-self.minele
                self.top+=1
                self.stack.append(encrypt)
                self.minele=value
        # IF STACK IS EMPTY WE PUSH VALUE TO BOTH MIN AND NORMAL BECAUSE CURRENTLY THERE IS ONLY ONE ELEMENT AND IT IS MINIMUM FOR CURRENT STATE
        else:
            self.top+=1
            self.stack.append(value)
            self.minele = value
    def pop(self):
        # IF STACK IS NOT EMPTY
        if self.stack:
            # NOW WILL HAVE TO DETECT ENCRYPT VALUE HOW ?
            # IF VALUE IS SMALLER THAN CURRENT MINIMUM VALUE THAN THAT IS OUR ENCRYPT VALUE AND WILL DECRYPT IT
            # OTHER WISE MIN STACK GIVES US FALSE RESULT
            if self.peep()<=self.minele:
                # Decrypt
                decrypt = 2*self.minele - self.peep()
                self.stack.pop()
                self.top-=1
                
                # update new min element
                self.minele = decrypt 

            self.top-=1
            self.stack.pop()
        # IF STACK IS EMPTY
        return -1
    
    # IT RETURNS CURRENT MINIMUM VALUE FROM MIN STACK IF IS NOT EMPTY ELSE IT WILL RETURN -1
    def get_min(self):
        if self.stack:
            return self.minele
        return "stack empty"
        

if __name__ == '__main__':
    method_1 = Stack()
    method_1.push(10)
    print(method_1.get_min())
    method_1.push(1)
    print(method_1.get_min())
    method_1.push(0)
    print(method_1.get_min())
    method_1.pop()
    print(method_1.get_min())
    method_1.push(-10)
    print(method_1.get_min())
    method_1.pop()
    print(method_1.get_min())
