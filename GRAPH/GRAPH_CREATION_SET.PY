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
    def __init__(self,edge):
        self.edge = edge
    def get_path(self,start,end,path):
        path = path + [start]
        
        if start==end:
            return [path]

        if start not in self.edge:
            return []

        all_paths = []
        for node in self.edge[start]:
            if node not in path:
                new_path = self.get_path(node,end,path)
                for i in new_path:
                    all_paths.append(i)
        return all_paths


if __name__ == '__main__':
    route ={
        0:set([1,4]),
        1:set([0,2,3,4]),
        2:set([1,3]),
        3:set([1,2,4]),
        4:set([0,1,3]),
    }
    graph = Graph(route)
    path=[]
    print(graph.get_path(0,2,path))
    
