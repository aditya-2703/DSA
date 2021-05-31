# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
# A subarray is a contiguous subsequence of the array.
# Return the sum of all odd-length subarrays of arr.

# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58



# here we have to observe a pattern 
#  odd even  odd    even      odd
#   1   1,4  1,4,2  1,4,2,5  1,4,2,5,3
#   4   4,2  4,2,5  4,2,5,3
#   2   2,5  2,5,3
#   5   5,3
#   3   

# in this whole odd even area 
# 1 -> odd(1) +  odd(1)  + odd(1) 3 1 comes 3 times total=1*3=1  
# 4 -> odd(1) +  odd(2)  + odd(1) 5 4 comes 4 times total=4*4=16 
# 2 -> odd(1) +  odd(3)  + odd(1) 5 2 comes 5 times total=2*5=10   
# 5 -> odd(1) +  odd(2)  + odd(1) 5 5 comes 4 times total=5*4=20 
# 3 -> odd(1) +  odd(1)  + odd(1) 3 3 comes 3 times total=3*3=9  

# total answer = 1*(3) + 4*(4) + 2*(5) + 5*(4) + 3*(3)
# total answer =58

# so our steps
# first calculate number's frequency then multiply with number

#  / \ / \
# a - b - c 
#     \ /
# so here from a to b there is two path
# from b to c there is 3 path 
# so total number of path from a to c is 2*3 = 6

# so will use this concept here

# start end                           totalstartpath totalendpath
# 0-5   0-0                     i=0         5             0
# 1-5   0-1 1-1                 i=1         4             1
# 2-5   0-2 1-2 2-2             i=2         3             2
# 3-5   0-3 1-3 2-3 3-3         i=3         2             3
# 4-5   0-4 1-4 2-4 3-4 4-4     i=4         1             4
# 5-5   0-5 1-5 2-5 3-5 4-5 5-5 i=5         0             5 
# n-n   0-n 1-n 2-n ....... n-n i=n        n-i            i  

# but this is total occurenece  of number in this odd even sequency but we only want odd so will divide by two
#  totalsequence//2(odd) + totalsequence//2(even) = totalsequence 

# if the array size is even then we easily apply this method because 4//2 = 2 , 8//2 = 4

# but what is array size is odd then there is some problem  occures 3//2 = 1 we miss one occurence so will add it later

  
def Method_1(arr,n):
    result=0
    for i in range(n):
        # we got our end here 
        end=i+1
        # we got our start here
        start=n-i
        # for all posible paths we multiply both
        totalpath=end*start
        # as i told we only want odd  so will divide by 2
        oddpath=totalpath//2
        if totalpath%2!=0:
            oddpath+=1
        result+=oddpath * arr[i]

    return result

if __name__ == '__main__':
    arr=[1,4,2,5,3]
    print(Method_1(arr,len(arr)))
    
