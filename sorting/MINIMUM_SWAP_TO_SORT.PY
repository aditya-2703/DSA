# Input: 
# N = 5
# arr = {1 5 4 3 2}
# Output: 2
# Explaination: swap 2 with 5 and 3 with 4.


def Method_1(arr,n):
    visited=[False]*n
    count=0
    for i in range(n):
        if visited[i]!=True:
            visited[i]=True

            if arr[i]==i+1:
                continue
            else:
                c=arr[i]-1

                while not visited[c]:
                    visited[c]=True
                    nn=arr[i]-1
                    c=nn
                    count+=1
    print(count)



if __name__ == '__main__':
    # arr=[1,4,3,2]
    arr=[4,2,5,1,3,7,6,8]
    # arr=[1,5,4,3,2]
    Method_1(arr,len(arr))
    