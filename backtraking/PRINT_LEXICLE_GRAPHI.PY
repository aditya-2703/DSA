# Generate all numbers up to N in Lexicographical Order

# https://www.geeksforgeeks.org/generate-all-numbers-up-to-n-in-lexicographical-order/

# Given an integer N, the task is to print all numbers up to N in Lexicographical order.

# Examples: 

# Input: N = 15 
# Output: 
# 1 10 11 12 13 14 15 2 3 4 5 6 7 8 9

# Input: N = 19 
# Output: 
# 1 10 11 12 13 14 15 16 17 18 19 2 3 4 5 6 7 8 9 

# this function make sure that all family which is given as parameter as i is printed
def dfs(i,n):
    if i>n:
        return 
    # print i then
    print(i)
    # again make call for children 
    # like if for 1 the next family is 10 11 12 which is 10*i + j where i is the family which can be 1 to 9 and j is 0 to 9 
    for j in range(0,10):
        dfs(10*i +  j,n)

def get_lexi(n):
    # This loop make sure that family of 1 to 9 is printed
    for j in range(1,10):
        dfs(j,n)

if __name__ == '__main__':
    n = 21
    get_lexi(n)