# Fractional Knapsack Problem

# Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# In the 0-1 Knapsack problem, we are not allowed to break items. We either take the whole item or don’t take it. 

# Input: 
# Items as (value, weight) pairs 
# arr[] = [[60, 10], [100, 20], [120, 30]] 
# Knapsack Capacity, W = 50; 

# Output: 
# Maximum possible value = 240 
# by taking items of weight 10 and 20 kg and 2/3 fraction 
# of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240

class Item:
    def __init__(self,item_size,item_price):
        self.item_size= item_size
        self.item_price = item_price
        self.fraction = self.item_price/self.item_size

    def __lt__(self,other):
        return self.fraction < other.fraction

def get_max_profit(item_info,bag_size):
    arr = []
    for price, weight in item_info:
        obj = Item(weight,price)
        arr.append(obj)
    # sort by fractions
    arr.sort(reverse = True)
    ans = 0
    # iterate through arr
    for i in arr:
        # if item can go into bag then put it and add price
        if i.item_size<bag_size:
            ans+=i.item_price
            bag_size-=i.item_size
        # if whole item can't be fit in bag then add fraction of upcoming weight and add so in this case after adding the bagsize is empty
        else:
            ans+=bag_size*i.fraction
            break
    print(ans)
    



if __name__ == '__main__':
    arr = [[60, 10], [100, 20], [120, 30]] 
    bag_size = 50
    get_max_profit(arr,bag_size)