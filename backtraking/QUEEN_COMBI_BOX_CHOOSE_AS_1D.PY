# Queens Combinations - 2d As 1d - Queen Chooses

# https://nados.io/question/queens-combinations-2d-as-1d-queen-chooses?zen=true
# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the combinations in which n queens can be placed on the 
#      n * n chess-board. 

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.

def get_display(matrix):
    for i in matrix:
        print("\t".join(i))
    print()


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
        
        # mark 
        matrix[new_row][new_col] = "q"
        # call
        get_solution(row+1,i,box,matrix,q_count+1)
        # unmark
        matrix[new_row][new_col] = "-"

if __name__ == '__main__':
    box = int(input())
    get_solution(0,-1,box,[["-" for i in range(box)]for i in range(box)],0)
    