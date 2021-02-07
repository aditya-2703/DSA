# a = 3
# m = 11
# Output: 4
# Explanation: Since (4*3) mod 11 = 1, 4 
# is modulo inverse of 3. One might think,
# 15 also as a valid output as "(15*3)
# mod 11"  is also 1, but 15 is not in 
# ring {0, 1, 2, ... 10}, so not valid.


# TAKES 0(N) TIME ANS 0(1) SPACE COMPLEXITY
def mod_inverse(a,m):
    a=a%m
    for i in range(m):
        if (a*i)%m==1:
            return i
    return -1

if __name__ == '__main__':
    print(mod_inverse(3,11))
    