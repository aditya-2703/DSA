# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

def Method_1(nums):
    nums.sort()
    count=0
    n=len(nums)
    i=0
    j=i+1
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                count+=1
    print(count)
          
if __name__ == '__main__':
    arr=[1,2,3,1,1,3]
    # arr=[1,1,1,1]
    Method_1(arr)
