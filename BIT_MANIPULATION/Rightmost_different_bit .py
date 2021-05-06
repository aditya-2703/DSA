# Input: M = 11, N = 9
# Output: 2
# Explanation: Binary representation of the given 
# numbers are: 1011 and 1001, 
# 2nd bit from right is different.


def Method_1(m,n):
    value=m^n
    count=1
    while value!=0:
        if value&1==1:
            return count
        else:
            count+=1
            value=value>>1
    return 0


if __name__ == '__main__':
    print(Method_1(11,9))
    