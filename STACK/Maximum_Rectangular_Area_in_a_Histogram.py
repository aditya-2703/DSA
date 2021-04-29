# Input:
# N = 7
# arr[] = {6,2,5,4,5,1,6}
# Output: 12

#  __           __
# | |  __  __  | |
# | | | |_| |  | |
# | | | | | |  | |
# | |_| | | |  | |
# | | | | | |__| |
# |_|_|_|_|_|_|_|
#  6 2 5 4 5 1 6

# FOR 6=6*1=6
# FOR 2=2*5=10
# FOR 5=5*1=5
# FOR 4=4*3=12 --->maximum
# FOR 5=5*1=10
# FOR 1=1*7=7
# FOR 6=6*1=6


def get_left(arr,index,value):
    for i in range(index,-1,-1):
        if arr[i]>=value:
            continue
        else:
            return i
    return -1
def get_right(arr,index,value):
    for i in range(index+1,len(arr)):
        if arr[i]>=value:
            continue
        else:
            return i
    return -1
        
# METHOD -1 TAKES O(N**2) TIME AND O(N) SPACE COMPLEXITY
def Method_1(histogram):
    right=[]
    left=[]
    maxarea=-999
    for i in range(len(histogram)):
        right.append(get_right(histogram,i,histogram[i]))
        left.append(get_left(histogram,i,histogram[i]))
    for i in range(len(histogram)):
        width=(right[i]-left[i]-1)*histogram[i]
        if width>maxarea:
            maxarea=width
    return maxarea

class Stack():
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,element):
        self.top+=1
        self.stack.append(element)
    def pop(self):
        if self.stack:
            self.top-=1
            return self.stack.pop()
        return -1
    def peep(self):
        return self.stack[-1]


# METHOD -2 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# here with the use of stack will able to do solve this problem in o(n) time complexity where will use the concept of next greater element problem
def Method_2(histogram):
    stack_obj=Stack()
    maxarea=-9999
   
    stack_obj.push(len(histogram)-1)
    right=[-1]*len(histogram)
    right[-1]=len(histogram)
    # for right boundry
    for i in range(len(histogram)-2,-1,-1):
        while(stack_obj.stack and histogram[i]<histogram[stack_obj.peep()]):
            stack_obj.pop()
        if stack_obj.stack:
            right[i]=stack_obj.peep()
        else:
            right[i]=len(histogram)
        stack_obj.push(i)

    left=[-1]*len(histogram)
    left[0]=-1
    stack_obj=Stack()
    stack_obj.push(0)
    # for left boundry
    for i in range(1,len(histogram)):
        while(stack_obj.stack and histogram[i]<histogram[stack_obj.peep()]):
            stack_obj.pop()
        if stack_obj.stack:
            left[i]=stack_obj.peep()
        else:
            left[i]=-1
        stack_obj.push(i)


    for i in range(len(histogram)):
        width=right[i]-left[i]-1
        area=width*histogram[i]
        if area>maxarea:
            maxarea=area
    return maxarea


if __name__ == '__main__':
    # histogram=[6,2,5,4,5,1,6]
    histogram=[7 ,2, 8, 9, 1 ,3 ,6 ,5]
    print(Method_1(histogram))
    print(Method_2(histogram))