# The Knapsack problem
# I found the Knapsack problem tricky and interesting at the same time. I am sure if you are visiting this page, you already know the problem statement but just for the sake of completion :
# Problem:
# Given a Knapsack of a maximum capacity of W and N items each with its own value and weight, throw in items inside the Knapsack such that the final contents has the maximum value. Yikes !!
# input
# Knapsack Max weight       :       W = 8 (units)
# Total items              :       N = 4
# Values of items          :       v[] = {10, 40, 50, 70}
# Weight of items          :       w[] = {1, 3, 4, 5}
# output :110

money = [10, 40, 50, 70]
kgs = [1, 3, 4, 5]
bag_size = 8
total_item = len(money)


# with recursion
recursion_moves = 0
max_money = 0
def knapsack_recursion(money,kgs,bag_size,total_money):
    global max_money,recursion_moves
    recursion_moves+=1
    if bag_size<0:
        return 0
    if bag_size==0:
        max_money = max(max_money,total_money)
        return total_money

    for i in range(len(kgs)):
        knapsack_recursion(money,kgs,bag_size-kgs[i],total_money+money[i])

knapsack_recursion(money,kgs,bag_size,0)
print(f"Ans is {max_money} with total moves {recursion_moves} with recursion")

# with dp
dp_moves = 0
def knapsack_dp(money,kgs,bag_size):
    global dp_moves
    dp =[0 for i in range(bag_size+1)]
    for cell in range(len(dp)):
        curr_max = -99999
        for each_weight in range(len(kgs)):
            dp_moves+=1
            if kgs[each_weight]<=cell:
                prev_amount_cell = cell - kgs[each_weight]
                if prev_amount_cell>=0:
                    curr_max = max(money[each_weight]+dp[prev_amount_cell],curr_max)
        if curr_max!=-99999:
            dp[cell] = curr_max
    return dp[-1]

max_money = knapsack_dp(money,kgs,bag_size)
print(f"Ans is {max_money} with total moves {dp_moves} with dp")

