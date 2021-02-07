class Graph:
    def __init__(self,totalsize):
        self.totalsize=totalsize
        self.graph=[[]for i in range(self.totalsize)]
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def Dfs(self,node,listvisited,visited):
        visited[node]=True
        listvisited.append(node)
        for i in self.graph[node]:
            if visited[i]==False:
                listvisited=self.Dfs(i,listvisited,visited)  
        return listvisited
    def connectedComponents(self):
        visited=[False]*self.totalsize
        cc=[]
        for i in range(self.totalsize):
            if visited[i]==False:
                cc.append(self.Dfs(i,[],visited))
        return cc

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
    