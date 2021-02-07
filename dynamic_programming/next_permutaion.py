def next_permutation(L):
    # 1 2 6 5 4 
    # find desending order 6 5 4
    # find that pointer from which order breaks 2
    # swap with the next posible value from right 1 4 6 5 2
    # now reverse the right side 1 4 2 5 6 this is your answer
    length=len(L)
    pointer=length-2
    while pointer>=0 and L[pointer]>L[pointer+1]:
        pointer-=1
    if pointer==-1:
        return False
    for i in range(length-1,pointer,-1):
        if L[i]>L[pointer]:
            L[i],L[pointer]=L[pointer],L[i]
            break
    L[pointer+1:]=reversed(L[pointer+1:])
    return L

if __name__ == '__main__':
    L=[1,2,3,5,4]
    lsit=next_permutation(L)
    print(lsit)