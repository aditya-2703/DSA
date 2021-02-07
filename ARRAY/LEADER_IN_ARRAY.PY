# # Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 
# N = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements 
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 


#METHOD 1 -- 0(N*N) TIME AND 0(D) SPACE COMPLEXITY WHERE D IS SIZE OF LEADER ARRAY
def method_1(arr):
    leader=[]
    # temp=arr[0]
    # for i in range(1,len(arr)):
    #     if arr[i]>temp:
    #         temp=arr[i]
        
    for i in range(0, len(arr)):  
        for j in range(i, len(arr)):  
            if arr[i]<arr[j]:  
                break
            if j == len(arr)-1: # If loop didn't break  
                leader.append(arr[i])
    return leader
    
# METHOD 2 -- O(N) TIME AND 0(D) SPCE COMPLEXITY WHERE D IS SIZE OF LAEDER ARRAY
def method_2(arr):
    leader=[]
    max_element=arr[len(arr)-1]
    leader.append(max_element)
    for i in range(len(arr)-2,-1,-1):
        if max_element<=arr[i]:
            max_element=arr[i]
            leader.append(max_element)
    leader.reverse()
    return leader
if __name__ == '__main__':
    l=method_1([16,11,4,3,5,2])
    k=method_2([16,11,4,3,5,2])
    for i in l:
        print(i,end = " ")


