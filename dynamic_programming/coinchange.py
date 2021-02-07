# ================================TOP DOWN=========================================

# METHOD 1 -- TAKES O(N*M) TIME AND O(N*M) SPACE COMPLEXITY
def Method_1(amount,coin):
    matrix=[[0 for i in range(amount+1)]for i in range(len(coin))]
    for i in range(amount+1):
        matrix[0][i]=i
    for i in range(1,len(coin)):
        for j in range(amount+1):
            if coin[i]>j:
                matrix[i][j]=matrix[i-1][j]
            if coin[i]==j:
                matrix[i][j]=1
            else:
                matrix[i][j]=min(matrix[i-1][j],1+matrix[i][j-coin[i]])
    return matrix[len(coin)-1][amount]
# ================================BOTTOM UP======================================

# METHOD 2 -- TAKES O(N*M) TIME AND O(M) SPACE COMPLEXITY
def Method_2(amount,coin):
    size=[amount+1]*(amount+1)#size array amount+1 size ka sare element amount+1
    size[0]=0#initialy 1st element 0
    for i in range(1,len(size)):#loop 1 se last element tk
        if i in coin:#agr i coin me he to simply assign1 because best way is give that 1 coin
            size[i]=1
        elif i not in coin:#agr nai he to
            for j in coin:#loop j one by one coins  
                if i>j:#agr i coin se bada he to ..
                    z=min(size[i-j]+1,size[i])#min way 
                    size[i]=z
    return size[amount]                
if __name__ == '__main__':
    amount=11
    coin=[1,2,5]
    print(Method_1(amount,coin))
    print(Method_2(amount,coin))
            