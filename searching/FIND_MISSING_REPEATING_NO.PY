from math import *
# Input
# [2, 3, 2, 1, 5]
# Output
# 4 2

# METHOD 1 -- O(N LOGN) TIME AND O(1) SPACE COMPLEXITY
# WE SORT THE ARRAY AND FIND BOTH ONE BY ONE
def bin_search(arr,l,r,element):
    if l<r:
        mid=(l+(r-1))//2
        if arr[mid]==element:
            return True
        elif element>arr[mid]:
            l=mid+1
        else:
            r=mid-1
    return False
def Method_1(arr):
    arr.sort()
    store=0
    missing=0
    temp=0
    for i in range(len(arr)):
        if arr[i]==arr[i-1]:
            store=arr[i]
    for i in range(len(arr)-1):
        temp=arr[i]
        if temp==arr[i+1]-1:
            continue
        else:
            missing=arr[i]+1

    return [missing,store]

# METHOD 2 -- O(N) TIME AND O(1) SPACE COMPLEXITY
# HERE WE USE PRODUCT AND SUM FORMULA
# sum = n(n+1)//2 - x + y 
# product = n! *y/x
def Method_2(arr):
    totsum=0
    sum=0
    totprouct=1
    prouct=1
    n=len(arr)
    for i in range(n):
        totsum+=arr[i]
        totprouct*=arr[i]
    sum=n*(n+1)//2
    prouct=factorial(n)
    # sum=totsum - x + y
    # prouct = totprouct *y/x
    x=0
    y=0
    # print(totsum, sum , totprouct, prouct)
    y=((totsum-sum)*prouct)//(totprouct-prouct) 
    x=totsum-sum+y
    return [y,x]

# METHO 3
# IN ABOVE METHOD THERE IS ARITHMETIC OVERFLOW SO OR REDUCE TAHT OR SOLVE THIS WE USE HASHING WHICH TAKES O(N) TIME AND O(N) SPACE COMPEXITY
def Method_3(arr):
    n=len(arr)
    count=[0]*(n+1)
    missing=0
    repeating=0
    for i in range(len(arr)):
        count[arr[i]]+=1
    for i in range(1,len(arr)):
        if count[i]==0:
            missing=i
        if count[i]==2:
            repeating=i
    return [missing,repeating]


# METHOD 4 -- O(N) TIME ANS O(1) SPACE COMPLEXITY
# HERE IN METHOD 3 IT TAKES N TIME OF SPACE SO FOR REDUCE THIS WE USE NEGATIVE INDEXING IN THIS METHOD 
def Method_4(arr):
    temp=missing=repeating=0
    for i in range(len(arr)):
        temp=arr[abs(arr[i])-1]
        if temp<0:
            repeating=arr[i]
            break
        arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
    for i in range(len(arr)):
        if arr[i]>0:
            missing=i
    return [missing,repeating]

if __name__ == '__main__':
    arr=[1, 3, 2, 1, 5]
    lsit=Method_1(arr)
    print(f"FOR ARRAY {arr} THE MISSING ELEMENT IS {lsit[0]} AND REPEATING ELEMENT IS {lsit[1]}")
    newist=Method_2(arr)
    print(f"FOR ARRAY {arr} THE MISSING ELEMENT IS {newist[0]} AND REPEATING ELEMENT IS {newist[1]}")
    newist1=Method_3(arr)
    print(f"FOR ARRAY {arr} THE MISSING ELEMENT IS {newist1[0]} AND REPEATING ELEMENT IS {newist1[1]}")
    arr=[1, 3, 2, 1, 5]
    newlist=Method_4(arr)
    print(f"FOR ARRAY {arr} THE MISSING ELEMENT IS {newlist[0]} AND REPEATING ELEMENT IS {newlist[1]}")
