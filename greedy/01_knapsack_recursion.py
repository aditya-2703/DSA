def knapsack(weight,amount,size,n):
    
    if n==0 or size==0:
        return 0
    if weight[n-1]>size:
        return knapsack(weight,amount,size,n-1)
    else:
        return max(amount[n-1]+knapsack(weight,amount,size-weight[n-1],n-1),knapsack(weight,amount,size,n-1))

if __name__ == '__main__':
    weight=[10,20,30,40,50]
    amount=[100,20,300,40,50]
    size=50
    n=len(weight)
    print(knapsack(weight,amount,size,n))
    