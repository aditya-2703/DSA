# Partition to K Equal Sum Subsets

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


def is_sum_equal(arr):
    curr_sum = sum(arr[0])
    for i in arr[1:]:
        if curr_sum!=sum(i):
            return False
    return True

def get_solution(i,filled_count,arr,k,ans):
    if i>=len(arr):
        if filled_count >= k:
            if is_sum_equal(ans):
                for i in ans:
                    print(i,end=" ")
        return 
    for j in range(len(ans)):
        if len(ans[j])>0:
            ans[j].append(arr[i])
            get_solution(i+1,filled_count,arr,k,ans)
            ans[j].remove(arr[i])
        else:
            ans[j].append(arr[i])
            get_solution(i+1,filled_count+1,arr,k,ans)
            ans[j].remove(arr[i])
            break

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    k = 3   
    get_solution(0,0,arr,k,[[]for i in range(k)])