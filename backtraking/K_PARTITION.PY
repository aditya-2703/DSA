# K-partitions

# 1. You are given two integers n and k, where n represents number of elements and k represents 
#      number of subsets.
# 2. You have to partition n elements in k subsets and print all such configurations.

# Note -> Check out the question video and write the recursive code as it is intended without changing signature. The judge can't force you but intends you to teach a concept.

# Sample Input

# 3
# 2

# Sample Output
# 1. [1, 2] [3] 
# 2. [1, 3] [2] 
# 3. [1] [2, 3] 





counter = 0
def get_solution(i,n,k,ans,filled_cell_count):
    global counter
    if i>=n+1:
        if filled_cell_count == k:
            counter+=1
            print(f"{counter}. ",end="")
            for li in ans:
                print("[",end="")
                for ele in li[:-1]:
                    print(ele,end="")
                    print(", ",end="")
                print(li[-1],end="")
                print("] ",end="")
            print()
        return

    for ind in range(len(ans)):
        if len(ans[ind])>0:
            ans[ind].append(i)
            get_solution(i+1,n,k,ans,filled_cell_count)
            ans[ind].remove(i)
        else:
            ans[ind].append(i)
            get_solution(i+1,n,k,ans,filled_cell_count+1)
            ans[ind].remove(i)
            break
if __name__ == '__main__':
    n = 3
    k = 2
    ans = []
    get_solution(1,n,k,[[]for i in range(k)],0)