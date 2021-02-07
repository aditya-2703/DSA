# Input:
# N = 2
# arr[] = {1,0}
# Output: 0 1
# Explanation: 
# arr[arr[0]] = arr[1] = 0.
# arr[arr[1]] = arr[0] = 1.


# Input:
# N = 5
# arr[] = {4,0,2,1,3}
# Output: 3 4 2 0 1
# Explanation: 
# arr[arr[0]] = arr[4] = 3.
# arr[arr[1]] = arr[0] = 4.
# and so on.

def swap(a,b):
    a,b=b,a
def arrange(arr, n): 
    #Your code here
    d=dict()
    for i in range(n):
        d[arr[i]]=arr[arr[i]]
    for i in range(n):
        arr[i]=d[arr[i]]

if __name__ == '__main__':
    # arr=[1,0]
    arr=[4,0,2,1,3]
    n=len(arr)
    arrange(arr,n)
    print(arr)