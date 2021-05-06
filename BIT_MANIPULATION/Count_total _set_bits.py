# You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
# Example 1:
# Input: N = 4
# Output: 5
# Explanation:
# For numbers from 1 to 4.
# For 1: 0 0 1 = 1 set bits
# For 2: 0 1 0 = 1 set bits
# For 3: 0 1 1 = 2 set bits
# For 4: 1 0 0 = 1 set bits
# Therefore, the total set bits is 5.

# HERE WILL PERFORM AND OPERATION WITH 1 SO IF THERE IS ONE IT BECAME 1 AND THE TIMES ONE OCCURE IT IS OUR ANSWER
def count_ones(string):
    count=0
    for i in string:
        if i=="1":
            count+=1
    return count

#METHOD-1 TAKES O(NM) TIME AND O(1) SPACE COMPLEXITY WHERE N=INPUT M=LEN_OF_EACH_BITS
def Method_1(n):
    total_count=0
    for i in range(1,n+1):
        total_count+=count_ones(bin(i)[2:])
    return total_count

def get_count(value):
    n=value
    count=0
    while n:
        n&=(n-1)
        count+=1
    return count
#HERE WILL DO N&(N-1) AND RIGHT SHIFT SO THAT IT CHECK LSB AND DO AND WITH 1 SO IF IS 1 THEN 1 ELSE 0
def Method_2(n):
    count=0
    for i in range(1,n+1):
        count+=get_count(i)
    return count

# HERE WILL USE THE PATTERN WHICH APPEAR IN THE BITS FORM
# 1-0001
# 2-0010
# 3-0011
# 4-0100
# 5-0101
# 6-0110
# 7-0111
# --------here there is half zero half one in the form so will first find
# 8-1000
# lowest power of 2  suppose x
# for upper msb zeros fomula: 2**(x-1) * x
# for n-upper values formula: n - (2**(x))+1
# we still has some bits left for that formula: func(n - (2**x))
def lowest_power_of_2(value):
    x=0
    while (1<<x)<=value:
        x+=1
    return x
def Method_3(n):
    if n==0:
        return 0
    x=lowest_power_of_2(n)
    msb_zer=x*(1<<(x-1)) 
    n_upper=n - (1<<x) + 1
    left_bit=Method_3(n-(1<<x))
    return msb_zer+n_upper+left_bit

if __name__ == '__main__':
    print(Method_3(4))