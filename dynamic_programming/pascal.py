def pascal(n,k):
    temp=[[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                temp[i][j]=1
            else:
                temp[i][j]=temp[i-1][j-1]+temp[i-1][j]
    return temp
if __name__ == '__main__':
    list=pascal(5,5)
    for i in list:
        print(*i)