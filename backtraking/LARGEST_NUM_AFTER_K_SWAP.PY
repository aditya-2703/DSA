# Find Maximum number possible by doing at-most K swaps

# https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/
# Given a positive integer, find the maximum integer possible by doing at-most K swap operations on its digits.
# Examples: 

# Input: M = 254, K = 1
# Output: 524
# Swap 5 with 2 so number becomes 524

# Input: M = 254, K = 2
# Output: 542
# Swap 5 with 2 so number becomes 524
# Swap 4 with 2 so number becomes 542

# Input: M = 68543, K = 1 
# Output: 86543
# Swap 8 with 6 so number becomes 86543

# swap of number in place i,j
def swap(number,i,j):
    ans = ""
    for k in range(len(number)):
        if k==i:
            ans+=number[j]
        elif k==j:
            ans+=number[i]
        else:
            ans+=number[k]
    return ans

result = 0
def get_solution(number,k):
    global result
    # capture the greatest number
    result=max(result,int(number))
    # when at most k swaps done return 
    if k==0:
        return 
    
    # i : 0->n-1
    for i in range(len(number)-1):
        # k : i->n
        for j in range(i+1,len(number)):
            # find the i,j number to swap 
            if int(number[i])<int(number[j]):
                # swap
                number = swap(number,i,j)
                # call
                get_solution(number,k-1)





if __name__ == '__main__':
    number = "7259943"
    k = 3
    get_solution(number,k)
    print(result)
    