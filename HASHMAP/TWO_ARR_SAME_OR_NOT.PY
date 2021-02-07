# Input:
# N = 5
# A[] = {1,2,5,4,0}
# B[] = {2,4,5,0,1}
# Output: 1
# Explanation: Both the array can be 
# rearranged to {0,1,2,4,5}

from collections import defaultdict

# METHOD 1 -- O(N*LOGN) TIME AND O(1)SPACE COMPLEXITY 
def Method_1(arr1,arr2):
    arr1.sort()
    arr2.sort()
    if arr1==arr2:
        return True
    return False

# METHOD 2 -- O(N) TIME ANS O(N) SPACE COMPLEXITY
def Method_2(arr1,arr2):
    hsh=defaultdict(int)#it does not give arror if there is no such element present in array
    for i in arr1:
        hsh[i]=0
    for i in arr1:
        hsh[i]+=1
    print(hsh)
    for j in arr2:
        if hsh[j]==0:
            return False
        else:
            hsh[j]-=1
    return True
if __name__ == '__main__':
    arr1=[1,2,5,4,0]
    arr2=[2,4,5,0,1]
    print(Method_2(arr1,arr2))
    