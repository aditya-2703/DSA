list=[1,12,9,5,6,10,3]#1->0 12->1 9->2 5->3 6->4 10->5
n=len(list)-1
def heap(list,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and list[l]>list[largest]:
        largest=l
    if r < n and list[r] > list[largest]:
        largest = r
    if largest!=i:
        list[i],list[largest]=list[largest],list[i]
        heap(list,n,largest)

def create_heap(list,n):
    for i in range(n//2,-1,-1):
        heap(list,n,i)
    for i in range(n,0,-1):
        list[i],list[0]=list[0],list[i]
        heap(list,i,0)
    return list

x=create_heap(list,n)
print(x)