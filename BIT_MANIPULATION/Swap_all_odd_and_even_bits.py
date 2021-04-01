# Input: N = 23
# Output: 43
# Explanation: 
# Binary representation of the given number 
# is 00010111 after swapping 
# 00101011 = 43 in decimal.



# Method 1 -- here will use some logic to swap array 
# 1 - we store our even bits 
# 2 - we store our odd bits 
# 3 - because  off swap we shift odd to even (odd bit shifts to right ) 
# 4 - because  off swap we shift even to odd (even bit shifts to left)
# 5 - now will combine both and get result
# --------------------------87654321------------------------------------------------
# ----1 for store even bits 1_0_0_1_ we want some value like 10101010 so it does not affected and we store so the value is A(1010) because of 32 bit no we do AND with AAAAAAAA (even_number & AAAAAAAA)
# ----2 for store odd bits _1_0_0_1 we want some value like  01010101 so it does not affected and we store so the value is 5(0101) because of 32 bit no we do AND with 55555555 (odd_number & 55555555)
# ----3 for swap even bits(even_number>>1)
# ----4 for swap odd bits(1<<odd_number)
# ----5 for combine both will do OR operation (even_number|odd_number)
def Method_1(n):
    even=n & 0xAAAAAAAA
    odd=n & 0x55555555
    odd<<=1
    even>>=1
    result=odd|even
    return result


if __name__ == '__main__':
    print(Method_1(23))
    