# Input:
# N = 1
# A[] = {1}
# Output: 1

# Input:
# N = 5
# A[] = {1,3,5,2,2}
# Output: 3
# as elements before it (1+3) = 
# elements after it (2+2).


# METHOD 1 -- time 0(N^2) AND SPACE 0(1) COMPLEXITY
def method_1(arr):
    
    for i in range(len(arr)):
        left=0
        right=0
        for j in range(i):
            left+=arr[j]

        for j in range(i+1,len(arr)):
            right+=arr[j]
        
        if left==right:
            return (i+1)
    return -1


# METHOD 2 -- TIME 0(N) AND SPACE 0(1) COMPLEXITY
def method_2(arr):
    totalsum=0
    leftsum=0
    n=len(arr)
    for i in range(n):
        totalsum+=arr[i]
    for i in range(n):
        totalsum-=arr[i]
        if i>0:
            leftsum+=arr[i-1]
        if leftsum==totalsum:
            return i+1
    return -1

if __name__ == '__main__':
    arr=[1,3,1,2,2]   
    print(method_1(arr))
    print(method_2(arr))
    