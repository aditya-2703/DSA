# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.


# METHOD 1 : BRUTE FORCE
# TAKES O(N**2) TIME AND O(1) SPACE COMPLEXITY 
def Method_1(n,arr):
    max_len=0
    
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=arr[j]

            if curr_sum==0:
                max_len=max(max_len,j-i+1)
    return max_len

# METHOD 2: EFFICIENT APPROACH
# TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# here we just add elements in hashtable if it is not present previosly other wise will choose our max length 
# suppose arr=15 -2 2 -8 1 7 10 23
# keep sum    15                        hashmap{15:0}                           maxlen=0    15=not in hashmap  
#             15 13                     hashmap{15:0,13:1}                      maxlen=0    13=not in hashmap
#             15 13 15                  hashmap{15:0,13:1}                      maxlen=2    15=in hashmap       -->calculater len
#             15 13 15 7                hashmap{15:0,13:1,7:3}                  maxlen=2    7=not in hashmap
#             15 13 15 7 8              hashmap{15:0,13:1,7:3,8:4}              maxlen=2    8=not in hashmap
#             15 13 15 7 8 15           hashmap{15:0,13:1,7:3,8:4}              maxlen=5    15=in hashmap       -->calculater len
#             15 13 15 7 8 15 25        hashmap{15:0,13:1,7:3,8:4,25:6}         maxlen=5    25=not in hashmap
#             15 13 15 7 8 15 25 48     hashmap{15:0,13:1,7:3,8:4,25:6,48:7}    maxlen=5    48 not in hashmap
def Method_2(n,arr):
    hash_table=dict()
    max_len=0
    sum_s=0
    hash_table[0]=-1
    for i in range(n):
        sum_s+=arr[i]
        if sum_s in hash_table:
            max_len=max(max_len,i-hash_table[sum_s])
        else:
            hash_table[sum_s]=i
    print(max_len)
if __name__ == '__main__':
    arr=[15,-2,2,-8,1,7,10,23]
    Method_2(len(arr),arr)
    

