# https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
# input n=5 k=3
# output 
# for explanation please check link given above

def Method_1(n, k):
    if n==1:
        return 0
    return (Method_1(n-1,k)+k)%n
    

if __name__ == '__main__':
    n=5
    k=3
    print(Method_1(n,k))
    