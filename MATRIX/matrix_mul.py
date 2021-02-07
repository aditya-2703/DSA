a=[[1,2,3],
    [1,2,3],
    [1,2,3]]

b=[[2,3,4],
    [2,3,4],
    [2,3,4]]

result=[[0 for i in range(3)],
        [0 for i in range(3)],
        [0 for i in range(3)]]
    
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in  range(len(a)):
            result[i][j]+=a[i][k]*b[k][j]
print(result)