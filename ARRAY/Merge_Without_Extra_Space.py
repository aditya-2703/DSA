# Input: 
# N = 4, arr1[] = [1 3 5 7] 
# M = 5, arr2[] = [0 2 6 8 9]
# Output: 
# arr1[] = [0 1 2 3]
# arr2[] = [5 6 7 8 9]
# Explanation: After merging the two 
# non-decreasing arrays, we get, 
# 0 1 2 3 5 6 7 8 9.

# 0(m*n)
# 0(m+nlog(m+n))
def Method_1(arr1,arr2,n,m):
    pass




if __name__ == '__main__':
    arr1=[]
    arr2=[]
    n=len(arr1)
    m=len(arr2)
    Method_1(arr1,arr2,n,m)
    print(arr1+arr2)