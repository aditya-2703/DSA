N = 5
k = 3
arr = [1,2,3,4,5]
# Output: 3 2 1          5 4
                  # 3 
def reverse(arr):
    i=0
    while i<N:
        left=i
        right=min(k+i-1,N-1)

        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        i+=k


reverse(arr)
print(arr)