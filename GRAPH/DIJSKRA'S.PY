class Shortest_path:
    def __init__(self,size,graph):
        self.size=size
        self.graph=graph
        self.INF=999999999999
    def min_distance(self,min_path,marked):
        minval=self.INF
        min_index=0
        for i in range(self.size):
            if min_path[i]<minval and marked[i]==False:
                minval=min_path[i]
                min_index=i
        return min_index
    def printSolution(self, dist): 
        print ("Vertex tDistance from Source") 
        for node in range(self.size): 
            print (node, "t", dist[node])
    def dijskras(self,src):
        marked=[False]*self.size
        min_path=[self.INF]*self.size
        min_path[src]=0
        for i in range(self.size):
            u=self.min_distance(min_path,marked)

            marked[u]=True
            for j in range(self.size):
                if  self.graph[u][j]>0 and marked[j]==False and min_path[j]>min_path[u]+self.graph[u][j]:
                    min_path[j]=min_path[u]+self.graph[u][j]  
        self.printSolution(min_path)
     
if __name__ == '__main__':

    graph =[[0,10,5,0,7],
            [10,0,3,1,0],
            [5,3,0,9,2],
            [0,1,9,0,6],
            [7,0,2,6,0]]
    obj=Shortest_path(len(graph),graph)
    obj.dijskras(0)
