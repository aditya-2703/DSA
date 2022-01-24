# 1. You are given a graph.
# 2. You are required to find and print if the graph is bipartite

# Note -> A graph is called bipartite if it is possible to split it's vertices in two sets of mutually 
#                exclusive and exhaustive vertices such that all edges are across sets.

# GRAPH IS BIPARTITE 
# WHEN -> GRAPH IS ACYCLIC
#      -> GRAPH HAS EVEN CYCLE  



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
class Pair:
    def __init__(self,node,level):
        self.node = node
        self.level = level
# So as above conditions we conclude that if there is odd cycle then graph is not bipartite so will detact odd cycle 
# will take pair for all vertex and we put the level in the vertext by default it is 0
# will maintain visited as usual but this time visited contain level of the node 
# so if there is some element which has already visited so that node level is recorded and will check its  level with our level if same then continue else return false
# this method is work because in even cycle the number of vertexes is even so we able to distribute equally in both set 
# but in odd cycle there is always one element left which want to come in both sets which is not possible 


def is_bipartite(graph , n): 
    q = []
    q.append(Pair(0,0))
    visited  =[-1]*n
    while q:
        curr_node = q.pop(0)
        if visited[curr_node.node]==-1:
            visited[curr_node.node]  = curr_node.level
            
            for node in graph[curr_node.node]:
                if visited[node]==-1:
                    q.append(Pair(node,curr_node.level+1))
        else:
            if curr_node.level != visited[curr_node.node]:
                return False
    return True






if __name__ == '__main__':
    V = 7
    g = Graph(V)
    g.add_edge(0 ,1)
    g.add_edge(1 ,2)
    g.add_edge(2 ,3)
    g.add_edge(0 ,3)
    g.add_edge(3 ,4)
    g.add_edge(4 ,5)
    g.add_edge(5 ,6)
    g.add_edge(4 ,6)
    g.make_edge_dict()
    ans = is_bipartite(g.graph_dict,V)
    print(ans)