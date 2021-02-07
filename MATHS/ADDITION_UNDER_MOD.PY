# Given two numbers a and b, find the sum of a and b. Since the sum can be very large, find the sum modulo 109+7.
# Input:
# a = 9223372036854775807
# b = 9223372036854775807
# Output: 582344006
# Explanation: 
# 9223372036854775807 + 9223372036854775807 
# = 18446744073709551614.
# 18446744073709551614 mod (10**9+7)
# = 582344006

# TAKES 0(1) TIME AND SPACE COMPLEXITY
def mod_cal(a,b):
    result=0
    sum=a+b
    result=sum%(10**9 + 7)
    return result

if __name__ == '__main__':
    a=9223372036854775807
    b=9223372036854775807
    print(mod_cal(a,b))
    