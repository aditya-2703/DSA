# Input:
# n = 10
# arr[] = {1,1,2,2,3,3,4,5,6,7}
# Output: 4 5 6 7
# Explanation: 4, 5, 6 and 7 are the only 
# elements which is having only 1 
# frequency and hence, Non-repeating.

# METHOD 1 -- TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
def fun(arr):    
    table=dict()
    nl=[]
    for i in arr:
        table[i]=0
    for i in arr:
        table[i]+=1
    print(table)
    for i in arr:
        if table[i]==1:
            nl.append(i)
    print(nl)
fun([1,1,2,2,3,3,4,5,6,7])