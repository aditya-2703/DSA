# he Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
# Fn = Fn-1 + Fn-2
# with seed values 
# F0 = 0 and F1 = 1.
# Given a number n, print n-th Fibonacci Number. 
# Examples: 
# Input  : n = 2
# Output : 1

# Input  : n = 9
# Output : 34

def fibonacci(n,dp):
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if dp[n]!=0:
        return dp[n]
    value = fibonacci(n-1,dp) + fibonacci(n-2,dp)
    dp[n] = value
    return value
    
if __name__ == '__main__':
    n=5
    dp = [0]*(n+1)
    print(fibonacci(n,dp))
