def kadane(arr,start,finish,n):
    maxsum=-999999999
    localstart=0
    finish[0]=-1
    Sum=0
    for i in range(n):
        Sum+=arr[i]
        if Sum<0:
            Sum=0
            localstart=i+1
        elif Sum>maxsum:
            maxsum=Sum
            start[0]=localstart
            finish[0]=i
    if finish[0]!=-1:
        return maxsum

    maxsum=arr[0]
    start[0]=finish[0]=0

    for i in range(1,n):
        if maxsum<arr[i]:
            maxsum=arr[i]
            start[0]=finish[0]=i
    return maxsum


def findmaxsum(matrix):
    global ROW,COL 
    start=finish=[0]
    left,right,top,bottom=None,None,None,None
    maxsum=-99999999999
    temp=[None]*ROW
    for L in range(COL):
        temp=[0]*ROW
        for R in range(L,COL):
            for i in range(ROW):
                temp[i]+=matrix[i][R]
            SUM=kadane(temp,start,finish,ROW)
            if SUM>maxsum:
                maxsum=SUM
                left=L
                right=R
                top=start[0]
                bottom=finish[0]
    print(f"the sum is {maxsum}")
if __name__ == '__main__':
    ROW=4
    COL=5   
    matrix=[[6,-5,-7,4,-4],
            [-9,3,-6,5,2],
            [-10,4,7,-6,3],
            [-8,9,-3,3,-7]]
    findmaxsum(matrix)
    