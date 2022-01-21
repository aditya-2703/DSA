# Is Graph Connected

# 1. You are given a graph.
# 2. You are required to find and print if the graph is connected (there is a path from 
#      every vertex to every other).

# Sample Input
# 7
# 5
# 0 1 10
# 2 3 10
# 4 5 10
# 5 6 10
# 4 6 10
# Sample Output
# false

class Graph:
    def __init__(self,vertex):
        self.V = vertex
        self.edge = [[]for i in  range(vertex)]
    def add_edge(self,u,v):
        self.edge[u].append(v)
        self.edge[v].append(u)
    def Dfs(self,node,visited,compo_list):
        visited[node]=True
        compo_list.append(node)
        for each in self.edge[node]:
            if visited[each]==False:
                compo_list = self.Dfs(each,visited,compo_list)
        return compo_list
    def is_connected(self):
        visited = [False]*self.V
        result=[]
        for i in range(self.V):
            if visited[i]==False:
                result.append(self.Dfs(i,visited,[]))
        return len(result)==1
        
if __name__ == '__main__':
    vertex = 7
    obj = Graph(vertex)
    obj.add_edge(0,1)
    obj.add_edge(2,3)
    obj.add_edge(4,5)
    obj.add_edge(5,6)
    obj.add_edge(4,6)
    
    
    is_graph_connected = obj.is_connected()
    print(is_graph_connected)