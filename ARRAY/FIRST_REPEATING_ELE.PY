# Input:
# N = 7
# arr[] = {1, 5, 3, 4, 3, 5, 6}
# Output: 2
# Explanation: 
# 5 is appearing twice and 
# its first appearence is at index 2 
# which is less than 3 whose first 
# occuring index is 3.


def count(arr,element):
    count=0
    for i in range(len(arr)):
        if element==arr[i]:
            count+=1
    return count

# Method 1 -- O(N*N)
def Method_1(arr,n):
    sortedarr=sorted(arr)
    dictionary=dict()
    for i in range(n):
        dictionary[arr[i]]=count(sortedarr,arr[i])
    findin=-1
    for i in range(len(arr)):
        if dictionary[arr[i]]>1:
            return i+1
        else:
            continue
    return findin
    
# Method 2 -- O(N*logn)
def Method_2(arr,n):
    pass
if __name__ == '__main__':
    arr=[1, 5, 3, 4, 3, 5, 6]
    print(Method_1(arr,len(arr)))
    print(Method_2(arr,len(arr)))
    