def ispossible(arr,subset,taken,bucketno,N,k,curr,end):
    if subset[curr]==bucketno:
        if curr==k-2:
            return True
        return ispossible(arr,subset,taken,bucketno,N,k,curr+1,end)
    for i in range(end,-1,-1):
        if taken[i]:
            continue
        tmp=arr[i]+subset[curr]
        if tmp<=bucketno:
            taken[i]=True
            subset[curr]+=arr[i]
            next=ispossible(arr,subset,taken,bucketno,N,k,curr,i-1)
            
            taken[i]=False
            subset[curr]-=arr[i]
            if next:
                return True
    return False    

def partition(arr,N,k):
    if k==0:  
        return False
    if k==1:
        return True
    if N<k:
        return False
    if sum(arr)%k!=0:
        return False
    subset=[0]*k
    taken=[False]*N
    bucketno=sum(arr)//k
    subset[0]=arr[N-1]
    taken[N-1]=True
    return ispossible(arr,subset,taken,bucketno,N,k,0,N-1)

if __name__ == '__main__':
    arr=[1,1,1,1,1,1,1,1,1] 
    N=len(arr)
    k=3
    if partition(arr,N,k):
        print("YES PARTITION IS VALID")
    else:
        print("PARTITION IS NOT VALID")
    