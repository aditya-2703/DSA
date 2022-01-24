# Spread Of Infection

# 1. You are given a graph, representing people and their connectivity.
# 2. You are also given a src person (who got infected) and time t.
# 3. You are required to find how many people will get infected in time t, if the infection spreads to neighbors of infected person in 1 unit of time.

class Graph:
    def __init__(self,V,flag):
        self.edge = [[]for i in range(V)]
        self.graph_dict = {}
        self.flag = flag
    def add_edge(self,u,v):
        if len(self.edge)>1:
            if u not in self.edge[v]:
                self.edge[v].append(u)
            if v not in self.edge[u]:
                self.edge[u].append(v)
        else:
            self.edge[u] = [v]
            self.edge[v] = [u]    
        self.graph_dict = {}
        if self.flag:
            self.make_edge_dict()
    def make_edge_dict(self):
        for i,value in zip(range(len(self.edge)),self.edge):
            self.graph_dict[i] = value
class Pair:
    def __init__(self,node,level):
        self.node = node
        self.level = level


# Here in this problem will use bfs because it increases in radius 
# will maintain pair object for each node which has (node ,level) the level indicate alert when it increase compare to time 
# if time < level of any node will break the loop 
# there is also one variable called count which maintain the count of all nodes or vertex which we have to return 
def get_infection_count(graph,src,time,n):
    q = []
    count=0
    visited = [False]*n
    q.append(Pair(src,1))
    while q:
        node = q.pop(0)
        if visited[node.node]==False:
            if node.level>time:
                break
            visited[node.node] = True
            for nbr in graph[node.node]:
                if visited[nbr]==False:
                    q.append(Pair(nbr,node.level+1))
            count+=1
    return count



if __name__ == '__main__':
    V = 7
    g = Graph(V,True)
    g.add_edge(0 , 1)
    g.add_edge(1 , 2)
    g.add_edge(2 , 3)
    g.add_edge(0 , 3)
    g.add_edge(3 , 4)
    g.add_edge(4 , 5)
    g.add_edge(5 , 6)
    g.add_edge(4 , 6)
    src = 6 
    time = 3
    ans = get_infection_count(g.graph_dict,src,time,V)
    print(f"No of person will infected is {ans}")