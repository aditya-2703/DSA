# Example 1:
# Input:
# Stack: 3 2 1
# Output: 1 2 3

class Stack: 
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,value):
        self.top+=1
        self.stack.append(value)
    def pop(self):
        if self.stack:
            self.top-=1
            return self.stack.pop()
    def peep(self):
        return self.stack[self.top]

# METHOD 1 -- TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
def Method_1(stack):
    temp=[i for i in stack]
    temp_stack=Stack()
    for i in range(len(stack)):
        temp_stack.push(temp.pop())
    return temp_stack.stack


def insert_at_bottom(stack,top):
    if not stack:
        stack.append(top)
    else:
        top_ele=stack.pop()
        insert_at_bottom(stack,top)
        stack.append(top_ele)
def reverse(stack):
    if stack:
        temp=stack.pop() 
        reverse(stack)
        insert_at_bottom(stack,temp)
# METHOD 2 -- TAKES O(N**2) TIME AND O(1) (except recursion stack) SPACE COMPLEXITY
def Method_2(stack):
   reverse(stack)
   return stack
if __name__ == '__main__':
    stack=[3,2,1]
    print(Method_1(stack))
    print(Method_2(stack)) 
