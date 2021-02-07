# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 2 1 4 3 5
# Explanation: Array elements after 
# sorting it in wave form are 
# 2 1 4 3 5.


# TAKES O(N) TIME AND 0(1) SPACE COMPLEXITY
def wave(arr,n):
    i=0
    while i<n-1:
        arr[i],arr[i+1]=arr[i+1],arr[i]
        i+=2

if __name__ == '__main__':
    arr=[1,2,3,4,5]
    wave(arr,len(arr))
    for i in arr:
        print(i,end=" ")
    