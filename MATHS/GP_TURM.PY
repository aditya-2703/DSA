# Input:
# A = 2 
# B = 3
# N = 1
# Output: 2
# Explanation: The first term is already
# given in the input as 2

# TAKES 0(1) TIME AND SPACE COMPLEXITY
def get_gpturm(a,b,n):
    r=b/a
    if n==1:
        return a
    else:
        return a*(r**(n-1))

if __name__ == '__main__':
    print(get_gpturm(1,2,2))
    