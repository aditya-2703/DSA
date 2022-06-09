# graph 

# minimum spaning tree
# it is the type of subgraph which has minimum number of weight sum with n vertex and n-1 edge

import heapq as hq

class Edge:
    def __init__(self,node,nbr,wt):
        self.node = node
        self.nbr = nbr 
        self.wt = wt

class Pair:
    def __init__(self,node,prev_node,wt):
        self.node = node
        self.prev_node = prev_node
        self.wt = wt
    def __lt__(self,other):
        return self.wt < other.wt

def get_minimum_spaing_tree(graph,n):
    pq = [] 
    hq.heappush(pq,(0,(Pair(0,-1,0))))
    visited = [False]*n
    while pq:
        wt , node = hq.heappop(pq)
        if visited[node.node]==False:
            visited[node.node] = True
            print(f"Node: {node.prev_node} -> {node.node} at weight {node.wt}")
            print(graph[node.node])
            for v,nbr,wt in graph[node.node]:
                hq.heappush(pq,(nbr.wt,(Pair(nbr,node.node,wt))))
    

if __name__ == '__main__':
    V = 7
    g = []
    g.append(Edge(1 ,0 ,10))
    g.append(Edge(1 ,2 ,10))
    g.append(Edge(2 ,3 ,10))
    g.append(Edge(0 ,3 ,40))
    g.append(Edge(3, 4, 2))
    g.append(Edge(4, 5, 3))
    g.append(Edge(5, 6, 3))
    g.append(Edge(4, 6, 8))
    get_minimum_spaing_tree(g,V)







