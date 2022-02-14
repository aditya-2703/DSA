# Queens Combinations - 2d As 2d - Queen Chooses

# https://nados.io/question/queens-combinations-2d-as-2d-queen-chooses?zen=true
# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the combinations in which n queens can be placed on the 
#      n * n chess-board. 

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.


def get_display(matrix):
    for i in matrix:
        print("\t".join(i))
    print()
def get_solution(row,col,box,matrix,q_count):
    if q_count == box:
        get_display(matrix)
        return 
    
    for c in range(col+1,box):
        if matrix[row][c] == "-":
            matrix[row][c] = "q"
            get_solution(row,c,box,matrix,q_count+1)
            matrix[row][c] = "-"
    for r in range(row+1,box):
        for c in range(box):
            if matrix[r][c] == "-":
                matrix[r][c] = "q"
                get_solution(r,c,box,matrix,q_count+1)
                matrix[r][c] = "-"


if __name__ == '__main__':
    box = 2
    matrix = [["-" for i in range(box)]for i in range(box)]
    get_solution(0,-1,box,matrix,0)
    