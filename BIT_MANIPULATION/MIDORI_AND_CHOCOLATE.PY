# Midori like chocolates and he loves to try different ones. There are N shops in a market labelled from 1 to N and each shop offers a different variety of chocolate. Midori starts from ith shop and goes ahead to each and every shop. But as there are too many shops Midori would like to know how many more shops he has to visit. You have been given L denoting number of bits required to represent N. You need to return the maximum number of shops he can visit.

# Example 1:
# Input: i = 2, L = 3
# Output: 6
# Explanation: There are 3 bits So N = 8
# Hence midori can visit 8 - 2 = 6 more shops.

# METHOD -1 TAKES O(1) TIME AND O(1) SPACE COMPLEXITY
def Method_1(i,l):
  value=1<<l
  result=value-i
  return result

if __name__ == '__main__':
  i=2
  l=3
  print(Method_1(i,l))