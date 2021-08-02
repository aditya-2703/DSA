# NOTE - THIS SOLUTION IS BASED ON STACK THE OTHER ONE WHICH IS BASED ON QUEUE, YOU CAN VISIT FROM QUEUE REPO  



# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
 
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# METHOD - 1 TAKES  O(N*k) TIME AND O(1) SPACE COMPLEXTIY
# Brute-force solution
def Method_1(arr,k):
    result = [0]*(len(arr)-k+1)
    for i in range(len(arr)-k+1):
        curr_max = -9999
        for j in range(i,k+i):
            curr_max = max(curr_max,arr[j])
        result[i]=curr_max
    print(result)


# METHOD -2 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# Here will use the concept of next greater element and fill appropriate result array
def Method_2(arr,k):
    
    # Building next greater element array
    stack=[] 
    n_g_e = [0]*len(arr) 
    n_g_e[-1]=9999
    stack.append(len(arr)-1)
    for i in range(len(arr)-2,-1,-1):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if stack:
            n_g_e[i]=stack[-1]
        else:
            n_g_e[i]=9999
        stack.append(i)
    
    # n g e complete

    result = []
    j=0
    for i in range(len(arr)-k+1):
        if j<i:
            j=i
        # if next greater element is in the window 
        while(n_g_e[j]<i+k):
            j=n_g_e[j]
        result.append(arr[j])

    print(result)

if __name__ == '__main__':
    arr=[1,3,-1,-3,5,3,6,7]
    k=3
    # Method_1(arr,k)
    Method_2(arr,k)

    
    