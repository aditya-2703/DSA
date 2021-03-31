# Input: N = 1
# Output: true
# Explanation: 1 is equal to 2 raised to 0 (20 == 1).

# Input: N = 98
# Output: false
# Explanation: 
# 98 cannot be obtained by any power of 2.

# Method-1 : here we simply do n&(n-1) if it is zero means power of 2 else not 
def Method_1(n):
    if n==0:
        return False
    if n&(n-1)==0:
        return True
    return False


if __name__ == '__main__':
    print(Method_1(256))
    