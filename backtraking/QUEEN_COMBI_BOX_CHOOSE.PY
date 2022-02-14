# Queens Combinations - 2d As 2d - Box Chooses

# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the combinations in which n queens can be placed on the 
#      n * n chess-board. 

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.

# Sample Input
# 2

# Sample Output
# qq
# --

# q-
# q-

# q-
# -q

# -q
# q-

# -q
# -q

# --
# qq

def get_solution(row,col,box,q_count,ans):
    # extreme point
    if row==box:
        # when total queen is same as box 
        if q_count==box: 
            print(ans)
        return 
    new_row = 0
    new_col = 0
    include = ""
    not_include = ""
    # if col is at end increase row
    if col==box-1:
        new_row = row+1
        new_col = 0
        # include the queen with new line 
        include = ans + "q\n"
        # not include the queen with new line
        not_include = ans + "-\n"
    # if col is not at end so just increase col
    else:
        new_row  = row
        new_col = col + 1
        # inlude the queen
        include = ans + "q"
        # not include the queen
        not_include = ans + "-"
    # call for include
    get_solution(new_row,new_col,box,q_count+1,include)
    # call for not include
    get_solution(new_row,new_col,box,q_count,not_include)

if __name__ == '__main__':
    box = 2
    get_solution(0,0,box,0,"")
    