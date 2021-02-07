# METHOD 1 -- O(n)
def method_1(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True

# METHOD 2 -- O(sqrt(n))
from math import *
def method_2(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
        else:
            return True


# METHOD 3 -- O(sqrt(n))
def method_3(n):
    if n<=1:
        return False
    if n>=2 and n%2==0:
        return False
    sqrt_n=1+sqrt(n)
    for i in range(3,int(sqrt_n),2):
        if n%i==0:
            return False
        else:
            return True

# Method 4 -- O(N* log(log n)) aprox O(n)
# SEIVE method
def Method_4(no):
    arr=[0]*(no+1)
    i=2
    while i*i<=no:    
        if arr[i]==0:
            for i in range(i*i,no+1,i):
                arr[i]=1
        i+=1
    return arr[no]
if __name__ == '__main__':
    print("no is prime") if method_1(123) else print("no is not prime")
    print ("no is prime") if method_2(3456) else print("no is not prime")
    print("no is prime") if method_3(61) else print("no is not prime")
    print("no is prime") if Method_4(3)==0 else print("no is not prime")

    