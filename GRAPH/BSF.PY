# graph 
# -----------------------------------------------------------------------------------------------------------
#           0-----------------1\
#           |               / | \
#           |           /     |  \  
#           |       /         |   2  
#           |    /            |   /
#           | /               |  /
#           4 ---------------3/
# 
# -----------------------------------------------------------------------------------------------------------

class Graph:
    def __init__(self,V):
        self.edge = {}
        self.list = [[]for i in range(V)]
    def addEdge(self,u,v):
        if len(self.list[u])>=1:
            if v not in self.list[u]:
                self.list[u].append(v)
        if len(self.list[v])>=1:
            if u not in self.list[v]:
                self.list[v].append(u)
        else:
            self.list[u]=[v]
            self.list[v]=[u]
    def make_dict(self,v):
        for i in range(v):
            self.edge[i]=self.list[i]
    def get_path(self,start):
        q = [start]
        result = []
        visited = [False]*len(self.edge)
        while q:
            node = q.pop(0)
            if visited[node]==False:    
                result.append(node)
                visited[node] = True
                for neighbor in self.edge[node]:
                    if visited[neighbor]==False:
                        q.append(neighbor)
                
        return result




if __name__ == '__main__':
    v = 5
    g = Graph(v)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(3, 4)
    g.addEdge(3, 2)
    g.make_dict(v)
    
    print(g.edge)

    result = g.get_path(2)
    print("result",result)
