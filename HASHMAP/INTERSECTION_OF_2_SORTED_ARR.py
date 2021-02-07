# Input: 
# N = 4, arr1[] = {1, 2, 3, 4}  
# M = 5, arr2 [] = {2, 4, 6, 7, 8}
# Output: 2 4
# Explanation: 2 and 4 are only common 
# elements in both the arrays.

# METHOD 1 -- O(N+M) TIME AND O(MAX(MAX(ARR1),MAX(ARR2))) SPACE COMPLEXITY
# HASHING
def Method_1(arr1,arr2):
    result=[]
    hash=[0]*(max(max(arr1)+1,max(arr2)+1))
    
    for i in range(len(arr1)):
        hash[arr1[i]]=1
        
    for j in range(len(arr2)):
        if hash[arr2[j]]==1:
            result.append(arr2[j])
    return result

# METHOD 2 -- 
# DIVIDE AND CONQURE TECHNIQUE
def Method_2(arr1,arr2):
    newarr1=[]
    newarr2=[]
    result=[]
    n=len(arr1)
    m=len(arr2)
    for i in range(n):
        if arr1[i]!=arr1[i-1]:
            newarr1.append(arr1[i])
    for i in range(m):
        if arr2[i]!=arr2[i-1]:
            newarr2.append(arr2[i])
    i=j=0
    while i<len(newarr1) and j<len(newarr2):
        if newarr1[i]<newarr2[j]:
            i+=1
        elif newarr1[i]>newarr2[j]:
            j+=1
        else:
            result.append(newarr2[j])
            j+=1
            i+=1
    return result

if __name__ == '__main__':
    arr1=[1,2,3,4]
    arr2=[2,4,6,7,8]
    print(Method_2(arr1,arr2))
    