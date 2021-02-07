# Input:
# I = -32
# Output: 32
# Explanation: 
# The absolute value of -32 is 32.

# IT TAKES 0(1) TIME AND SPACE COMPLEXITY
def absolute_maker(val):
    if val > 0:
        return val
    else:
        return -(val)

if __name__ == '__main__':
    print(absolute_maker(32))
    