def fact(n):
    k=0
    if n==0 or n==1:
       return 1
    else:
        k=n*fact(n-1)
    return k
if __name__ == '__main__':
    print(fact(5))
    # 5 = 120
    # 5*
    