# Tiling Problem

# Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 
# Examples: 

# Input: n = 4
# Output: 5

# Explanation:
# For a 2 x 4 board, there are 5 ways
# All 4 vertical (1 way)
# All 4 horizontal (1 way)
# 2 vertical and 2 horizontal (3 ways)
# Input: n = 3
# Output: 3

# Explanation:
# We need 3 tiles to tile the board of size  2 x 3.
# We can tile the board using following ways
# Place all 3 tiles vertically.
# Place 1 tile vertically and remaining 2 tiles horizontally (2 ways)


# O(2^N) time complexity
total_recursion_moves = 0
def get_ways_rescursion(n):
    global total_recursion_moves 
    total_recursion_moves+=1
    if n<0:
        return 0
    if n==0:
        return 1
    tile_1 = get_ways_rescursion(n-1)
    tile_2 = get_ways_rescursion(n-2)
    return tile_1 + tile_2

# memorization
# O(2*N + 1) time and O(N) space complexity
total_dp_moves = 0
def get_ways_dp_memo(n,dp):
    global total_dp_moves
    total_dp_moves+=1
    if n<0:
        return 0
    if n==0:
        return 1
    if dp[n]!=0:
        return dp[n]
    tile_1 = get_ways_dp_memo(n-1,dp)
    tile_2 = get_ways_dp_memo(n-2,dp)
    value = tile_1+tile_2
    dp[n] = value
    return value

# tabulation
# O(N) time and O(N) space complexity
total_dp_moves_tab = 0
def get_ways_dp_tab(n,dp):
    global total_dp_moves_tab
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        total_dp_moves_tab+=1
        tile_1 = dp[i-1]
        tile_2 = dp[i-2]
        dp[i] = tile_1+tile_2
    return dp[-1]


# tabulation
# O(N) time and O(1) space complexity
def get_ways_dp_tab_op(n):
    one_tile = 1
    two_tile = 1
    for i in range(2,n+1):
        new_one_tile = two_tile
        new_two_tile = one_tile + two_tile
        one_tile = new_one_tile
        two_tile = new_two_tile

    return two_tile


if __name__ == '__main__':
    n=5
    ans_re = get_ways_rescursion(n)
    ans_me = get_ways_dp_memo(n,[0]*(n+1))
    ans_tab = get_ways_dp_tab(n,[0]*(n+1))
    ans_tab_op = get_ways_dp_tab_op(n)

    print(f"Ans is {ans_re} with moves {total_recursion_moves} in recursion")
    print(f"Ans is {ans_me} with moves {total_dp_moves} in dp memorization")
    print(f"Ans is {ans_tab} with moves {total_dp_moves_tab} in dp tabulation")
    print(f"Ans is {ans_tab_op} with moves {total_dp_moves_tab} in dp optimal tabulation")
