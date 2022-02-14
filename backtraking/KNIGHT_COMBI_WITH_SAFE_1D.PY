# Nknights Combinations - 2d As 1d - Knight Chooses

# https://nados.io/question/nknights-combinations-2d-as-1d-knight-chooses
# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the combinations in which n knights can be placed on the 
#      n * n chess-board. 
# 3. No knight shall be able to kill another.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.

def get_display(matrix):
    for i in matrix:
        print("\t".join(i))
    print()

# check is queen safe
def is_safe(matrix,row,col):
    if row-2>=0 and col-1>=0:
        upper_left_1 = matrix[row-2][col-1]
        if upper_left_1=="k":
            return False
    if row-2>=0 and col+1<len(matrix[0]):
        upper_right_1 = matrix[row-2][col+1]
        if upper_right_1=="k":
            return False

    if col-2>=0 and row-1>=0:
        upper_left_2 = matrix[row-1][col-2]
        if upper_left_2=="k":
            return False

    if col-2>=0 and row+1<len(matrix):
        upper_right_2 = matrix[row+1][col-2]
        if upper_right_2=="k":
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
            matrix[new_row][new_col] = "k"
            # call
            get_solution(row+1,i,box,matrix,q_count+1)
            # unmark
            matrix[new_row][new_col] = "-"

if __name__ == '__main__':
    box = 2
    get_solution(0,-1,box,[["-" for i in range(box)]for i in range(box)],0)
    
