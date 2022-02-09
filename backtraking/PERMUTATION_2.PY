# Permutations - 2

# 1. You are give a number of boxes (nboxes) and number of non-identical items (ritems).
# 2. You are required to place the items in those boxes and print all such configurations possible.

# Items are numbered from 1 to ritems.
# Note 1 -> Number of boxes is greater than number of items, hence some of the boxes may remain 
#                    empty.
# Note 2 -> Check out the question video and write the recursive code as it is intended without 
#                    changing signature. The judge can't force you but intends you to teach a concept.

# Sample Input

# 5
# 3

# Sample Output
# 12300
# 12030
# 12003
# 13200
# 13020
# 13002
# 10230
# 10203
# 10320
# 10302
# 10023
# 10032
# 21300
# 21030
# 21003
# 23100
# 23010
# 23001
# 20130
# 20103
# 20310
# 20301
# 20013
# 20031
# 31200
# 31020
# 31002
# 32100
# 32010
# 32001
# 30120
# 30102
# 30210
# 30201
# 30012
# 30021
# 01230
# 01203
# 01320
# 01302
# 01023
# 01032
# 02130
# 02103
# 02310
# 02301
# 02013
# 02031
# 03120
# 03102
# 03210
# 03201
# 03012
# 03021
# 00123
# 00132
# 00213
# 00231
# 00312
# 00321


def get_solution(i,n,k,arr):
    if i>=n:
        print(arr)
        return 
    
    for j in range(k):
        if arr[j]=="0":
            arr[j] = str(j+1)
            get_solution(i+1,n,k,arr)
            arr[j] = "0"
    get_solution(i+1,n,k,arr)
    


if __name__ == '__main__':
    n = 5
    k = 3
    get_solution(0,n,k,["0"]*n)
