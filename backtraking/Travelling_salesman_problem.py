from sys import maxsize
V=4
def tsp(graph,start):
    vertex=[int(i) for i in range(V) if start!=i]    
    # print(vertex)
    min_path=maxsize
    while True:
        current_path=0
        k=start
        for i in range(len(vertex)): 
            current_path += graph[k][vertex[i]] 
            k = vertex[i] 
        current_path += graph[k][start] 
        
        min_path=min(min_path,current_path)
        temp=next_permutation(vertex)
        if temp==False:
            break
    return min_path

def next_permutation(L):
    n=len(L)
    pointer=n-2
    while pointer>=0 and L[pointer]>L[pointer+1]:
        pointer-=1
    if pointer == -1:
        return False
    for i in range(n-1,pointer,-1):
        if L[pointer]<L[i]:
            L[i],L[pointer]=L[pointer],L[i]
            break
    L[pointer+1:]=reversed(L[pointer+1:])
    
    return True

if __name__ == '__main__':
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],  
             [15, 35, 0, 30], [20, 25, 30, 0]] 
    x=tsp(graph,0)
    print(x)
    