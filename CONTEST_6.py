# There are N houses in Geek valley numbered from 1 to N. Geek has installed a special lock system in all the houses where the numeric digits making up the house number are in order of their smallest numeric permutation. 
# How many houses are passcode protected against danger ?

# Input:
# First line of input contains number of testcases T. For each testcase, there will a single input line containing N, the total number of houses in the valley.

# Output:
# Print the total number of houses that are passcode protected.

# Your Task:
# Complete the function passcode_protected() that takes N as input parameter and returns the number of houses that are protected by a lock.

# Constraints: 
# 1 <= T <= 100
# 1 <= N <= (9 x 1017)

# Example:
# Sample Input:
# 2
# 13
# 666

# Sample Output:
# 12
# 200

# Explanation:
# Testcase 1: Total houses in the valley = N = 13.
# House numbers of protected house are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13. 
# House number 10 can not be protected as the smallest permutation of the digits '0' and '1' is 01. 


# ====================================2====================================

# Professor X wants his students to help each other in the chemistry lab. He suggests that every student should help out a classmate who scored less marks than him in chemistry and whose roll number appears after him. But the students are lazy and they don't want to search too far. They each pick the first roll number after them that fits the criteria. Find the marks of the classmate that each student picks. If a student is unable to find anyone print -1.
# Note: one student may be selected by multiple classmates.

# Input:
# First line of input contains number of testcases T. For each testcase, there will be two lines, first of which contains N denoting the number of students in the class. Second line contains N space separated integers denoting the marks of each student roll number wise.

# Output:
# For each roll number, print the marks of the student he choses to help.

# Your Task:
# Complete the function help_classmate() that takes array containing marks and integer N as input parameters and returns a list of integers containing the marks of the classmate that each roll number selects.

# Constraints: 
# 1 <= T <= 100
# 1 <= N <= 10^6

# Example:
# Sample Input:
# 2
# 5
# 3 8 5 2 25 
# 4
# 1 2 3 4 

# Sample Output:
# 2 5 2 -1 -1
# -1 -1 -1 -1 

# Explanation:
# Testcase 1:
# Roll number 1 has 3 marks. The first person who has less marks than him is roll number 4, who has 2 marks.
# Roll number 2 has 8 marks, he helps student with 5 marks.
# Roll number 3 has 5 marks, he helps student with 2 marks.
# Roll number 4 and 5 can not pick anyone as no student with higher roll number has lesser marks than them. This is denoted by -1.
# Output shows the marks of the weaker student that each roll number helps in order. ie- 2,5,2,-1,-1

# Testcase 2:
# As the marks ars in increasing order. None of the students can find a classmate who has a higher roll number and less marks than them.

