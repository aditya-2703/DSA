# Input:
# 7
# 1 9 3 10 4 20 2
# Output:
# 4
# Explanation:
# Logest consecutive subsequence is 1, 2, 3, 4 of length 4.

# METHOD - 1 TAKES O(NLOGN) TIME AND O(Y) (where y is len of all sequesnces) SPACE COMPLEXITY
def Method_1(arr):
    arr.sort()
    count=1
    nlist=[]
    for i in range(1,len(arr)):
        if arr[i-1]+1==arr[i]:
            count+=1
        else:
            nlist.append(count)
            count=1
    return max(nlist)

# METHOD - 2 TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# here we find min element of sequence and then add 1 to it so if it in set we just add 1 and we continue 

def Method_2(arr):
    dictionary=set()
    for i in arr:
        dictionary.add(i)
    ans=0
    for i in range(len(arr)):
        if arr[i]-1 not in dictionary:
            j=arr[i]
            while j in dictionary:
                j+=1
            ans=max(ans,j-arr[i])
    return ans
if __name__ == '__main__':
    print(Method_2([36 ,41 ,56 ,35 ,44 ,33 ,34 ,92 ,43 ,32 ,42]))
    