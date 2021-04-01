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

class Bin_to_Grey:
    def __init__(self,n):
        self.n=n
    def Method_1(self):
        binary=bin(self.n)[2:]
        result=""
        result+=binary[0]
        for i in range(1,len(binary)):
            result+=str(int(binary[i])^int(binary[i-1]))
        return int(result,2)

    def Method_2(self):
        return self.n^(self.n>>1)

class Grey_to_Bin:
    def __init__(self,n):
        self.n=n
    def Method_1(self):
        inv = 0
        while(self.n):
            inv = inv ^ self.n
            self.n = self.n >> 1
        return inv


if __name__ == '__main__':
    obj=Bin_to_Grey(7)
    print(obj.Method_1())
    print(obj.Method_2())

    ob1=Grey_to_Bin(7)
    print(ob1.Method_1())
