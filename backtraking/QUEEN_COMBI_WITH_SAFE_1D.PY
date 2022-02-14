# Nqueens Combinations - 2d As 1d - Queen Chooses

# https://nados.io/question/nqueens-combinations-2d-as-1d-queen-chooses?zen=true
# Format
# Input
# A number n
# Output
# Check the sample output and question video
# Example
# Sample Input
# 4
# Sample Output
# -	q	-	-	
# -	-	-	q	
# q	-	-	-	
# -	-	q	-	

# -	-	q	-	
# q	-	-	-	
# -	-	-	q	
# -	q	-	-	


def get_display(matrix):
    for i in matrix:
        print("\t".join(i))
    print()

# check is queen safe
def is_safe(matrix,row,col):
    for i in range(len(matrix)):
        if matrix[row][i] == "q" or matrix[i][col]=="q":
            return False

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i+j == row+col or i-j == row-col:
                if matrix[i][j] == "q":
                    return False
    return True

# 1d to 2d : row = cell / size
#          : col = cell % size
# 2d to 1d : cell = row * size  + col
def get_solution(row,level,box,matrix,q_count):
    # base case when queen is  = boxlen
    # print ans
    if q_count == box:
        get_display(matrix)
        return 
    
    # loop as 1d 
    for i in range(level+1,box*box):
        # extract row and col from 1d
        new_row = i // box
        new_col = i % box
        if is_safe(matrix,new_row,new_col):

            # mark 
            matrix[new_row][new_col] = "q"
            # call
            get_solution(row+1,i,box,matrix,q_count+1)
            # unmark
            matrix[new_row][new_col] = "-"

if __name__ == '__main__':
    box = 4
    get_solution(0,-1,box,[["-" for i in range(box)]for i in range(box)],0)
    