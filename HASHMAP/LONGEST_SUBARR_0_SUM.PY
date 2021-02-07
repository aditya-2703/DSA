# # Input:
# # N = 8
# # A[] = {15,-2,2,-8,1,7,10,23}
# # Output: 5
# # Explanation: The largest subarray with
# # sum 0 will be -2 2 -8 1 7.
from icecream import *
# def Method_1(arr):#locha
#     arr.sort()
#     count=1
#     sum=0
#     current=0
#     if arr[0]>0:
#         return False
#     else:
#         for i in arr:
#             current=i
#             if sum>0:
#                 break
#             else:
#                 sum+=current
#                 count+=1
#     print(sum)            
#     print(count)
# if __name__ == '__main__':
#     Method_1([15,-2,2,-8,1,7,10,23])
    
def fun(n,arr,i):
    if n==i:
        ic(arr)
        return
    arr[i]=0
    fun(n,arr,i+1)
    arr[i]=1
    fun(n,arr,i+1)

fun(3,[0,0,0],0)