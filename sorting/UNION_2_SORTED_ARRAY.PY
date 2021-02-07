# Input:
# N = 5, arr1[] = {1, 1, 1, 1, 1}
# M = 5, arr2[] = {2, 2, 2, 2, 2}
# Output: 1 2
# Explanation: Distinct elements including 
# both the arrays are: 1 2.

# TAKES O(M+N) TIME AND O(M+N) SPACE COMPLEXITY
def Method_1(arr1,arr2):
    i=j=k=0
    newarr=list()
    newlist=list()
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            newarr.insert(k,arr1[i])
            i+=1
            k+=1
        else:
            newarr.insert(k,arr2[j])
            j+=1
            k+=1
    while i<len(arr1):
        newarr.insert(k,arr1[i])
        i+=1
        k+=1
    while j<len(arr2):
        newarr.insert(k,arr2[j])
        j+=1
        k+=1
    for i in range(len(newarr)):
        if newarr[i]!=newarr[i-1]:
            newlist.append(newarr[i])
        
    return newlist

if __name__ == '__main__':
    arr1=[1,2,3,4,5,6]
    arr2=[1,2,3,3]
    print(Method_1(arr1,arr2))
    