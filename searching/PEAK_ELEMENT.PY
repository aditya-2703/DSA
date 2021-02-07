# Input:
# N = 3
# arr[] = {1,2,3}
# Output: 2 
# Explanation: index 2 is 3.
# It is the peak element as it is 
# greater than its neighbour 2.

# METHOD 1 -- O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_1(arr):
    maxval=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxval:
            if i==0 or i==len(arr)-1:
                maxval=arr[i]
            elif arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                maxval=arr[i]

    return maxval

# METHOD 2 -- O(LOGN) TIME AND O(1) SPACE COMPLEXITY 
# BINARY SEARCH METHOD
def Method_2(arr):
    l=0
    r=len(arr)-1
    n=len(arr)
    while l<=r:
        mid=(l+r)//2
        if (mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid
        elif mid>0 and arr[mid-1]>arr[mid]:
            r=mid-1
        else:
            l=mid+1
if __name__ == '__main__':
    arr=[1,1,2,3,1,1]
    print(Method_1(arr))
    print(Method_2(arr))