def is_row(grid,row,val):
    for i in range(9):
        if grid[row][i]==val:
            return False
    return True
def is_col(grid,col,val):
    for j in range(9):
        if grid[j][col]==val:
            return False
    return True
def is_box(grid,row,col,val):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col]==val:
                return False
    return True
def num_not_repeated(grid,row,col,val):
    return is_row(grid,row,val) and is_col(grid,col,val) and is_box(grid,row-row%3,col-col%3,val)
def empty_space(grid,list_row_col):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                list_row_col[0]=i
                list_row_col[1]=j
                return True
    return False
def sudoko_solver(grid):
    list_row_col=[0,0]
    if not(empty_space(grid,list_row_col)):
        return True
    row=list_row_col[0]
    col=list_row_col[1]
    for curr_val in range(1,10):
        if num_not_repeated(grid,row,col,curr_val):
            grid[row][col]=curr_val
            if sudoko_solver(grid):
                return True
            grid[row][col]=0
    return False
if __name__ =='__main__':
    grid =[[3, 4, 0, 0, 1, 0, 0, 0, 2], 
        [7, 0, 9, 0, 0, 8, 0, 3, 0], 
        [0, 6, 8, 0, 0, 0, 7, 0, 0], 
        [4, 0, 0, 0, 0, 2, 0, 0, 5], 
        [0, 0, 0, 1, 9, 0, 0, 0, 0], 
        [5, 0, 2, 4, 0, 0, 0, 0, 1], 
        [0, 0, 0, 9, 8, 6, 0, 0, 0], 
        [9, 0, 4, 5, 0, 0, 0, 0, 8], 
        [0, 0, 0, 0, 4, 0, 0, 0, 0]] 
    if sudoko_solver(grid):
        for i in grid:
            print(i)
    else:
        print("NOT SOLUTOIN EXITS")
            