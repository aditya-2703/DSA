# Input: N = 4, K = 0
# Output: false
# Explanation: Binary representation of 4 is 100, 
# in which 0th bit from LSB is not set. 
# So, return false

# Input: N = 4, K = 2
# Output: true
# Explanation: Binary representation of 4 is 100, 
# in which 2nd bit from LSB is set. 
# So, return true.


def isKthBitSet(n, k): 
    print(f"initialy   {bin(n)}")
    for i in range(k):
        print(bin(0<<(i)))
    if n & (1 << (k - 1)): 
        print( "SET") 
    else: 
        print("NOT SET") 

 
n = 15
k = 2
isKthBitSet(n, k) 

