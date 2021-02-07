# INPUT 
# 2454353454352435345645243435
# 345245334524333455223453454
#OUTPUT
# WHICH IS SUM OF BOTH THE LARGE NUMBERS 
# 2,799,598,788,876,768,800,868,696,889

def Method_1(a,b):
    n=len(a)
    m=len(b)
    i=n-1
    j=m-1
    ans=""
    carry=0
    while i>=0 and j>=0:
        add=int(a[i])+int(b[j])+carry
        if add<10:
            ans+=str(add)
        else:
            carry=add//10
            c=add%10
            ans+=str(c)
    print(ans)


if __name__ == '__main__':
    a=""
    b=""
    print(Method_1(a,b))