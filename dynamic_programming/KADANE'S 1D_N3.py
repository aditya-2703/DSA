def kadane(array):
    maxsum=-9999999999
    n=len(array)
    for L in range(n):
        for R in range(L,n):
            currentsum=0
            for k in range(L,R+1):
                currentsum+=array[k]
            maxsum=max(currentsum,maxsum)
    return maxsum
if __name__ == '__main__':
    array=[-2,1,-3,4,-1,2,1,-5,4]
    print(kadane(array))
    