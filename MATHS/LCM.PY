# LCM=a*b
#     -------
#     GCD(a,b)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

if __name__ == '__main__':
    N=3
    lcm=1
    for i in range(2,N+1):
        lcm=lcm*i // gcd(lcm,i)
    print(lcm)

