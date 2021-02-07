# 10==>4==5==3==2==>18
        
# 12==>2==10==1==4==>7

# CALCULATE MIN PATH 
# METHOD 1 -- TAKES O(N) TIME AND O(N*M) SPACE COMPLEXITY (n is len of a and m is len of b)
def Method_1(a,b,start,end):
    value=len(a[0])
    for_a=[0]*value
    for_b=[0]*value
    for_a[0]=start[0]+a[0][0]
    for_b[0]=start[1]+a[1][0]
    for i in range(1,value):
        for_a[i]=min(for_a[i-1]+a[0][i],for_b[i-1]+b[1][i]+a[0][i])
        for_b[i]=min(for_b[i-1]+a[1][i],for_a[i-1]+b[0][i]+a[1][i])
    print(for_a)
    print(for_b)
    ans=min(for_a[value-1]+end[0],for_b[value-1]+end[1])
    print(ans)


# METHOD 2 -- TKES O(N) TIME AND 0(1) SPACE COMPLEXITY
def Method_2(a,value,start,end):
    n=len(a[0])
    first=start[0]+a[0][0]
    second=start[1]+a[1][0]
    for i in range(1,n):
        up=min(first+a[0][i],second+value[1][i]+a[0][i])
        down=min(second+a[1][i],first+value[0][i]+a[1][i])
        first,second=up,down
    first+=end[0]
    second+=end[1]
    print(min(first,second))
if __name__ == '__main__':
    a = [[ 4, 5, 3, 2 ], 
        [ 2, 10, 1, 4 ]] 
    b = [[ 0, 7, 4, 5 ], 
        [ 0, 9, 2, 8 ]]
    start = [ 10, 12 ] 
    end = [ 18, 7 ] 
    Method_1(a,b,start,end)
    Method_2(a,b,start,end)