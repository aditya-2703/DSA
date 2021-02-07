# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition 
# point where 1 begins.


# METHOD 1 -- O(N) O(1)
# linear manner
def method_1(arr):
    result=-1
    for i in range(len(arr)):
        if arr[i]==1:
            result=i
            break
        else:
            continue
    return result

# METHOD 2 -- O(logn) O(1)
# binary manner
def method_2(arr,l,r):
    
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==0:
            l=mid+1
        elif arr[mid]==1:
            if mid==0 or (mid>0 and arr[mid-1]==0):
                return mid
            r=mid-1
    return -1
if __name__ == '__main__':
    arr=[0,0,0,0,1,1,1]
    print(method_1(arr))
    print(method_2(arr,0,len(arr)-1))
    