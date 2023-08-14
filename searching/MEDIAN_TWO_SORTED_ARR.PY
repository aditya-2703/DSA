# Given two sorted arrays of sizes N and M respectively. The task is to find the median of the two arrays when they get merged.
 
# Example 1:

# Input:
# N = 5, M = 6 
# arr[] = {1,2,3,4,5}
# brr[] = {3,4,5,6,7,8}
# Output: 4
# Explanation: After merging two arrays, 
# elements will be as 1 2 3 3 4 4 5 5 6 7 8
# So, median is 4.
 

# Example 2:

# Input:
# N = 2, M = 3 
# arr[] = {1,2}
# brr[] = {2,3,4}
# Output: 2
# Explanation: After merging two arrays, 
# elements will be as 1 2 2 3 4. So, 
# median is 2.

# METHOD 1 TAKES O(NM) TIME AND O(N+M) SPACE COMPLEXITYer6 
def Method_1(arr,brr,n,m):
    newlist=[]
    j=0
    i=0
    while j<n and i<max(len(arr),len(brr)):
        if arr[j]<=brr[i]:
            newlist.append(arr[j])
            newlist.append(brr[i])
            j+=1
            i+=1
    while j<n:
        newlist.append(arr[j])
        j+=1
    while i<max(len(arr),len(brr)):    
        newlist.append(brr[i])
        i+=1
    return newlist[len(newlist)//2]
    
def Method_2(arr,brr,n,m):
    if m>n: 
        return Method_2(brr,arr,m,n)
    low = 0
    high = n
    total = (n+m+1)//2
    while low<=high:
        mid1 = low+(high-low)//2
        mid2 = total - mid1
        if mid1<n:
            r1 = arr[mid1]
        if mid2<m:
            r2 = brr[mid2]
        if mid1-1>=0:
            l1 = arr[mid1-1]
        if mid2-1>=0:
            l2 = brr[mid2-1]
        if l1<=r2 and l2<=r1:
            if (n1+n2)%2==1:
                return max(l1,l2)/1.0
            return (max(l1,l2)+min(r1,r2))/2.0
        if l1>r2 or l2>r1:
            high =  mid1-1
        else:
            low  = mid1+1
    return -1

if __name__ == '__main__':
    # arr=[1,2,3,4,5]
    # brr=[2,3,4,5,6,7,8]
    arr=[1,3,4,7,10,12]
    brr=[2,3,6,15]
    print(Method_1(arr,brr,len(arr),len(brr)))
    print(Method_2(arr,brr,len(arr),len(brr)))
