# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Output: 15
# Explanation: For a given value 16, there
# are four values which are smaller than
# it. But 15 is the number which is smaller
# and closest to it with minimum difference
# of 1.

# METHOD 1 - 0(N*LOGN) TIME AND SPACE 0(1) COMPLEXITY
def Method_1(arr,x):
    arr.sort()
    i=len(arr)-1
    while i>-1:
        if arr[i]<x:
            return arr[i]
        i-=1
    return -1


if __name__ == '__main__':
    arr=[4 ,67, 13, 12 ,15]
    print(Method_1(arr,69))