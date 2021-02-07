def kadane(arr):
    maxsum=end=arr[0]
    n=len(arr)
    for L in range(1,n):
        end=max(end+arr[L],arr[L])
        maxsum=max(end,maxsum)
    return maxsum

if __name__ == '__main__':
    arr=[-2,1,-3,4,-1,2,1,-5,4]
    print(kadane(arr))
    