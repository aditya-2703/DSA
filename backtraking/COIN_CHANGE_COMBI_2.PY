# Coin Change - Combinations - 2

# https://nados.io/question/coin-change-combinations-2
# 1. You are given a number n, representing the count of coins.
# 2. You are given n numbers, representing the denominations of n coins.
# 3. You are given a number "amt".
# 4. You are required to calculate and print the combinations of the n coins (same coin can be used 
#      again any number of times) using which the amount "amt" can be paid.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.


def get_solution_m1(i,arr,target,ans):
    if i>=len(arr):
        if target==0:
            print(f"{ans}.")
        return 
    if target<0:
        return 
    first = arr[i]
    get_solution_m1(i,arr,target-first,ans+f"{first}-")
    get_solution_m1(i+1,arr,target,ans)



if __name__ == '__main__':
    arr=[2,3,5,6,7]
    target = 12
    get_solution_m1(0,arr,target,"")
    