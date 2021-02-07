# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output: 0 0 1 2 2
# Explanation: 0s 1s and 2s are segregated 
# into ascending order.

def Method_1(arr):
    n=len(arr)
    newlist=[0]*n
    count=[0]*3
    for i in range(n):
        count[arr[i]]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(n):
        arr[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
    print(arr)
if __name__ == '__main__':
    arr=[0 ,2 ,1 ,2 ,0]
    Method_1(arr)
    