#locho.
def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while j>=0 and list[j]>temp:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=temp

def shell_sort(array,n):
    gap=n//2
    for i in range(gap,1,-1):
        for j in range(n//2,):
            for i in range(j-gap,0,-1):
                if array[i+gap]>array[i]:
                    break
                else:
                    array[i+gap],array[i]=array[i],array[i+gap]
                i=i-gap
            j+=1
        gap//=2
        if gap==1:
            insertion_sort(array)


if __name__ == '__main__':
    array=[123,124,32,4,32,524,5,345,435,5]
    print('ARRAY BEFORE SORTING : ',array)
    shell_sort(array,len(array)-1)
    print('ARRAY AFTER SORTING : ', array)




















