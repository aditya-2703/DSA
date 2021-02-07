# # Input: nums = {2, 8, 5, 4}
# # Output: 1
# # Explaination: swap 8 with 4.

def minSwaps(arr):
    # here in this approach will first assign an array with its index 
    in_arr=[*enumerate(arr)]
    
    # the resion for building this is we can make sure the element is visited
    check={k:False for k in range(len(in_arr))}
    # now in in_arr the first is index number and second is the value 
    # now will sort the array by its value

    sorted_arr=sorted(in_arr,key = lambda x:x[1])
    # now we have our soted_arr in which array is sorted by it's value not index 

    counter=0
    # now will check that if the position of index is right ot not by iterate through it
    for i in range(len(in_arr)):
        if check[i] or sorted_arr[i][0]==i:
            continue
        cycle=0
        j=i
        while not check[j]:
            check[j]=True
            j=sorted_arr[j][0] 
            cycle+=1

            if cycle>0:
                counter+=(cycle-1)    
    return counter

if __name__ == '__main__':
    print(minSwaps([1 ,5 ,4 ,3 ,2]))
