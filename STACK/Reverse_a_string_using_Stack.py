# Example 1:
# the task is to reverse the string using stack.
# Input: S="GeeksforGeeks"
# Output: skeeGrofskeeG



class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop() 


def Method_1(string):
    obj=Stack()
    for i in string:
        obj.push(i)
    result=""
    for i in range(len(string)):
        result+=obj.pop()
    return result

if __name__ == '__main__':
    s="GeeksforGeeks"
    print(Method_1(s))