# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.

def subarr_given_sum(arr,givensum):
    i=j=0
    n=len(arr)
    newsum=givensum
    while i<n:
        if givensum!=0:
            givensum-=arr[i]
            i+=1
            
        if givensum<0:
            j+=1
            i=j
            givensum=newsum

        if givensum==0:
            return (j+1,i)
        


if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9,10]
    givensum=15
    print(subarr_given_sum(arr,givensum))
    