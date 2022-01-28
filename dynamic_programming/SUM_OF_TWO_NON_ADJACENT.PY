# Maximum sum such that no two elements are adjacent

# Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.

# Examples : 
# Input : arr[] = [5, 5, 10, 100, 10, 5]
# Output : 110

# Input : arr[] = [1, 2, 3]
# Output : 4

# Input : arr[] = [1, 20, 3]
# Output : 20





total_recursion_move = 0
def get_adjucent_sum_recursion(arr,curr_sum,is_include):
    global total_recursion_move
    total_recursion_move+=1
    if not arr:
        return curr_sum
    
    # curr max sum from calling function 
    max_sum = -99999999
    # if is_include flag is empty means call for both this is starting 
    if is_include == "":
        # call from taking first element
        take_zeroth = curr_sum+arr[0]
        if len(arr)>0:
            after_zero_rest = arr[1:]
            zero_th = get_adjucent_sum_recursion(after_zero_rest,take_zeroth,"yes")
            max_sum = max(zero_th,max_sum)
        # call from taking second element ingnoring first element
        if len(arr)>1:
            take_oneth = curr_sum+arr[1]
            after_one_rest = arr[2:]
            one_th = get_adjucent_sum_recursion(after_one_rest,take_oneth,"yes")
            max_sum = max(one_th,max_sum)
    # this flag suggest that previous element was taken so ignore this element
    if is_include == "yes":
        if len(arr)>0:
            one_th = get_adjucent_sum_recursion(arr[1:],curr_sum,"no")
            max_sum = max(one_th,max_sum)
    # this says that previous element was not taken so include this elements 
    else:
        take_zeroth = curr_sum+arr[0]
        if len(arr)>0:
            after_zero_rest = arr[1:]
            zero_th = get_adjucent_sum_recursion(after_zero_rest,take_zeroth,"yes")
            max_sum = max(zero_th,max_sum)
        if len(arr)>1:
            take_oneth = curr_sum+arr[1]
            after_one_rest = arr[2:]
            one_th = get_adjucent_sum_recursion(after_one_rest,take_oneth,"yes")
            max_sum = max(one_th,max_sum)
    # for each call update max sum variable 
    
    # return curr function max sum 
    return max_sum

total_dp_move = 0
def get_adjucent_sum_dp(arr,n):
    global total_dp_move
    # if we take first element then sum is 
    is_taken = arr[0]
    # if we ignore first element then sum is 
    is_not_taken = 0
    for i in range(1,n):
        total_dp_move+=1
        # now we do not take element so add curr element to this var
        new_is_taken = is_not_taken + arr[i]
        # now we take the element so ignore this element and save the max of prev two var
        new_is_not_taken = max(is_taken,is_not_taken)
        # update both var
        is_taken = new_is_taken
        is_not_taken = new_is_not_taken
    # return max out of two
    return max(is_taken,is_not_taken)

if __name__ == '__main__':
    arr = [5, 5, 10, 100, 10, 5]
    print(f"Ans is {get_adjucent_sum_recursion(arr,0,'')} with {total_recursion_move} moves in recursion ")
    print(f"Ans is {get_adjucent_sum_dp(arr,len(arr))} with {total_dp_move} moves in dp ")
    