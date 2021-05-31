# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output: 0 0 1 2 2
# Explanation: 0s 1s and 2s are segregated 
# into ascending order.

# METHOD 1 -- TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
def Method_1(arr):
    n=len(arr)
    newlist=[0]*n
    count=[0]*3
    for i in range(n):
        count[arr[i]]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(n):
        arr[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
    print(arr)
    
  
# METHOD 2 -- TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_2(arr):
        # 0 -> i 0
        # i -> j 1 
        # j -> k 2
        #  i take care of 0
        #  j take care of 1
        #  k take care of 2
        
        # initially i,j=0
        # j -> increment if he got 1, k-> decrement if he got 2 , i-> increment if he got 0

        # if j == 0 we belong to 0 - i area so swap i , j then increment both
        # if j == 1 we belong to i - j area so we just increment j
        # if j == 2 we belong to j - k area so swap j , k then  decreament k
        
        # because we know the value of j so k gets 2 we know that 
        # but the value comes from k we don't know so we don't increment j
        i,j=0,0
        n=len(arr)
        k=n-1
        while j<=k:
                # if value is 0
                if arr[j]==0:
                        arr[i],arr[j]=arr[j],arr[i]
                        i+=1
                        j+=1

                # if value is 1
                elif arr[j]==1:
                        j+=1

                # if value is 2
                else:
                        arr[j],arr[k]=arr[k],arr[j]
                        k-=1
        print(arr)
if __name__ == '__main__':
    arr=[0 ,2 ,1 ,2 ,0]
    Method_1(arr)
    Method_2(arr)
    
