# 1. You are given a graph.
# 2. You are required to find and print all connected components of the graph.

# Sample Input
# 7
# 5
# 0 1 10
# 2 3 10
# 4 5 10
# 5 6 10
# 4 6 10

# Sample Output
# [[0, 1], [2, 3], [4, 5, 6]]

class Graph:
    def __init__(self,vertex):
        self.V = vertex
        self.edge = [[]for i in range(self.V)]
    def addEdge(self,vertex,edge):
        self.edge[vertex].append(edge)
        self.edge[edge].append(vertex)
    def Dfs(self,node,visited,components):
        visited[node]=True
        components.append(node)
        for each_node in self.edge[node]:
            if visited[each_node]==False:
                components=self.Dfs(each_node,visited,components)
        return components 
    def connectedComponents(self,visited):
        result=[]
        for node in range(self.V):
            if visited[node]==False:
                components = self.Dfs(node,visited,[])
                result.append(components)
        return result
if __name__ == '__main__':
    vertex=5
    g = Graph(vertex)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    cc = g.connectedComponents([False]*vertex)
    print(cc)
    