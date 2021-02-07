# Given a link list of size N and an integer K, the task is to rotate the link list clockwise by K places.

# Input:
# First line of input contains number of testcases T. For each testcase, first line of input contains N ie- length of link list. The next line contains N elements. The third line contains the integer K. 

# Output:
# Print the resultant linked list.

# Your Task:
# The task is to complete the function rightRotate() which takes head of link list and K as input and returns the updated head.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 1000
# 1 <= link list element <= 10^5
# 1 <= K <= 10^5

# Example:
# Input:
# 2
# 5
# 1 2 3 4 5 
# 2
# 6
# 7 9 11 13 3 5
# 12

# Output:
# 4 5 1 2 3 
# 7 9 11 13 3 5

# Explaination:
# Testcase 1: 
# Original   : 1 2 3 4 5 
# Rotation 1 : 5 1 2 3 4
# Rotation 2 : 4 5 1 2 3 










# ============================================2========================


# Geek Land has a population of N people and each peron's ability to rule the town is measured by a numeric value X. The two people that can together rule Geek Land must be compatible with each other ie- the sum of digits of their ability X must be equal. Their combined ability should be maximum amongst all the possible pairs of people.
# Find the combined ability of the Ruling Pair.

# Input:
# First line of input contains number of testcases T. For each testcase, there will be 2 lines. First line contains N which denoted the number of people in Geek Land. Second line contains N space separated integers denoting each person's ability X.

# Output:
# Print the combined ability of the Ruling Pair. If no such pair is possible print -1.

# Your Task:
# Complete the function RulingPair() which takes, the list of each person's ability, arr[] and N as inputs and returns the combined ability of the Ruling Pair. Return -1 if no such pair is possible. 

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10^5
# 1 <= arr[i] <= 10^9

# Example:
# Sample Input:
# 2
# 5
# 55 23 32 46 88
# 4
# 18 19 23 15

# Sample Output:
# 101
# -1 

# Explanation:
# Testcase 1:
# All possible pairs that are compatible with each other are- 
# (23, 32) with digit sum 5 
# (55, 46) with digit sum 10 
# Out of these the maximum combined ability pair is (55, 46) i.e. 55 + 46 = 101

# Testcase 2:
# No two people are compatible with each other. 
