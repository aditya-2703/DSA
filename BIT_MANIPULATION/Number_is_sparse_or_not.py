# Input: N = 2
# Output: true
# Explanation: Binary Representation of 2 is 10, 
# which is not having consecutive set bits. 
# So, it is sparse number.


# here will check the two or more consicutive one's 
# METHOD 1 -- TAKES O(N) where N is length of bits TIME AND O(1) COMPLEXITY
def Method_1(n):
    count=0
    for i in bin(n)[2:]:
        if int(i)==1 and count==1:
            return False
        elif int(i)==1:
            count+=1
        else:
            count=0
    return True

# METHOD 2 -- HERE MY SIMPLE LOGIC IS WILL FIRST SET THE ONE'S IN LSB AND THEN PERFORM AND OPERATION WITH 3 BECAUSE 0000 0011 THREE HAS TWO CONSICUTIVE ONE'S SO IF RESULT IS 3 ITSELF BECAUSE OTHER IS ZEROS WHICH DO ZERO'S TO ALL OTHERS AND THAN IT RESULT IS 3 THAN WILL GET OUR ANSWER IF NOT THEN AGAIN PUT THAT ONES IN LSB TAKES O(LOGN) TIME AND O(1) SPACE COMPLEXITY 
def Method_2(n):

    while n!=0:
        if n&1==1:
            res=n&3
            if res==3:
                return False
            else:
                n=n>>2
        else:
            n=n>>1  
    return True




if __name__ == '__main__':
    print(Method_1(1))
    print(Method_2(1))
    