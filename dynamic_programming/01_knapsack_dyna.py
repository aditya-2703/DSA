def knapsack(weight,amount,bag_size,n):
    matrix=[[0 for i in range(bag_size+1)] for i in range(n+1)]
    for i in range(n+1):
        for size in range(bag_size+1):
            if size==0 or i==0:
                matrix[i][size]=0
            elif weight[i-1]<=size:
                matrix[i][size]=max(amount[i-1]+matrix[i-1][size-weight[i-1]],matrix[i-1][size])
            else:
                matrix[i][size]=matrix[i-1][size]
    return matrix[n][bag_size]

# Driver program to test above function 
weight=[4,5,1]
amount=[1,2,3]
bag_size=4
n=len(weight)
print(knapsack(weight,amount,bag_size,n))