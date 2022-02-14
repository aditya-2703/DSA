# Nqueens Permutations - 2d As 1d - Queen Chooses

# https://nados.io/question/nqueens-permutations-2d-as-1d-queen-chooses
# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the permutations in which n queens (distinct) can be 
#      placed on the n * n chess-board. 
# 3. No queen shall be able to kill another.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.
def get_display(matrix):
    for i in matrix:
        print("\t".join(i))
    print()

# check is queen safe
def is_safe(matrix,row,col):
    for i in range(len(matrix)):
        if matrix[row][i] != "-" or matrix[i][col]!="-":
            return False

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i+j == row+col or i-j == row-col:
                if matrix[i][j] != "-":
                    return False
    return True

# 1d to 2d : row = cell / size
#          : col = cell % size
# 2d to 1d : cell = row * size  + col
def get_solution(row,box,matrix,q_count):
    # base case when queen is  = boxlen
    # print ans
    if q_count == box:
        get_display(matrix)
        return 
    
    # loop as 1d 
    for i in range(box*box):
        # extract row and col from 1d
        new_row = i // box
        new_col = i % box
        if is_safe(matrix,new_row,new_col) and matrix[new_row][new_col]=="-":            
            # mark 
            matrix[new_row][new_col] = f"q{q_count+1}"
            # call
            get_solution(row+1,box,matrix,q_count+1)
            # unmark
            matrix[new_row][new_col] = "-"

if __name__ == '__main__':
    box = 4
    get_solution(0,box,[["-" for i in range(box)]for i in range(box)],0)
    