# Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.
# After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
 
# Example 1:
# Input: n = 34, k = 6
# Output: 9
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

def Method_1(number,base):
  print(bin(54)[2:])
  # print(value , reminder, value+reminder)



if __name__ == '__main__':
    number=34
    base=6
    print(Method_1(number,base))
    