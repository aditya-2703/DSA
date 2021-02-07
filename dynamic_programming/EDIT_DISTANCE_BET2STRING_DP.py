def func(fromstr,tostr,m,n):
    matrix=[[i for i in range(m+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                matrix[i][j]=j
            elif j==0:
                matrix[i][j]=i
            elif fromstr[i-1]==tostr[j-1]:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=1+min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
    
    return matrix[m-1][n-1]

if __name__ == '__main__':
    string2="benyam"
    string1="ephrem"
    print(func(string1,string2,len(string1),len(string2)))
    