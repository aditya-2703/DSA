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

if __name__ == '__main__':
    arr=[1,2,3,4,5]
    brr=[2,3,4,5,6,7,8]
    print(Method_1(arr,brr,len(arr),len(brr)))
