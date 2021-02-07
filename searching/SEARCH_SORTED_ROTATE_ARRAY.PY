# Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.
# Input:
# N = 9
# A[] = {5 6,7,8,9,10,1,2,3}
# K = 10
# Output: 5
# Explanation: 10 is found at index 5.
# IF NOT FOUND RETURN -1


# METHOD 1 -- O(N) TIME AND O(1) SPACE COMPLEXITY
# LINEAR SEARCH




def Method_1(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return f"ELEMENT FOUND AT INDEX {i}"
    return "ELEMENT NOT EXIST IN THIS ARRAY"
def find_index(arr):
    n=len(arr)
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if (mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid
        elif mid>0 and arr[mid]<=arr[mid-1]:
            right=mid-1
        else:
            left=mid+1  
def binary_search(arr, low, high, key): 
  
    if high < low: 
        return -1
          
    # low + (high - low)/2;     
    mid = (low + high)//2 
      
    if key == arr[mid]: 
        return mid 
    if key > arr[mid]: 
        return binary_search(arr, (mid + 1), high, key); 
    return binary_search(arr, low, (mid -1), key);

# METHOD 2 -- O(LOG N ) TIME AND O(1) SPACE COMPLEXITY
def Method_2(arr,k):
    max_index=find_index(arr)
    n=len(arr)
    first=arr[0]
    index=0
    if max_index==-1:
       index=binary_search(arr,0,n-1,k)
    elif arr[max_index]==k:
        return max_index
    elif k>=first:
        index=binary_search(arr,0,max_index,k)
    else:
        index=binary_search(arr,max_index+1,n-1,k)
    return index

def metho_2(rr,nr,r,unit):
    mi=(nr+r)//2
    
    if nr>r:
        return -1
    if rr[mi]==unit:
        return mi

    if rr[nr]<=rr[mi]:
        if (unit>=rr[nr] and rr[mi]>=unit):
            return metho_2(rr,nr,mi-1,unit)
        else:
            return metho_2(rr,mi+1,r,unit)
    else:
        if (unit>=rr[mi] and rr[r]>=unit):
            return metho_2(rr,mi+1,r,unit)
        else:
            return metho_2(rr,nr,mi-1,unit)


if __name__ == '__main__':
    arr=[1,2,3,5,6,7,8,9,10]
    for i in range(1,11):
        print(metho_2(arr,0,len(arr)-1,i))
    