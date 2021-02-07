# we have our coin and our amount we have to find total possible ways to make coins which is equal to the amount 
# input : 1 2 3     5
# output : 5
# explanation : 11111,1112,113,23,32


# METHOD 1  -- TAKES O(2^N) TIME AND O(1) SPACE COMPLEXITY 
def Method_1(coin,n,amount):
    if n<=0 and amount>=1:
        return 0
    if amount==0:
        return 1
    if amount<0:
        return 0
    else:
        return Method_1(coin,n-1,amount)+Method_1(coin,n,amount-coin[n-1])

# METHOD 2 -- TAKES O(N*M) TIME AND O(N*M) SPACE COMPLEXITY(n is len of coin and m is amount)
def Method_2(coin,n,amount):
    matrix=[[0 for i in range(amount+1)]for i in range(n+1)]
    for i in range(n+1):
        matrix[i][0]=1
    for i in range(1,n+1):
        for j in range(amount+1):
            if i>j:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-i]
    return matrix[n][amount]

# METHOD 3 -- TAKES O(N*M) TIME AND O(M) SPACE COMPLEXITY
def Method_3(coin,n,amount):
    arr=[0 for i in range(amount+1)]
    arr[0]=1
    for i in range(n):
        for j in range(coin[i],amount+1):
            arr[j]+=arr[j-coin[i]]
        print(arr)

if __name__ == '__main__':
    coin=[1,2,3]
    # print(Method_1(coin,len(coin),9))
    # print(Method_2(coin,len(coin),9))
    Method_3(coin,len(coin),5)