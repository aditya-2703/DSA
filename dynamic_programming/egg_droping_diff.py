def egg_droping(egg,experiment):
    matrix=[[0 for i in range(egg+1)] for i in range(experiment+1)]
    for i in range(1,experiment+1):
        matrix[i][0]=0
        matrix[i][1]=1
    for i in range(egg+1):
        matrix[1][i]=i    
    for i in range(1,experiment+1):
        for j in range(1,egg+1):
            matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]+1
    return matrix
if __name__ == '__main__':
    egg=3
    experiment=6
    k=egg_droping(egg,experiment)
    for i in k:
        print(i)
    floor=6
    count=0
    for i in range(1,experiment+1):
        for j in range(1,egg+1):
            if k[i][j]==floor:
                count=i
                break
    if count!=0:
        print("THE NUMBER OF EXPERIMENT FOR {} FLOOR IS {}".format(floor,count))
    else:
        print("INVALID")