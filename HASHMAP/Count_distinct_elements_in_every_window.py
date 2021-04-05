# Input:
# N = 7, K = 4
# A[] = {1,2,1,3,4,2,3}
# Output: 3 4 4 3
# Explanation: Window 1 of size k = 4 is
# 1 2 1 3. Number of distinct elements in
# this window are 3. 
# Window 2 of size k = 4 is 2 1 3 4. Number
# of distinct elements in this window are 4.
# Window 3 of size k = 4 is 1 3 4 2. Number
# of distinct elements in this window are 4.
# Window 4 of size k = 4 is 3 4 2 3. Number
# of distinct elements in this window are 3.

# METHOD -1 : TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# here will use hashmap and put evrey record here and then remove it one by one.
def Method_1(n,k,arr):
    hashmap=dict()
    distinc_list=[]
    for i in range(k-1):
        if arr[i] not in hashmap:
            hashmap[arr[i]]=1
        else:
            hashmap[arr[i]]+=1
    i=0
    for j in range(k-1,n):

        # build hashmap with acquire element
        if arr[j] in hashmap:
            hashmap[arr[j]]+=1
        elif arr[j] not in hashmap:
            hashmap[arr[j]]=1
        distinc_list.append(len(hashmap))

        #release hashmap  
        freq=hashmap[arr[i]]
        if freq==1:
            del hashmap[arr[i]]
        else:
            hashmap[arr[i]]=freq-1
        i+=1

    print(distinc_list)    
        
        
    
if __name__=="__main__":
    arr=[1,2,1,3,4,2,3]
    Method_1(len(arr),4,arr)