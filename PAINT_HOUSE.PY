# Given an integer N and a 2D array cost[][3], where cost[i][0], cost[i][1], and cost[i][2] is the cost of painting ith house with colors red, blue, and green respectively, the task is to find the minimum cost to paint all the houses such that no two adjacent houses have the same color.

# Examples:
# Input: N = 3, cost[][3] = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
# Output: 10
# Explanation: 
# Paint house 0 as blue. Cost = 2. Paint house 1 as green. Cost = 5. Paint house 2 as blue. Cost = 3.
# Therefore, the total cost = 2 + 5 + 3 = 10.

# Input: N = 2, cost[][3] = [[1, 2, 3], [1, 4, 6]]
# Output: 3


# with recursion
min_cost = 999999
total_recursion_moves = 0
def paint_with_recursion(i,colors,n,total_cost,color,print_color,print_the_values):
    global min_cost,total_recursion_moves
    total_recursion_moves+=1
    if i==n:
        if print_the_values:
            print(f"colors {print_color} with cost {total_cost}")
        min_cost = min(min_cost,total_cost)
        return min_cost
    if i>n:
        return 0

    red_cost,green_cost,blue_cost = colors[i][0],colors[i][1],colors[i][2]
    

    total_sum = 100
    if color=="red":
        green_color_cost  =paint_with_recursion(i+1,colors,n,total_cost+green_cost,"green",print_color+ "-"+"g",print_the_values)
        blue_color_cost = paint_with_recursion(i+1,colors,n,total_cost+blue_cost,"blue",print_color+ "-"+"b",print_the_values)
        total_sum  = red_cost + min(blue_color_cost,green_color_cost)
    elif color == "green":
        red_color_cost = paint_with_recursion(i+1,colors,n,total_cost+red_cost,"red",print_color+"-"+"r",print_the_values)
        blue_color_cost = paint_with_recursion(i+1,colors,n,total_cost+blue_cost,"blue",print_color+ "-"+"b",print_the_values)
        total_sum = green_cost + min(red_color_cost,blue_color_cost)
    elif color == "blue":
        red_color_cost = paint_with_recursion(i+1,colors,n,total_cost+red_cost,"red",print_color+"-"+"r",print_the_values)
        green_color_cost  =paint_with_recursion(i+1,colors,n,total_cost+green_cost,"green",print_color+ "-"+"g",print_the_values)
        total_sum = blue_cost + min(red_color_cost,green_color_cost)
    else:
        red_color_cost = paint_with_recursion(i+1,colors,n,total_cost+red_cost,"red",print_color+"-"+"r",print_the_values)
        green_color_cost  =paint_with_recursion(i+1,colors,n,total_cost+green_cost,"green",print_color+ "-"+"g",print_the_values)
        blue_color_cost = paint_with_recursion(i+1,colors,n,total_cost+blue_cost,"blue",print_color+ "-"+"b",print_the_values)


    return total_sum


# with dp
total_dp_moves = 0
def paint_with_dp(colors,n):
    global total_dp_moves
    r = colors[0][0]
    g = colors[0][1]
    b = colors[0][2]
    for i in range(1,n):
        total_dp_moves+=1
        prev_r,prev_g,prev_b = r,g,b
        r = colors[i][0]+min(prev_b,prev_g)
        g = colors[i][1]+min(prev_r,prev_b)
        b = colors[i][2]+min(prev_r,prev_g)

    return min(r,b,g)

if __name__ == '__main__':
    n = 4
    rgb = [[1, 5, 7],
        [5, 8, 4],
        [3, 2, 9],
        [1, 2, 4]]
    # n=3
    # rgb = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    paint_with_recursion(0,rgb,n,0,"","",print_the_values = False)
    print(f"Ans is {min_cost} with moves {total_recursion_moves} in recursion")

    print(f"Ans is {paint_with_dp(rgb,n)} with moves {total_dp_moves} in dp")
    
    
    