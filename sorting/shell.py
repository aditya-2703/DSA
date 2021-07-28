def shellSort(array, n):
#     gap n-> n//2 -> n//4
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap //= 2


        

if __name__ == '__main__':
    data = [9, 8, 3, 7, 5, 6, 4, 1]
    size = len(data)
    shellSort(data, size)
    print('Sorted Array in Ascending Order:')
    print(data)


















