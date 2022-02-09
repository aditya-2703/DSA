# Tug of War

# https://www.geeksforgeeks.org/tug-of-war/
# Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the difference of the sum of two subsets is as minimum as possible. If n is even, then sizes of two subsets must be strictly n/2 and if n is odd, then size of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.
# For example, let given set be {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}, the size of set is 10. Output for this set should be {4, 100, 1, 23, 20} and {3, 5, -3, 89, 54}. Both output subsets are of size 5 and sum of elements in both subsets is same (148 and 148). 

min_gap = 9999
result = ""
def get_solution(arr,ans):
    global min_gap,result
    # base case when arr is empty
    if not arr:
        # when the both bucket is having gap of 0 or 1
        if abs(len(ans[0])-len(ans[1]))<2:
            # record min sum gap between two and save ans as string
            if min_gap>abs(sum(ans[0])-sum(ans[1])):
                if ans[0] and ans[1]:
                    min_gap = abs(sum(ans[0])-sum(ans[1]))
                    result = str(ans[0]) + " " + str(ans[1])
        return 

    # take first element   
    first = arr[0]
    # rest array 
    rest = arr[1:]

    # backtrack for including first element into 1st bucket
    ans[0].append(first)
    get_solution(rest,ans)
    ans[0].remove(first)

    # backtrack for including first element into 2nd bucket
    ans[1].append(first)
    get_solution(rest,ans)
    ans[1].remove(first)






if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    get_solution(arr,[[],[]])
    print(result)

    