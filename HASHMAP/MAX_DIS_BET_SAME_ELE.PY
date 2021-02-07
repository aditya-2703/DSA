# Input
# n= 6
# arr = {1, 1, 2, 2, 2, 1}

# Output
# 5

# Explanation
# arr[] = {1, 1, 2, 2, 2, 1}
# Max Distance: 5
# Distance for 1 is: 5-0 = 5
# Distance for 2 is : 4-2 = 2
# Max Distance 5


# METHOD 1 -- O(N) TIME AND O(N) SPACE COMPLEXITY
def Method_1(arr):
    dictionary=dict()
    for i in arr:
        dictionary[i]=[]
    for i in range(len(arr)):
        dictionary[arr[i]].append(i)
    mx=-1
    mn=999
    res=-1
    for i in dictionary:
        mx=max(dictionary[i])
        mn=min(dictionary[i])
        if res<(mx-mn):
            res=mx-mn
    return res
if __name__ == '__main__':
    print(Method_1([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]))
    