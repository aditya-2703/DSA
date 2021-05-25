# Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

# Examples : 
# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater
# than the half of the size of the array size. 

# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is
# greater than the half of the size of the array size.

def count(arr,value):
    count_ele=0
    for i in arr:
        if i==value:
            count_ele+=1
    return count_ele
# METHOD 1 -- BRUTE FORCE O(N**2) TIME AND O(1) SPACE COMPLEXTIY
def Method_1(arr):
    result=-999
    for i in range(len(arr)):
        result=max(result,count(arr,arr[i]))
    print(result) 

# METHOD 2 -- WITH SORTING O(NLOGN) TIME AND O(1) SPACE COMPLEXITY
def Method_2(arr):
    arr.sort()
    result=-999
    count=1
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            count+=1
        else:
            result=max(result,count)
            count=1
    if count>result:
        result=count;
    print(result)

# METHOD 3 -- WITH HASHMAP O(N) TIME AND O(N) SPACE COMPLEXITY
def Method_3(arr):
    hashmap={}
    result=-9999
    for i in range(len(arr)):
        if arr[i] not in hashmap:
            hashmap[arr[i]]=1
        else:
            hashmap[arr[i]]+=1
    for i in hashmap:
        result=max(hashmap[i],result)
    print(result)

# METHOD 4 -- WITH MOORE'S VOTING ALGORITHM O(N) TIME AND O(N) SPACE COMPLEXITY
# explanation -
# the problem is majority element should be greater than n/2 this means the count of majority element is alwaays greater then all of other different elements  example ..
# array = [1,1,2,1,1,3,4]  n=7 n/2=3 majority element is 1 so [2 3 4] this three other element is less than 1 so the idea is
# we always get majority element count than  any other element 

# first step - if we got same elements we increament count else we decrement it and as per rule which i  describe above we also get 1 extra element in array at last so we get our answer at last 

# 1 [1,1,2,1,1,3,4] count=1                 1->1
# 1 1 [1,1,2,1,1,3,4] count=2               1->2
# 1 1 2 [1,1,2,1,1,3,4] count=1-1           1->1
# 1 1 2 1 [1,1,2,1,1,3,4] count = 1+1       1->2
# 1 1 2 1 1 [1,1,2,1,1,3,4] count= 2+1      1->3
# 1 1 2 1 1 3 [1,1,2,1,1,3,4] count=3-1     1->2 
# 1 1 2 1 1 3 4 [1,1,2,1,1,3,4] count=2-1   1->1

# we switch element when count goes to 0 

def Method_4(arr):
    index_record=0
    count=1
    for i in range(len(arr)):
        if arr[i]==arr[index_record]:
            count+=1
        else:
            count-=1
        # here element goes to 0 so the other element is like greater than curr so it became zero we record that index then update count
        if count==0:
            index_record=i
            count=1
    our_element=arr[index_record]
    count=0
    for i in arr:
        if i==our_element:
            count+=1
    if count>len(arr)//2:
        print(count)
    else:
        return -1
if __name__ == "__main__":
    arr=[1,1,2,3,1]
    Method_1(arr)
    Method_2(arr)   
    Method_3(arr)
    Method_4(arr)
