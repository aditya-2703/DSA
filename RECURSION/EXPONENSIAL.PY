  # INPUT a=10 b=2
# OUTPUT 100
# EXPLANATION a**b=100

# base case = a**0 =1 
# METHOD -1 TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
# relation 3**2 = 3*3 likewise a**b=a*a**(b-1) 3**3 = 3*3**(2) = 3*3*3**(1) = 3*3*3**(0) == 3*3*3*1
def Method_1(a,b):
    if b==0:
        return 1
    return a*Method_1(a,b-1)

# METHOD -2 TAKES O(LOGN) TIME AND O(1) SPACE COMPLEXITY

def Method_2(a,b):
    if b==0:
        return 1
    elif b&1==0:
        return Method_2(a,b//2)*Method_2(a,b//2)
    else:
        return a*Method_2(a,b//2)*Method_2(a,b//2)


if __name__ == '__main__':
    a=10
    b=3
    print(Method_1(a,b))
    print(Method_2(a,b))
