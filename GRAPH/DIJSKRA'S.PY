# graph 
# -----------------------------------------------------------------------------------------------------------
#           0-------[10]------1\
#           |               / | \
#           |           /     |  [9]  
#          [30]    [20]      [5]   2  
#           |    /            |   /
#           | /               |  [8]
#           4 ------[40]------3 /
# 
# -----------------------------------------------------------------------------------------------------------

# each vertex has object of class vertex 
# 0 -> [vertex,vertex]
# vertex = vertex-0 , weight-10 , edge-1

import queue


class Graph:
    def __init__(self,graph,size,weight_matrix):
        self.edge = graph
        self.size = size
        self.weight_matrix = weight_matrix
    
    def dikstra(self,src):
        pq = queue.PriorityQueue()
        visited = [False]*self.size
        visited[src]=True
        pq.put((0,src))
        shortest_paths = ""
        while pq.queue:
            nodes_weight,node = pq.get()
            visited[node]=True
            for each_node in self.edge[node]:
                if visited[each_node]==False:
                    u = node
                    v = each_node
                    weight = min(self.weight_matrix[u][v]  + nodes_weight,self.weight_matrix[u][v])
                    pq.put((weight,each_node))
                    msg = f"{u} to {v}"

                    shortest_paths+=msg + " -> " + str(weight) + "\n"
                    
        print(shortest_paths)
            
if __name__ == '__main__':
    inf = 99999999
    graph = {
        0:set([1,4]),
        1:set([0,2,3,4]),
        2:set([1,3]),
        3:set([1,2,4]),
        4:set([0,1,3]),
    }
    weight_list = [[inf,10,inf,inf,30],
                   [10,inf,9,5,20],
                   [inf,9,inf,8,inf],
                   [inf,5,8,inf,40],
                   [inf,20,inf,40,inf]]

    size = 5
    g = Graph(graph,size,weight_list)
    
    # print("edge",g.edge)

    g.dikstra(0)
    
