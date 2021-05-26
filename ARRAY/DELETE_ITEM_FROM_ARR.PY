# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

# METHOD 1 -- TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_1(arr,value):
    i=0
    for j in range(len(arr)):
        if arr[j]!=value:
            arr[i]=arr[j]
            i+=1
        
    return arr

# ------------------------------- OR --------------------------------------------

def Method_2(arr,value):
    i=0
    j=len(arr)-1
    while i<j:
        
        while i<j and arr[j]==value:
            j-=1
        
        if arr[i]==value:
            arr[i],arr[j]=arr[j],arr[i]
        i+=1
    return arr





if __name__ == '__main__':
    arr=[0,1,2,2,3,0,4,2]
    print(Method_1(arr,2))
    print(Method_2(arr,2))
