# The Knapsack problem
# I found the Knapsack problem tricky and interesting at the same time. I am sure if you are visiting this page, you already know the problem statement but just for the sake of completion :
# Problem:
# Given a Knapsack of a maximum capacity of W and N items each with its own value and weight, throw in items inside the Knapsack such that the final contents has the maximum value. Yikes !!
# input
# Knapsack Max weight       :       W = 10 (units)
# Total items              :       N = 4
# Values of items          :       v[] = {10, 40, 30, 50}
# Weight of items          :       w[] = {5, 4, 6, 3}
# output :90

money = [10,40,30,50]
kgs = [5,4,6,3]
bag_size = 10
total_item = len(money)

money = [15,15,10,45,30]
kgs =[2,5,1,3,4]
bag_size = 7
total_item = len(money)

# with recursion
recursion_moves = 0
def knapsack_recursion(money,kgs,bag_size,total_item):
    global recursion_moves
    recursion_moves+=1
    if total_item<=0 or bag_size<=0:
        return 0
    if kgs[total_item-1]>bag_size:
        return knapsack_recursion(money,kgs,bag_size,total_item-1)
    item_taken = knapsack_recursion(money,kgs,bag_size-kgs[total_item],total_item-1)
    item_not_taken  = knapsack_recursion(money,kgs,bag_size,total_item-1)
    return max(money[total_item]+item_taken,item_not_taken)

max_money = knapsack_recursion(money,kgs,bag_size,total_item-1)
print(f"Ans is {max_money} with total moves {recursion_moves} with recursion")

# with dp
dp_moves = 0
def knapsack_dp(money,kgs,bag_size,total_item):
    global dp_moves
    dp =[[0 for i in range(bag_size+1)]for i in range(total_item)]
    for item in range(total_item):
        for curr_bag_size in range(bag_size+1):
            dp_moves+=1
            if item!=0 or curr_bag_size!=0:
                dp[item][curr_bag_size] =0
            if kgs[item]>curr_bag_size:
                dp[item][curr_bag_size] = dp[item-1][curr_bag_size]
            else:
                is_taken = money[item]+dp[item-1][curr_bag_size-kgs[item]]
                is_not_taken = dp[item-1][curr_bag_size] 
                dp[item][curr_bag_size] = max(is_taken,is_not_taken)
    return dp[-1][-1]
max_money = knapsack_dp(money,kgs,bag_size,total_item)
print(f"Ans is {max_money} with total moves {dp_moves} with dp")

