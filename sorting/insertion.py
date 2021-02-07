
def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while j>=0 and list[j]>temp:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=temp
    return list

if __name__ == '__main__':
    lsit = [1, 4, 325, 346, 5, 6356, 54, 6743, 747, 6, 77, 65, 7, 56, 85, 8, 678, 76]
    print("list before sorted {}".format(lsit))
    print("list after sorting {}".format(insertion_sort(lsit)))
