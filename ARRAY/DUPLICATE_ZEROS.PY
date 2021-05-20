# iven a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.
 
# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Here we don't solve this problem with only one pointer which point to zero and we shift array.
# so our approach is we use two operator one is i and other is j and here we go backwards  and each times when zero occures we activate j and shift all the values in right side by doing arr[j+1]=arr[j] and our condition is non of i and j hits length of array
 

def Method_1(arr):
    # first i go backwards then check whether there is 0 or not
    # if i is on the end of array and there is zero then so we have nothing because it goes out of bound. 
    # and after shift all element we have to set extra zero so for that we know i reach to that one position where  there is zero so as our problem we have to set i+1 zero 
    n=len(arr)
    for i in range(n-1,-1,-1):
        if (arr[i]==0 and i<n-1):
            for j in range(n-1,i,-1):
                if (j<n-1):
                    arr[j+1]=arr[j]
            arr[i+1]=0
    return arr


if __name__ == '__main__':
    arr=[1,0,2,3,0,4,5,0]
    print(Method_1(arr))
    