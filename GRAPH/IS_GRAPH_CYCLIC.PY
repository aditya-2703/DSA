# Input: n = 4
# 1. You are given a graph.
# 2. You are required to find and print if the graph is cyclic.
# 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3
# Output: Yes
# note : will not use directed graph 
# diagram - https://media.geeksforgeeks.org/wp-content/uploads/20200429134027/Untitled-Diagram1411.png





class Graph:
    def __init__(self,V):
        self.edge = [[]for i in range(V)]
    def add_edge(self,u,v):
        if len(self.edge)>1:
            if u not in self.edge[v]:
                self.edge[v].append(u)
            if v not in self.edge[u]:
                self.edge[u].append(v)
        else:
            self.edge[u] = [v]
            self.edge[v] = [u]    
    def make_edge_dict(self):
        self.graph_dict = {}
        for i,value in zip(range(len(self.edge)),self.edge):
            self.graph_dict[i] = value
    
# traverse the graph and find if graph visited then there is cycle 
# here will use bfs   
def is_graph_cyclic(graph,n):
    q = []
    visited = [False] * n
    q.append(0)
    while q:
        curr_ele = q.pop(0)
        if visited[curr_ele]==True:
            return True
        else:

            visited[curr_ele] = True
            for nbr in graph[curr_ele]:
                if visited[nbr]==False:
                    q.append(nbr)
    return False



if __name__ == '__main__':
    V = 4
    g = Graph(V)
    g.add_edge(0 ,1)
    g.add_edge(0 ,2)
    g.add_edge(1 ,2)
    g.add_edge(2 ,0)
    g.add_edge(2 ,3)
    g.add_edge(3 ,3)
    
    # g.add_edge(0 ,1)
    # g.add_edge(0 ,2)
    # g.add_edge(1 ,2)
    # g.add_edge(2 ,3)

    g.make_edge_dict()
    print(g.graph_dict)
    flag = is_graph_cyclic(g.graph_dict,V)
    print(flag)