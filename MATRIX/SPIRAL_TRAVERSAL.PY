# Input:
# R = 4, C = 4
# matrix[][] = {{1, 2, 3, 4},
#            {5, 6, 7, 8},
#            {9, 10, 11, 12},
#            {13, 14, 15,16}}
# Output: 
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
# EXPLANATION:
#   1-> 2-> 3-> 4         
#               | 
# 5->6->7      8
# |      |     |     
# 9 10<-11     12
# |            | 
# 13<-14<-15<-16

# METHOD 1 -- TAKES O(N*M) TIME AND O(N*M) SPACE COMPLEXITY
def Method_1(matrix,r,c):
    arr=[0]*(r*c)
    top=left=0
    down=r
    right=c
    direction=0
    for_arr=0

    while top<down and left<right:

        # first row
        if direction==0:
            for i in range(left,right):
                arr[for_arr]=matrix[top][i]
                for_arr+=1
            top+=1

        elif direction==1:
            for i in range(top,down):
                arr[for_arr]=matrix[i][right-1]
                for_arr+=1
            right-=1
        
        elif direction==2:
            for i in reversed(range(left,right)):
                arr[for_arr]=matrix[down-1][i]
                for_arr+=1
            down-=1
        
        elif direction==3:
            for i in reversed(range(top,down)):
                arr[for_arr]=matrix[i][left]
                for_arr+=1
            left+=1
        
        direction=(direction+1)%max(r,c)        
    
    return arr
if __name__ == '__main__':
    matrix=[[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15,16]]
    print(Method_1(matrix,len(matrix),len(matrix[0])))
    