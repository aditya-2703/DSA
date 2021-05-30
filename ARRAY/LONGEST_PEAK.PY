# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time.

# Exampl
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: here 3 is peak element so it has maximum length of 4 because 1 2 3 1 here strictly decreasing in left side and right side has length of 4

# Exampl
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: here 6 is peak element so it has maximum length of 1 3 5 6 4 here strickly  decreasing in left side and right side has length of 5

# Method -1 takes o(n) time and o(1) space complexity
# here will have to find longest peak 
# so first will check if there is element so that element>prev and element>next
# and if not than we simply increment pointer
# but if we have this type of element than will 
# do this 
# left pointer stratch left side 
# right pointer stratch right side
# and we count our length 
def Method_1(arr):
    result=-999
    # we also have to take care of prev and next element so will start from 1
    i=1
    # as i told we have to take care prev and next element so if we do not take len-1 
    # then it shows array out of bound error
    while i<len(arr)-1:
        
        # it returns true of false so if true there is a peak and if false there is no peak at this time
        isPeak= arr[i]>arr[i-1] and arr[i]>arr[i+1]
        
        # if there is not peak we simply increment i because nothing to do
        if not isPeak:
            i+=1
        
        # if we have peak then we stratch to left till we don't find any disturbance element which break the decreasing order
        left = i-2
        while left>=0 and arr[left]<arr[left+1]:
            left-=1
        
        # here we stratch to right till we don't find any disturbance element which break the decreasing order
        right=i+2
        while right<=len(arr)-1 and arr[right]<arr[right-1]:
            right+=1
        
        # we have our left sratch and right stratch so calculate our current length
        currentLen=right-left-1
        
        # and we keep track of our result so that it finds maximum peak
        result= max(result,currentLen)
        # here we know that the one who disturbing decreasing order is right element so we don't need to go previous so we skip to right and start from right.
        i=right
    
    return result



if __name__ == '__main__':
    
    arr=[1,2,1,3,5,6,4]
    print(Method_1(arr))

