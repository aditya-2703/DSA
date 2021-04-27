# Input: 
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1
# Explanation:
# In the array, the next larger element 
# to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
# since it doesn't exist, it is -1.

def get_max(value,arr):
    for i in  range(len(arr)):
        if arr[i]>value:
            return  arr[i]
    return -1

# METHOD 1 -- TAKES O(N**2) TIME AND O(N) SPACE COMPLEXITY
def Method_1(arr):
    result=[]
    for i in range(len(arr)):
        result.append(get_max(arr[i],arr[i:]))
    return result

# WITH THE HELP OF STACK WILL SOLVE THIS PROBLEM IN O(N) TIME AND O(N) SPACE COMPLEXITY
# steps-->1.pop(always make top max)
#         2.show answer
#         3.push(all time)
class Stack:
    def __init__(self):
        self.top=-1
        self.stack=[]
    def push(self,element):
        self.top+=1
        self.stack.append(element)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1
    def peep(self):
        return self.stack[-1]
def Method_2(arr):
    stack=Stack()
    result=[-1]*len(arr)
    stack.push(arr[-1])
    for i in range(len(arr)-2,-1,-1):
        while(stack.stack and arr[i]>=stack.peep()):
            stack.pop()
        if not stack.stack:
            pass
        else:
            result[i]=stack.peep()
        stack.push(arr[i])
    return result


if __name__ == '__main__':
    arr=[6, 8 ,0 ,1 ,3]
    print(Method_1(arr))
    print(Method_2(arr))
    