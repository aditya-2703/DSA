# One Repeating And One Missing

# https://nados.io/question/one-repeating-and-one-missing?zen=true
# 1. You are given an array of length n containing numbers from 1 to n.
# 2. One number is present twice in array and one is missing.
# 3. You have to find these two numbers.
# Sample Input
# 7
# 1 
# 3 
# 4 
# 5 
# 1 
# 6 
# 2

# Sample Output
# Missing Number -> 7
# Repeating Number -> 1


def get_solution(n,arr):
    # here we do not have duplicate to cancel the unneccessory nums so make duplicates by adding aditional 1 to n number
    # so here if occurence is odd after adding 1-n it became even and cancel out 
    # if occurence is even and it became odd and do not cancel out
    mix = 0
    for i , j in zip(arr, range(1,len(arr)+1)):
        mix ^= i ^ j

    rightmost_set_bit = mix & -mix
    rm_on_bit = 0
    rm_off_bit = 0
    for i, j in zip(arr,range(1,len(arr)+1)):
        if i & rightmost_set_bit == 0:
            rm_off_bit ^= i
        if j & rightmost_set_bit == 0:
            rm_off_bit ^=j
        if i & rightmost_set_bit != 0:
            rm_on_bit ^= i
        if j & rightmost_set_bit != 0:
            rm_on_bit ^= j
    
    for i in arr:
        if i == rm_on_bit:
            print("repeating num ->" , i)
            print("missing num ->"  , rm_off_bit)
            break
        if i == rm_off_bit:
            print("repeating num ->" ,i)
            print("missing num ->",rm_on_bit)
            break
if __name__ == '__main__':
    n = 7
    nums = [1 ,3 ,4 ,5 ,1 ,6 ,2]
    get_solution(n,nums)