# Input: N = 7
# Output: 4
# Explanation: 7 is represented as 111 in 
# binary form. The gray code of 111 is 100, 
# in the binary form whose decimal equivalent 
# is 4.

# bin to grey code conversion
# BIN : 11110000
# GREY CODE: 10101111 
# TECHNIQUE : PUT MSB AS IT IS THEN PERFORM XOR WITH PREVIOUS BITS 
# ----------- 1________
# ----------- 1(1^1)_______
# ----------- 10(1^1)_______
# ----------- 100(1^1)_______
# ----------- 1000(0^1)________
# ----------- 10001(0^0)________
# ----------- 100010(0^0)________
# ----------- 1000100(0^0)________
# so answer is : 10001000


def Method_1(n):
    binary=bin(n)[2:]
    result=""
    result+=binary[0]
    for i in range(1,len(binary)):
        result+=str(int(binary[i])^int(binary[i-1]))
    return int(result,2)

def Method_2(n):
    return n^(n>>1)

if __name__ == '__main__':
    print(Method_1(7))
    print(Method_2(7))