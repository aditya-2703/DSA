# Paint House - Many Colors

# 1. You are given a number n and a number k separated by a space, representing the number of houses and number of colors.
# 2. In the next n rows, you are given k space separated numbers representing the cost of painting nth house with one of the k colors.
# 3. You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.

# Constraints
# 1 <= n <= 1000
# 1 <= k <= 10
# 0 <= n1-0th, n1-1st, .. <= 1000

# Sample Input
# 4 3
# 1 5 7
# 5 8 4
# 3 2 9
# 1 2 4

# Sample Output
# 8

# with dp - O(N**3) time complexity
total_dp_moves = 0
def paint_with_dp_cube(colors,n):
    global total_dp_moves
    dp = [[0 for i in range(len(colors[0]))]for i in range(len(colors))]
    dp[0][0] = colors[0][0]
    dp[0][1] = colors[0][1]
    dp[0][2] = colors[0][2]
    for i in range(1,n):
        for j in range(len(colors[0])):
            min_value = 9999
            for k in range(len(colors[0])):
                total_dp_moves+=1
                if k!=j:
                    min_value = min(min_value,dp[i-1][k])
            dp[i][j] = min_value + colors[i][j]
            
    
    result = 999999
    for i in range(len(dp[0])):
        result = min(result,dp[-1][i])
    return result

# with dp - O(N**2) time complexity
total_dp_moves_s = 0
def paint_with_dp_square(colors,n):
    global total_dp_moves_s
    dp = [[0 for i in range(len(colors[0]))]for i in range(len(colors))]
    min_value = 99999
    second_min_value = 99999
    m = len(colors[0])
    for i in range(m):
        value = colors[0][i]
        dp[0][i] = value
        
        if value<=min_value:
            second_min_value = min_value
            min_value = value
        elif value<=second_min_value:
            second_min_value = value
    for i in range(1,n):
        new_min_value = 99999
        new_second_min_value = 99999
        for j in range(m):
            total_dp_moves_s+=1
            value = colors[i][j]
            if dp[i-1][j]==min_value:
                dp[i][j] = second_min_value + value
            else:
                dp[i][j] = min_value + value

            if dp[i][j]<=new_min_value:
                new_second_min_value = new_min_value
                new_min_value = dp[i][j]
            elif dp[i][j]<=new_second_min_value:
                new_second_min_value = dp[i][j]

        min_value = new_min_value
        second_min_value = new_second_min_value
    return min_value


if __name__ == '__main__':
    n = 4
    rgb = [[1, 5, 7],
        [5, 8, 4],
        [3, 2, 9],
        [1, 2, 4]]
    # n=3
    # rgb = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]

    print(f"Ans is {paint_with_dp_cube(rgb,n)} with moves {total_dp_moves} in dp")
    print(f"Ans is {paint_with_dp_square(rgb,n)} with moves {total_dp_moves_s} in dp")

    
    