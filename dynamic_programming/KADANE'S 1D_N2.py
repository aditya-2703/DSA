def kadane(arr):
    maxsum=-999898989898989
    n=len(arr)

    for L in  range(n):
        currentsum=0
        for R in range(L,n):
            currentsum+=arr[R]
            maxsum=max(currentsum,maxsum)
    
    return maxsum

if __name__ == '__main__':
    arr=[-2,1,-3,4,-1,2,1,-5,4]
    print(kadane(arr))