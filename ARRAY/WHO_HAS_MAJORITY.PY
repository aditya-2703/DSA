# input - [1,2,2,2,2,2,2,3,3,3,3,4,4,5]
# x=2 y=3
# output - 2
# count 1=1
# count 2=6 --
# count 3=4 --
# count 4=2
# count 5=1
# here out of x(2) and y(3) the count of 2 is max so it return 6  
# if both count is same then return min out of x and y


# METHOD 1 -- 0(n)
def method_1(arr,x,y):
    majorityx=1
    majorityy=1
    x_in=0
    y_in=0
    for i in range(len(arr)):
        if arr[i]==x:
            majorityx+=1
            x_in=arr[i]
            
        if arr[i]==y:
            majorityy+=1
            y_in=arr[i]
        
    if majorityx==majorityy:
        return min(x,y)
    if majorityx>majorityy:
        return x_in
    else:
        return y_in


# METHOD 2
# BINARY SEARCH
# arr=[1,2,2,2,2,2,2,3,3,3,3,4,4,5]
def check_left(arr,l,r,a):
    while l<=r:
        mid = (l+r)//2
        if mid==0 or (arr[mid]==a and arr[mid]>arr[mid-1]) :
                return mid
        elif a>arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1
def check_right(arr,l,r,a):
    n=len(arr)
    while l<=r:
        mid = (l+r)//2
        if mid==n-1  or (arr[mid]==a and arr[mid]<arr[mid+1]):
                return mid
        elif a>arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1
def method_2(arr,x,y):
    x_start=check_left(arr,0,len(arr)-1,x)
    x_end=check_right(arr,0,len(arr)-1,x)
    y_start=check_left(arr,0,len(arr)-1,y)
    y_end=check_right(arr,0,len(arr)-1,y)
    return (x_end-x_start+1,y_end-y_start+1)

if __name__ == '__main__':    
    arr=[1,2,2,2,2,2,2,3,3,3,3,4,4,5]
    print(*method_2(arr,2,3))