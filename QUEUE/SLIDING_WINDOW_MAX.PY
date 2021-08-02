# NOTE - THIS SOLUTION IS BASED ON QUEUE THE OTHER ONE WHICH IS BASED ON STACK, YOU CAN VISIT FROM STACK REPO  



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


# METHOD -2 TAKES O(N*LOGK) TIME AND O(K) SPACE COMPLEXITY
# Here will use the concept of priority queue where priority queue by default set priority based on there sorting order means if the number is maximum then it has maximum priority compare to all others
# for priority queue in python 
from queue import PriorityQueue 
def Method_2(arr,k):
    
    result=[]

    # building priority queue of size of k
    pq = PriorityQueue(k)
    for i in range(k):
        pq.put(arr[i])
    # now this first answer will put on our result list
    


# METHOD -3 TAKES O(N) TIME AND O(K) SPACE COMPLEXITY
# Here will use dequeue data structure where will take place of indexes of values with sorting order so that if index is out of window we easily remove that 
from collections import deque
# add first appendleft
# add last  append
# rem first popleft
# rem last  pop
# peek first [0]
# peek last  [-1] 
def Method_3(arr,k):

    result=[]

    dq = deque(maxlen=k)
    # in this loop will find the first window max element and store it in deque
    for i in range(k):
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)

    for i in range(k,len(arr)):
        result.append(arr[dq[0]])
        # check for boundry
        while dq and dq[0]<=i-k:
            dq.popleft()
        # and will continue our steps
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)
    result.append(arr[dq[0]])
    print(result)
    

   

if __name__ == '__main__':
    arr=[4,3,1,2,5,3,4,7,1,9]
    k=4
    # Method_1(arr,k)
    Method_3(arr,k)

    
    