# N Queen Problem using Branch And Bound

# The N queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.
# Backtracking Algorithm for N-Queen is already discussed here. In backtracking solution we backtrack when we hit a dead end. In Branch and Bound solution, after building a partial solution, we figure out that there is no point going any deeper as we are going to hit a dead end. 
# Sample Input
# 4

# Sample Output
# 0-1, 1-3, 2-0, 3-2, .
# 0-2, 1-0, 2-3, 3-1, .

def solver(row,n,col_arr,right_diag_arr,left_diag_arr,ans):
    # goal state
    if row==n:
        print(ans+" .")
        return 
    
    # for each col in this row
    for col in range(n):
        # check that all places are safe
        if col_arr[col] == False and left_diag_arr[row+col]==False and right_diag_arr[row-col+n-1]==False:
            # mark the danger positions 
            col_arr[col] = True
            left_diag_arr[row+col] = True
            right_diag_arr[row-col+n-1] = True
            # call for next row
            solver(row+1,n,col_arr,right_diag_arr,left_diag_arr,ans+f"{row}-{col}, ")
            # unmark the danger position for more exploration - backtrack
            col_arr[col] = False
            left_diag_arr[row+col] = False
            right_diag_arr[row-col+n-1] = False



if __name__ == '__main__':
    n = 8
    # column arr which blocks the danger cols
    col = [False]*n
    # right diagonal arr which blocks the danger right diagonal - row+col
    right_diag = [False]*(2*n-1)
    # left diagonal arr which blocks the danger left diagonal - row-col
    # but in case of row - col we get negative indexes which is not possible so add n-1 to it 
    # row - col + n -1
    left_diag = [False]*(2*n-1)
    solver(0,n,col,right_diag,left_diag,"")
    