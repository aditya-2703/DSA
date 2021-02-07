def max_sum(matrix):
   rows = len(matrix)
   cols = len(matrix[0])
   maxsum=-1
   for i in  range(rows):
      for j in range(cols):
            if i>0:
               matrix[i][j]+=matrix[i-1][j]
            if j>0:
               matrix[i][j]+=matrix[i][j-1]
            if i>0 and j>0:
               matrix[i][j]-=matrix[i-1][j-1]    
   for row in range(rows):
      for col in range(cols):
         for r in range(row,rows):
            for c in range(col,cols):
               currentsum=matrix[r][c]
               if row>0:
                  currentsum-=matrix[row-1][c] 
               if col>0:
                  currentsum-=matrix[r][col-1] 
               if col and row > 0:
                  currentsum+=matrix[row-1][col-1]
               if maxsum<currentsum:
                  maxsum=currentsum   
                                  
   return maxsum
if __name__ == '__main__':
    matrix=[[6,-5,-7,4,-4],
            [-9,3,-6,5,2],
            [-10,4,7,-6,3],
            [-8,9,-3,3,-7]]
    print(max_sum(matrix))
    