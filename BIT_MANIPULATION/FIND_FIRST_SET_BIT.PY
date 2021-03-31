# Input: N = 18
# Output: 2
# Explanation: Binary representation of 
# 18 is 010010,the first set bit from the 
# right side is at position 2.

# METHOD-1 : here in this function we know that for lsb , if we want to know whether it is 1 or 0 then will do AND operation with that number so from that logic we simple check and if it is not 1  then right sift that and continue till we find the one's  
def Method_1(n):
    count=0
    if n==0:
        return 0
    while n!=0:
        if n&1==1:
            return count
        else:
            count+=1
            n=n>>1
    


if __name__ == '__main__':
    print(Method_1(12))
    