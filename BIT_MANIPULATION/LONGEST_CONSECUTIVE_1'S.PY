# Given a number N. Find the length of the longest consecutive 1s in its binary representation.

# Example 1:
# Input: N = 14
# Output: 3
# Explanation: 
# Binary representation of 14 is 
# 1110, in which 111 is the longest 
# consecutive set bits of length is 3.

# METHOD -1 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_1(n):
  max_count=0
  count=0
  while n!=0:
    if n & 1 == 1:
      count+=1
    else:
      count=0
    max_count=max(max_count,count)
    n=n>>1
  return max_count


if __name__ == '__main__':
    n=222
    print(Method_1(n))