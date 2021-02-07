def counting(array,exp):
    n=len(array)
    output=[0]*n
    count=[0]*10

    for i in array:
        index=i/exp
        count[int((index)%10)]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=array[i]/exp
        output[count[int((index)%10)]-1]=array[i]
        count[int((index)%10)]-=1
        i-=1
    for i in range(0,n):
        array[i]=output[i]        

def radix(array):
    max1=max(array)
    exp=1
    while max1//exp > 0:
        counting(array,exp)
        exp*=10    

if __name__ == "__main__":
    array=[6,5,4,35,445,45,4,54]
    radix(array)
    for i in array:
        print(i)