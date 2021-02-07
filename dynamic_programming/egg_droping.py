max_value=34534535
def egg_droping(egg,floor):
    matrix=[[0 for i in range(floor+1) ]for i in range(egg+1)]        
    for i in range(1,egg+1):
        matrix[i][1]=1
        matrix[i][0]=0
    for i in range(2,floor+1):
        matrix[1][i]=i

    for i in range(2,egg+1):
        for j in range(2,floor+1):
            matrix[i][j]=max_value
            for x in range(1,j+1):
                res=1+max(matrix[i][j-x],matrix[i-1][x- 1])
                if res<matrix[i][j]:
                    matrix[i][j]=res

    return matrix
if __name__ == '__main__':
    egg=3
    floor=6
    k=egg_droping(egg,floor)
    print("THE NUMBER OF EXPERIMENT FOR {} FLOOR IS {}".format(floor,k[-1][-1]))