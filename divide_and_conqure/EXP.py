def exponent(a,N):

    if N==0:
        return 1
    if N==1:
        return a
    else:
        R=exponent(a,N//2)
        if N%2==0:
            return R*R
        else:
            return R*a*R     

if __name__ == "__main__":
    j=exponent(100,3)
    print(j)