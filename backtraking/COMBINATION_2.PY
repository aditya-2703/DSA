# Combinations - 2

# https://nados.io/question/combinations-2?zen=true
# 1. You are give a number of boxes (nboxes) and number of identical items (ritems).
# 2. You are required to place the items in those boxes and print all such configurations possible.

# Items are identical and all of them are named 'i'
# Note 1 -> Number of boxes is greater than number of items, hence some of the boxes may remain 
#                    empty.
# Note 2 -> Check out the question video and write the recursive code as it is intended without 
#                    changing signature. The judge can't force you but intends you to teach a concept.
# Sample Input
# 5
# 3

# Sample Output
# iii--
# ii-i-
# ii--i
# i-ii-
# i-i-i
# i--ii
# -iii-
# -ii-i
# -i-ii
# --iii


def get_solution(index,n,k,visited,level):
    if index >= k:
        # if all item filled print ans
        for i in visited:
            if i==True:
                print("i",end="")
            else:
                print("-",end="")
        print()
        return 
    
    # for combination in each cell explore all values  \
    # but make sure 2 appear after 1 so that there is no chance of 21 so 12 ans 21 is not permute
    for j in range(level+1,n):
        if visited[j] == False:
            visited[j] = True
            get_solution(index+1,n,k,visited,j)
            visited[j] = False




if __name__ == '__main__':
    n = 5
    k = 3
    get_solution(0,n,k,[False]*n,-1)
    