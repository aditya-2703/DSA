# Queens Permutations - 2d As 2d - Box Chooses

# https://nados.io/question/queens-permutations-2d-as-2d-box-chooses?zen=true
# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the permutations in which n queens can be placed on the 
#      n * n chess-board. 

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.


def get_solution(row,col,box,q_set,matrix,q_count):
    if row==box:
        if q_count==box:
            for i in matrix:
                print("\t".join(i))
            print()
        return 
    new_row = 0
    new_col = 0
    if col == box-1:
        new_row = row+1
        new_col = 0
    else:
        new_row = row
        new_col = col+1

    for q in range(box):
        if q+1 not in q_set:
            if matrix[row][col] == "-":
                q_set.add(q+1)
                matrix[row][col] = "q"+str(q+1)
                get_solution(new_row,new_col,box,q_set,matrix,q_count+1)
                matrix[row][col] = "-"
                q_set.remove(q+1)

    get_solution(new_row,new_col,box,q_set,matrix,q_count)




if __name__ == '__main__':
    box = 2
    get_solution(0,0,box,set(),[["-" for i in range(box)]for i in range(box)],0)
    



