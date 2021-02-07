# Input: N = 5
# Output: 3
# Explanation: Factorial of 5 is 120.
# Number of digits in 120 is 3 (1, 2, and 0)


# TAKES 0(N) TIME  AND  0(1) SPACE COMPLEXITY
import math
def fact_count(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return int(math.log(fact,10)+1)


if __name__ == '__main__':
    print(fact_count(5))
    