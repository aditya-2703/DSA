# INPUT - [1,2,3,4,5,6] target_sum = 5
# OUTPUT - [1,4],[2,3],[5] 
# Explanation -  print the subarr whose sum is equal to target sum


def get_sequence(arr,target_sum,ans,result):
    if len(arr)==0:
        if ans==target_sum:
            print(result)
        return 
    first = arr[0]
    rest = arr[1:]
    get_sequence(rest,target_sum,ans+first,result+[first])
    get_sequence(rest,target_sum,ans,result)


if __name__ == '__main__':
    target_sum = 5
    arr= [i for i in range(1,6)]
    get_sequence(arr,target_sum,0,[])
    