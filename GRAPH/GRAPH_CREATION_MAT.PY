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
    def __init__(self,matrix):
        self.V = len(matrix)
        self.edge = self.get_edge(matrix)
        self.neighbors=self.get_neighbors()
    def get_edge(self,matrix):
        edge=[[] for i in range(self.V)]
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col]==1:
                    if (col not in edge[row]) and (row not in edge[col]):
                        edge[row].append(col)
                        edge[col].append(row)
        for value in edge:
            value.sort()
        return edge
    def get_neighbors(self):
        neighbors={}
        for i in range(self.V):
            neighbors[i] = self.edge[i]
        return neighbors
    def get_path(self,start,end,path):
        path=path+[start]

        if start==end:
            return [path]

        if start not in range(self.V):
            return []
        
        all_path=[]
        for node in self.edge[start]:
            if node not in path:
                old_paths = self.get_path(node,end,path)
                for each_path in old_paths:
                    all_path.append(each_path)
        return all_path

if __name__ == '__main__':
    matrix=[[0,1,0,0,1],
            [1,0,1,1,1],
            [0,1,0,1,0],
            [0,1,1,0,1],
            [1,1,0,1,0]] 

    obj = Graph(matrix)
    print(obj.get_path(0,2,[]))    
    