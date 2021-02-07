def range_query(lsit,i,j):
    newlist=[0]*(len(lsit)+1)
    for i1 in range(len(lsit)):
        newlist[i1+1]=newlist[i1]+lsit[i1]
    return (newlist[j+1]-newlist[i])

if __name__ == '__main__':
    lsit=[4,5,345,3,5,43,5,34,53,45,43,543]
    print(range_query(lsit,3,8))
    