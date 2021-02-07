# Given an array arr[] of size N, You have to print the arrangement of the array such that upon performing following operations on that arrangement, an increasing order is obtained as the output:

#  Take the first (0th index) element, remove it from the array and print it.
# If there are elements left in the array, move the next top element to the end of the array.
# Repeat the above steps until array is not empty.
# Input:
# First line of input contains a single integer T which denotes the number of test cases. First line of each test case contains a single integer N which denotes the size of the array. Second line of each test case contains N space separated integers denoting values of the array.

# Output:
# For each test case , print the newly arranged array .
# Your Task:
# Complete the function arrangement() which accepts given array as parameter and returns such array when we perform given operations on it , an increasing order of integers is obtained.
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 104
# 1 <= Arr[i] <= 105
# Example:
# Input:
# 2
# 4
# 7 5 2 4 
# 7
# 4 4 5 1 7 2 8 
# Output:
# 2 5 4 7 
# 1 7 2 5 4 8 4 
# Explanation:
# Test Case 1: Performing operations on [ 2 5 4 7 ] , we got [2 4 5 7 ] which is in increasing order.
 


# =========================================================2=============================================


# Given an array of infinite length and two integers M and N which are co-primes, the task is to find the number of positions that cannot be visited starting from the first position 0, when in a single move from arr[i], either arr[i + M] or arr[i + N] can be reached. 
# Note : The largest index X that can’t be obtained using any combination of M & N can be found out using Frobenium Number where X = (M * N) – M – N

# Input:
# First line of input contains number of testcases T. For each testcase, there will be one lines each containing n and m separated by a space.

# Output:
# Print the number of positions that cannot be visited.

# Your Task:
# The task is to complete the function countUnvisited() that takes n and m as input and returns an integer value.

# Constraints: 
# 1 <= T <= 100
# 2 <= N,M <= 500

# Example:
# Sample Input:
# 3
# 2 5
# 2 7
# 25 7

# Sample Output:
# 2
# 3
# 72

# Explanation:
# Testcase 1:
# From index 0, the indices that can be visited are
# 0 + 2 = 2
# 0 + 2 + 2 = 4
# 0 + 5 = 5
# 0 + 2 + 2 + 2 = 6
# 0 + 2 + 5 = 7
# 0 + 2 + 2 + 2 + 2 = 8
# 0 + 2 + 2 + 5 = 9
# 0 + 5 + 5 = 10
# 1 and 3 are the only indices that cannot be visited.