def partition(arr,l,h):
    pviot=h
    i=l-1
    for j in range(l,h):
        if arr[j]<arr[pviot]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]# swap(arr[i],arr[j])
    arr[i+1],arr[h]=arr[h],arr[i+1]# swap(arr[i+1],arr[h])    
    return (i+1)
def quick_sort(arr,l,h):
    if l<h:
        p=partition(arr,l,h)
        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,h)

if __name__ == "__main__":
    arr=[1,2,23,4,5,342,5,24,5,43,5]
    quick_sort(arr,0,(len(arr)-1))
    for i in arr:
        print(i)