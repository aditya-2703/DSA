# Coin Change - Permutations - 2

# https://nados.io/question/coin-change-permutations-2
# 1. You are given a number n, representing the count of coins.
# 2. You are given n numbers, representing the denominations of n coins.
# 3. You are given a number "amt".
# 4. You are required to calculate and print the permutations of the n coins (same coin can be used again any number of times) using which the amount "amt" can be paid.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't force you but the intention is to teach a concept. Play in spirit of the question.

def get_solution(arr,target,ans):
    # if target goes in negative we don't want the tree  to explore further
    if target<0:
        return 
    # if target ==0 then we got our ans so print and return
    if target==0:
        print(f"{ans}.")
        return 

    # for all element make recursion call
    for ele in arr:
        # make a call
        get_solution(arr,target-ele,ans+f"{ele}-")
        
if __name__ == '__main__':
    arr = [2,3,5]
    target = 7
    get_solution(arr,target,"")