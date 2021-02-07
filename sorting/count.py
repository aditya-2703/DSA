def count(array,n,k):
    count=[]
    newarray=[0]*n
    for i in range(k+2):
        count.append(0)
    for i in array:
        count[i]+=1
    for i in range(k+1):
        count[i]+=count[i-1] 
    
    for i in array:
        newarray[count[i]-1]=i
        count[i]-=1
    return newarray

if __name__ == "__main__":
    arrray=[34,2,35,21,52,23,51,25,124,3,52,31]
    n=len(arrray)
    array=count(arrray,n,max(arrray))
    print(array)