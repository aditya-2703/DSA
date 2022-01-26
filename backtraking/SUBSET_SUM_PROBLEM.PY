# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

# Example: 

# Input: set[] = [3, 34, 4, 12, 5, 2], sum = 9
# Output: True  
# There is a subset (4, 5) with sum 9.

# Input: set[] = [3, 34, 4, 12, 5, 2], sum = 30
# Output: False
# There is no subset that add up to 30.


# set[]=[3, 4, 5, 2]
# sum=9
# (x, y)= 'x' is the left number of elements,
# 'y' is the required sum
  
#               (4, 9)
#              [True]
#            /        \  
#         (3, 6)       (3, 9)
               
#         /    \        /   \ 
#      (2, 2)  (2, 6)   (2, 5)  (2, 9)
#      [True]  
#      /   \ 
#   (1, -3) (1, 2)  
# [False]  [True] 
#          /    \
#        (0, 0)  (0, 2)
#        [True] [False]      



def get_all_subset_sum_pair(subset,target,pair,curr_sum):
    if not subset:
        if curr_sum==target:
            print(pair)
        return 
    take = subset[0]
    rest = subset[1:]
    get_all_subset_sum_pair(rest,target,pair+[take],curr_sum+take)
    get_all_subset_sum_pair(rest,target,pair,curr_sum)




if __name__ == '__main__':
    subset = [3, 34, 4, 12, 5, 2]
    target = 46
    get_all_subset_sum_pair(subset,target,[],0)
    