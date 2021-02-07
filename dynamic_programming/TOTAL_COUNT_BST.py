def total(n):
    result=[0]*(n+1)
    result[0]=result[1]=1
    for i in range(2,n+1):
        for j in range(1,n+1):
            result[i]+=result[i-j]*result[j-1]
    return result[n]
if __name__ == '__main__':
    print(total(15))
    