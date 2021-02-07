def sort(list,n):
    for i in range(n):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j+1],list[j]=list[j],list[j+1]
    return list

if __name__ == '__main__':
    list = [23, 24, 324, 54, 5, 6, 54, 6, 5467, 47]
    print("BEFORE SORTING : : ",*list)
    n = len(list)
    x=sort(list,n)
    print("AFTER SORTING : :",*x)