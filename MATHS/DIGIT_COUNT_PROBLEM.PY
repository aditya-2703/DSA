# METHOD 1: -- time-0(n) space-0(1)

def method_1(val):
    digit_count=0
    while val!=0:
        digit_count+=1
        val=val//10
    return digit_count

# METHOD 2: -- time-0(1) space-0(1) 
from math import *
def method_2(val):
    # floor(log(n)+1)
    return floor(log(val,10)+1)



if __name__ == '__main__':
    print(method_1(56546566453))
    print(method_2(56546566453))