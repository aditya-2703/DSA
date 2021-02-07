# input  ----- [1,2,3,4,5,6,7,8,9]
#             n=2
# output ----- [3,4,5,6,7,8,9,1,2]
rr=[1,2,3,4,5,6,7,8,9]
n=2


# METHOD 1 -- 0(m+n) 
def method_1(rr):
    temp=[0]*n
    for i in range(n):#0(n)  where n is no of shift
        temp[i]=rr[i]
    for i in range(len(rr)-n):#0(m-n) where m is len array  
        rr[i]=rr[i+n]
    print(temp)
    print(rr)
    for i in range(1,n+1):#0(n) 
        rr[len(rr)-i]=temp[n-i]
    print(rr)

# METHOD 2 -- 0(m*n)
def rotate_fun(rr):#0(m) m is length of array
    temp=rr[0]
    for i in range(len(rr)-1):
        rr[i]=rr[i+1]
    rr[-1]=temp
def method_2(rr):#0(n) n is number of shift
    for i in range(n):
        rotate_fun(rr)
    print(rr)

# METHOD 3 -- time - 0(m+n)
# step 1:reveres till n
# step 2:reverse from n
# step 3:reverse whole arr
def reverse(arr):
    for i in range(len(arr)):
        if i<len(arr)-i:
            arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
def method_3(rr):
    arr1=rr[:n]
    arr2=rr[n:]
    reverse(arr1)#  -- 0(n)
    reverse(arr2)#  -- 0(m-n)
    mix=arr1+arr2
    reverse(mix)#   -- 0(m)
    rr[:n]=mix[:n]
    rr[n:]=mix[n:]


