# Input: A = 10, B = 20
# Output: 4
# Explanation:
# A  = 01010
# B  = 10100
# As we can see, the bits of A that need 
# to be flipped are 01010. If we flip 
# these bits, we get 10100, which is B.

# METHOD -1 : here we simply xor both value and find the one's or count the one's 

def Method_1(a,b):
    value=a^b
    count=0
    while value!=0:
        value=value&(value-1)
        count+=1
    return count
if __name__ == '__main__':
    print(Method_1(10,20))
    