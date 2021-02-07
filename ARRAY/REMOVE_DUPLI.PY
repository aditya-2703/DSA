# REMOVE DUPLICATE ELEEMENT IN SORTED ARRAY
# sorted -- time  - 0(n)        space - 0(n)
def method_1(arr):
    newlist=[]
    for i in range(len(arr)):
        if arr[i-1]!=arr[i]:
            newlist.append(arr[i])
    return newlist


# sorted -- time  - 0(n)        space - 0(1)
def method_2(arr):
    j=0
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j]=arr[n-1]
    j+=1
    return j

if __name__ == '__main__':
    arr=[1,2,3,3,4,4,4,4,5]
    print(arr)
    print(method_1(arr))
    n=method_2(arr)
    for i in range(n):
        print(arr[i],end="")
    