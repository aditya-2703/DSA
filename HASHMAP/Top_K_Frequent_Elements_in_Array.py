# Input:
# nums = {1,1,1,2,2,3},
# k = 2
# Output: {1, 2}

def get_max_element(hashmap):
    max_element=-9999
    flag=False
    for i in  hashmap:
        if hashmap[i]>max_element:
            max_element=i
        if hashmap[i]==max_element:
            flag=True
    return max_element,flag
def Method_1(arr,k):
    n=len(arr)
    result=[0]*k
    hash_table=dict()
    for i in range(n):
        hash_table[arr[i]]=0
    for i in range(n):
        hash_table[arr[i]]+=1
    
    for i in range(k):
        get_max,flag=get_max_element(hash_table)
        if flag==False:
            result[i]=get_max
            del hash_table[get_max]
        else:
            result[i]=max()
    print(result)
if __name__ == '__main__':
    arr=[1,1,1,2,2,3]
    Method_1(arr,2)
    