# Combinations - 1

# 1. You are give a number of boxes (nboxes) and number of identical items (ritems).
# 2. You are required to place the items in those boxes and print all such configurations possible.

# Items are identical and all of them are named 'i'.
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



def is_k_ele(arr,k):
    count = 0
    for i in arr:
        if i=="i":
            count+=1
    return count==k

def get_solution(i,n,k,arr):
    if i>=n:
        if is_k_ele(arr,k):
            print("".join(arr))
        return 

    if arr[i]=="-":
        arr[i] = "i"
        get_solution(i+1,n,k,arr)
        arr[i] = "-"

    get_solution(i+1,n,k,arr)




if __name__ == '__main__':
    n = 5
    k = 3
    get_solution(0,n,k,["-"]*n)
    