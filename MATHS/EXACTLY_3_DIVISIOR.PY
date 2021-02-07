# Input:
# N = 6
# Output: 1
# Explanation: The only number with 
# 3 divisor is 4.
import math
def prime(value):
    if value==2:
        return True
    for i in range(2,value):
        if value%i==0:
            return False
    return True
def ThreeDiv(value):
    count=0
    for i in range(2,value):
        if (prime(i) and (i*i<=value)):
            count+=1
    return count

if __name__ == '__main__':
    print(ThreeDiv(26))
    

