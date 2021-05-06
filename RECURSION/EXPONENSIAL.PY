# INPUT a=10 b=2
# OUTPUT 100
# EXPLANATION a**b=100

# base case = a**0 =1 
# relation 3**2 = 3*3 likewise a**b=a*a**(b-1) 3**3 = 3*3**(2) = 3*3*3**(1) = 3*3*3**(0) == 3*3*3*1
def Method_1(a,b):
    if b==0:
        return 1
    return a*Method_1(a,b-1)

if __name__ == '__main__':
    a=110
    b=3
    print(Method_1(a,b))