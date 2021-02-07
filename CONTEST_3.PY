# Given two strings A and B, find the minimum number of times A has to be stated such that B becomes a substring of the repeated A. If no such solution exists, return -1.

# Input:
# First line of input contains number of testcases T. For each testcase, there will be two lines containing A and B respectively. 

# Output:
# Print the minimum number of times A needs to be repeated. If no solution exists, return -1.

# Your Task:
# Complete the function repeatedStringMatch() that takes strings A and B as input and returns integer output.

# Constraints: 
# 1 <= T <= 100
# 1<= A.length() <= 1000
# 1<= B.length() <= 1000

# Example:
# Sample Input :
# 2
# abcd
# cdabcdab
# aa
# a

# Sample Output :
# 3
# 1

# Explanation : 
# Testcase 1: After repeating A 3 times, we get ‘abcdabcdabcd’. B is now a substring of A.

# Testcase 2: B is already a substring of A and need to be stated only once. 


















# =====================================================2===========================================



# Given an integer array of size  N . You have to find sum of bit differences in all pairs that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.
# For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).

# Input:
# First line of input contains a single integer T denoting number of test cases . For each test case, there will be two lines, first of which containing the size of the array N. Next line contains N space separated integers denoting the elements of the array.
# Output:
# For each test case , print the sum of bit differences in all pairs that can be formed from array .
# Your Task:
# You have to complete the function sumBitDiff() which accepts the given array and its size as parameter and returns sum of bit differences in all pairs that can be formed from array .
# Constraints:
# 1<=T<=100
# 1<=N<=104
# 1<=arr[i]<=108
# Example:
# Input:
# 2
# 2
# 1 2 
# 5
# 3 5 2 5 2
# Output:
# 4
# 36
# Explanation:
# Test Case 1: All possible pairs are [ (1,1) (1,2) (2,1) (2,2) ] their respective Bit differences are 0 ,  2 , 2 , 0

