# Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must visit each square exactly once. Print the order of each cell in which they are visited.

# Example:

# Input : 
# N = 8
# Output:
# 0  59  38  33  30  17   8  63
# 37  34  31  60   9  62  29  16
# 58   1  36  39  32  27  18   7
# 35  48  41  26  61  10  15  28
# 42  57   2  49  40  23   6  19
# 47  50  45  54  25  20  11  14
# 56  43  52   3  22  13  24   5
# 51  46  55  44  53   4  21  12

def get_all_paths(mat,i,j,move):
    # edge case
    if i<0 or j<0 or i>=len(mat) or j>=len(mat[0]) or mat[i][j]!=0:
        return 
    # goal case
    if move == len(mat)*len(mat):
        # print matrix
        for i in mat:
            print(i)
        print()

        return 

    # mark
    mat[i][j] = move

    get_all_paths(mat,i-2,j+1,move+1)
    get_all_paths(mat,i-1,j+2,move+1)
    get_all_paths(mat,i+1,j+2,move+1)
    get_all_paths(mat,i+2,j+1,move+1)

    get_all_paths(mat,i+2,j-1,move+1)
    get_all_paths(mat,i+1,j-2,move+1)
    get_all_paths(mat,i-1,j-2,move+1)
    get_all_paths(mat,i-2,j-1,move+1)

    # unmark
    mat[i][j] = 0

if __name__ == '__main__':
    N = 5
    mat = [[0 for i in range(N)]for i in range(N)]
    src_row = 0
    src_col = 0
    move = 1
    get_all_paths(mat,src_row,src_col,move)