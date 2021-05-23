# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].


# METHOD 1 -- TAKES O(N**2) TIME AND O(1) SPACE COMPLEXITY
def Method_1(arr,value):
    # brute force solution with the use of two for loops
    for i in range(len(arr)-1):
        firstSum=arr[i]
        for j in range(i+1,len(arr)):
            secondSum=arr[j]
            if firstSum+secondSum==value:
                return [firstSum,secondSum]
    return -1


# METHOD 2 -- TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
def Method_2(arr,value):
    # WITH THE HELP OF Hashable
    hashtable={}
    for i in range(len(arr)):
        if value-arr[i] in hashtable:
            return [value-arr[i],arr[i]]
        else:
            hashtable[arr[i]]=True

# METHOD 3 -- TAKES O(NLOGN) TIME AND O(1) SPACE COMPLEXITY
def Method_3(arr,value):
    # WITH THE HELP OF SORTING
    # HERE WE USE TWO VAR ONE GOES TO LEFT TO RIGHT SECOND ONE GOES TO RIGHT TO LEFT
    # LOGIC IF WE HAVE THREE CONDITIONS : 1. SUM OF RIGHT AND LEFT IS LESS THAN VALUE 2. SUM OF RIGHT AND LEFT IS GREATER THAN VALUE 3. SUM OF RIGHT AND LEFT IS EQUAL TO VALUE WHICH IS OUR ANSWER
    # IF SUM IS LESS THAN OUR ANSWER WE INCREMENT LEFT
    # IF SUM IS GREATER THAN OUR ANSWER WE DECREMENT RIGHT 
    # IF SUM IS EQUAL WE RETURN 
    arr.sort()
    l=0
    r=len(arr)-1
    while l<r:
        if arr[l]+arr[r]==value:
            return [arr[l],arr[r]] 
        elif arr[l]+arr[r]<value:
            l+=1
        else:
            r-=1
    
if __name__ == '__main__':
    arr=[2,7,11,15]
    value=9
    print(Method_1(arr,value))
    print(Method_2(arr,value))
    print(Method_3(arr,value))