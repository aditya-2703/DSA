# Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. Count distinct triplets in the list that sum up to given integer X.

# Input:The first line of input contains an integer T denoting number of test cases. For each test case, there are two lines of input. First line contains two integers size of linked list( N ) and the value X . Next line contains reversely sorted N integers.

# Output:For each test case, print the count of triplets with given sum X .

# Your Task:You have to complete the function countTriplets() which takes head pointer of sorted linked list and given value X as parameters and returns count of triplets.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 1000
# 1 <= data of a node <= 104
# 1 <= x <= 5000

# Example:
# Input:

# 2
# 7 17
# 9 8 6 5 4 2 1
# 7 15
# 9 8 6 5 4 2 1
# Output:

# 2
# 5
# Explanation:
# Test Case 1:  Head pointer pointing to link list 1-> 2->4->5->6->8->9 , Distinct triplets are ( 2,6,9) and (4,5,8)  which have sum equal to X i.e 17.



# ========================================================2================================================

# Merry and Pippin have invented a new game called String Reduction. A random string S consisting of lowercase albhabets will be given. A player can choose any pair of similar consecutive characters and erase them in his turn. Merry has won the toss so he always goes first. Help decide who is the winner if the first person to give up loses.

# Input:
# First line of input contains number of testcases T. For each testcase, there will be one string input. 

# Output:
# Print the name of the winner. 

# Your Task:
# Complete the function findWinner() that takes the given string S as input and returns the name of the winner. 

# Constraints: 
# 1 <= T <= 100
# 1 <= S.length <= 10^5

# Example:

# Sample Input:
# 3
# tooth
# abc
# aabaab

# Sample Output:
# Pippin
# Pippin
# Merry 

# Explanation:
# Testcase 1:
# Merry will go first and reduce the stirng to tth. 
# Pippin will go second and reduce the string to h.
# Since Merry can not reduce the string any further he loses and Pippin wins. 

# Testcase 2:
# Since the given string can not be reduced any further Merry wont be able to start the game and Pippin will win.