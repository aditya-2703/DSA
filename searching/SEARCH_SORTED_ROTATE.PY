# Input:
# N = 9
# A[] = {5 6,7,8,9,10,1,2,3}
# K = 10
# Output: 5
# Explanation: 10 is found at index 5.
def findmax(arr,n):
    left=0
    right=n
    mid=-1
    #     arr=[5,6,7,8,9,10,11,12,13]
    while left<right:
        mid=(left+(right-1))//2
        if mid>0:
            if mid<n-1:
                if arr[mid]>(arr[mid+1]):
                    return mid
                elif arr[mid]<arr[mid-1]:
                    right=mid-1
                elif arr[mid]>arr[mid-1]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                return mid    
        else:
            # left not possible
            return mid
    return mid
def binary_search(arr,n,element):
    maxvin=findmax(arr,n)
    left=0
    print(maxvin)
    right=maxvin+1
    while left<right:
        mid=(left+(right-1))//2
        if arr[mid]==element:
            return mid
        elif element>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    left=maxvin+1
    right=n
    while left<right:
        mid=(left+(right-1))//2
        if arr[mid]==element:
            return mid
        elif element>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
if __name__ == '__main__':
    arr=[2,3,4,5,6,7,18]
    n=len(arr)
    element=5
    print(f"FOR ARRAY {arr} {binary_search(arr,n,element)}")
    
    