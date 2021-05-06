# Input:
# N = 5
# A[] = {5,5,4,6,4}
# Output: 4 4 5 5 6
# Explanation: The highest frequency here is
# 2. Both 5 and 4 have that frequency. Now
# since the frequencies are same then 
# smallerelement comes first. So 4 4 comes 
# firstthen comes 5 5. Finally comes 6.
# The output is 4 4 5 5 6.

def get_max(dictionary):
    max_value=-999
    max_count=-9999
    for i in dictionary:
        if dictionary[i]>max_count:
            max_value=i
            max_count=dictionary[i]
    return max_value,max_count
def calculate_freq(arr,value):
        count=0
        for i in arr:
            if i==value:
                count+=1
        return count
def Method_1(arr,n):
    arr.sort()
    dictionary=dict()
    for i in range(len(arr)):
        dictionary[arr[i]]=calculate_freq(arr,arr[i])
    print(dictionary)
    count=0
    i=0
    while i<len(arr):
        value,count=get_max(dictionary)
        while count!=0:
            arr[i]=value
            count-=1
            i+=1
        if count==0:
            del dictionary[value]
    print(arr)
    

    

if __name__ == '__main__':
    arr=[8, 9, 1, 2 ,3 ,1]
    Method_1(arr,len(arr))