# Input: 
# N = 4, arr1[] = [1 3 5 7] 
# M = 5, arr2[] = [0 2 6 8 9]
# Output: 
# arr1[] = [0 1 2 3]
# arr2[] = [5 6 7 8 9]
# Explanation: After merging the two 
# non-decreasing arrays, we get, 
# 0 1 2 3 5 6 7 8 9.

# 0(m+n)
def Method_1(arr1,arr2,n,m):
    k=n+m
    result=[0]*k
    i=j=k=0
    while (i<n and j<m):
        if arr1[i]<arr2[j]:
            result[k]=arr1[i]
            i+=1
        else:
            result[k]=arr2[j]
            j+=1
        k+=1
    while i<n:
        result[k]=arr1[i]
        k+=1
        i+=1
    while j<m:
        result[k]=arr2[j]
        k+=1
        j+=1
    arr1=[result[i] for i in range(len(arr1))]
    arr2=[result[i] for i in range(len(arr1),len(result))]
    return arr1,arr2

if __name__ == '__main__':
    arr1=[1,2,3,4,5,6]
    arr2=[0,1,2,3]
    n=len(arr1)
    m=len(arr2)
    arr1,arr2=Method_1(arr1,arr2,n,m)
    print(arr1+arr2)
