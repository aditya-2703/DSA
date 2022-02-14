# Coin Change - Combinations - 1

# https://nados.io/question/coin-change-combinations-1
# 1. You are given a number n, representing the count of coins.
# 2. You are given n numbers, representing the denominations of n coins.
# 3. You are given a number "amt".
# 4. You are required to calculate and print the combinations of the n coins (non-duplicate) using 
#      which the amount "amt" can be paid.

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.


def get_solution(i,arr,target,curr_sum,ans):
    if i>=len(arr):
        if curr_sum == target:
            print(ans,end=".")
            print()
        return 
    
    first = arr[i]
    get_solution(i+1,arr,target,curr_sum+first,ans+f"{first}-")
    get_solution(i+1,arr,target,curr_sum,ans)

if __name__ == '__main__':
    arr = [2,3,5,6,7]
    target =12
    get_solution(0,arr,target,0,"")