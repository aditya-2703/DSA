def total_ways(string,n,temp):
    result=0
    if n==0 or n==1:
        return 1
    if temp[n]!=0:
        return temp[n]
    if string[n-1]>='0':
        result+=total_ways(string,n-1,temp)
        temp[n]=result
    if 10<=int(string[n-2:n])<=26:
        result+=total_ways(string,n-2,temp)
        temp[n]=result
    return temp[n]

if __name__ == '__main__':
    n=len("231468")
    temp=[0]*(n+1)
    x=total_ways("231468",n,temp)
    print(f"TOTAL WAYS TO DECODE STRING IS {x}")