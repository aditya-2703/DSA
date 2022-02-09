# Permutation - 1

# 1. You are give a number of boxes (nboxes) and number of non-identical items (ritems).
# 2. You are required to place the items in those boxes and print all such configurations possible.

# Items are numbered from 1 to ritems.
# Note 1 -> Number of boxes is greater than number of items, hence some of the boxes may remain empty.
# Note 2 -> Check out the question video and write the recursive code as it is intended without changing signature. The judge can't 
#                    force you but intends you to teach a concept.


# Sample Input
# 5
# 3

# Sample Output
# 12300
# 12030
# 12003
# 13200
# 10230
# 10203
# 13020
# 10320
# 10023
# 13002
# 10302
# 10032
# 21300
# 21030
# 21003
# 31200
# 01230
# 01203
# 31020
# 01320
# 01023
# 31002
# 01302
# 01032
# 23100
# 20130
# 20103
# 32100
# 02130
# 02103
# 30120
# 03120
# 00123
# 30102
# 03102
# 00132
# 23010
# 20310
# 20013
# 32010
# 02310
# 02013
# 30210
# 03210
# 00213
# 30012
# 03012
# 00312
# 23001
# 20301
# 20031
# 32001
# 02301
# 02031
# 30201
# 03201
# 00231
# 30021
# 03021
# 00321

def get_solution(i,buckets,ele,ans):
    # base case 
    if i>=ele+1:
        # print method in string
        print("".join(ans))
        return 
    # for all the places 
    for ind in range(len(ans)):
        # if place not container any digit
        if ans[ind] == "0" and i not in ans:
            # mark or add
            ans[ind] = str(i)
            # call
            get_solution(i+1,buckets,ele,ans)
            # unmark or remove 
            ans[ind] = "0"

if __name__ == '__main__':
    buckets  = 5
    ele = 3
    get_solution(1,buckets,ele,["0"]*buckets)

