# Input:
# N = 6, X = 16
# A[] = {1,4,45,6,10,8}
# Output: Yes
# Explanation: 10 and 6 are numbers
# making a pair whose sum is equal to 16.

# METHOD 1 -- O(N) TIME AND O(N) SPACE COMPLEXITY
def Method_1(arr,x):
    nlist=set()
    total=x
    for i in arr:
        if i not in nlist:
            nlist.add(total-i)
        elif i in nlist:
            return True
    return False

if __name__ == '__main__':
    print(Method_1([1,45,6,10,8],18))
    