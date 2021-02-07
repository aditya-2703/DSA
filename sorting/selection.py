
def selection_sort(list,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if list[j]<list[min]:
                min=j

        if min!=i:
            list[i],list[min]=list[min],list[i]
    return list

if __name__ == '__main__':
    list = [ -34, -234, -324, 2,-423, -4, 23, -432]
    n = len(list)
    print("before sorting list {}".format(list))
    selection_sort(list,n)
    print("after sorting list {}".format(list))