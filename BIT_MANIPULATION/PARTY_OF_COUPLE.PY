# Party of Couples 
# In a party of N people, each person is denoted by an integer. Couples are represented by the same number. Find out the only singe person in the party of couples.

# Example 1:
# Input: N = 5
# arr = {1, 2, 3, 2, 1}
# Output: 3
# Explaination: Only the number 3 is single.

# METHOD -1 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# here will use hashtable for store the record  with counting of element
def Method_1(array):
  hashtable={}
  for i in array:
    if i in hashtable:
      hashtable[i]+=1
    else:
      hashtable[i]=1
  for i in hashtable:
    if hashtable[i]==1:
      return i

# METHOD -2 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# here will use bit manipulation technique for that we use xor operation
# xor with 0 is never changes the value
# xor operation cuts the duplicate element so will use that 
def Method_2(array):
  result=0
  for i in array:
    result ^= i
  return result

if __name__ == '__main__':
  array=[1, 2, 3, 2, 1]
  print(Method_1(array))
  print(Method_2(array))