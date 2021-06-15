# Given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. Find the other two numbers.

# Example 1:
# Input: 
# N = 2
# arr[] = {1, 2, 3, 2, 1, 4}
# Output:
# 3 4 
# Explanation:
# 3 and 4 occur exactly once.

# METHOD -1 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# here will first xor all element and remove all double element except two non repeating
def Method_1(arr):
  total_xor=0
  for i in arr:
    total_xor^=i
  
  ans1=0
  ans2=0
  # now will divide array in two group so that in one group our one non repeating element store and in other one our second non repeating element stores
  # we divide this two group based on their right most set bit 
  # simple formula is 2's complement 
  # value = value & (-value)

  total_xor=total_xor & (-total_xor)
  # one group value & total_xor >0
  # two group value & total_xor <0
  for i in arr:
    if total_xor & i >0:
      ans1^=i
    else:
      ans2^=i
  if ans1>ans2:
    return [ans2,ans1]
  return [ans1,ans2]
if __name__ == '__main__':
  arr=[1, 2, 3, 2, 1, 4]
  print(Method_1(arr))