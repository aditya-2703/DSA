def binary_search(arr,l,r,element):
    mid=(l+r)//2
    if arr[mid]==element:
        return True
    elif arr[mid]<element:
        return binary_search(arr,mid+1,r,element)
    else:
        return binary_search(arr,l,mid,element)
    return False

if __name__ == '__main__':
    arr=[3,43,4,23,4,235,23,5,235,23,1,2,3]
    arr.sort()
    n=len(arr)
    if binary_search(arr,0,n,4):
        print("element found successfully")
    else:
        print("element not found")
    