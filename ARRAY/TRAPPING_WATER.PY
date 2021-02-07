# Input:
# N = 6
# arr[] = {3,0,0,2,0,4}
# Output: 10
# Explanation:
#               |
# |             |
# |        |    |
# |        |    |
# 3  0  0  2  0  4

def left_most(arr,value):
    maxval=0
    for i in range(value):
        if arr[i]>maxval:
            maxval=arr[i]
    return maxval
def right_most(arr,value):
    maxval=0
    for i in range(value,len(arr)):
        if arr[i]>maxval:
            maxval=arr[i]
    return maxval

# METHOD 1 -- 0(N^2) TIME AND 0(1) SPACE COMPLEXITY
def Method_1(arr,n):
    result=0
    for i in range(n):
        if arr[i]<left_most(arr,i):
            result+=min(left_most(arr,i),right_most(arr,i))-arr[i]    
    return result


# METHOD 2 -- O(N) TIME AND SPACE COMPLEXITY
def Method_2(arr,n):
    left_most=[0]*n
    right_most=[0]*n
    left_most[0]=arr[0]
    result=0
    for i in range(1,n):
        left_most[i]=max(left_most[i-1],arr[i])
    right_most[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right_most[i]=max(right_most[i+1],arr[i])
    for i in range(n):
        result+=min(left_most[i],right_most[i])-arr[i]
    return result
if __name__ == '__main__':
    arr=[1 ,1 ,5 ,2 ,7 ,6 ,1 ,4 ,2 ,3]
    # arr=[8 ,8 ,2 ,4 ,5 ,5 ,1]
    n=len(arr)
    print(Method_1(arr,n))
    print(Method_2(arr,n))
