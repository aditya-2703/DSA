def knapsack(bag,weight,amount,n):
    matrix=[[0 for i in range(bag+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(bag+1):
            if i==0 or j==0:
                matrix[i][j]=0
            elif weight[i-1]<=bag:
                matrix[i][j]=max(amount[i-1]+matrix[i-1][bag-weight[i-1]],matrix[i-1][j])
            else:
                matrix[i][j]=matrix[i-1][j]
    return matrix
if __name__ == '__main__':
    bag=50
    weight=[30,10,10,40,20]
    amount=[21000,20000,100000,50000,10000]
    mat=knapsack(bag,weight,amount,len(weight))
    for i in mat:
        print(i)