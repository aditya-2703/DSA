# Hamiltonian Path And Cycle

# 1. You are given a graph and a src vertex.
# 2. You are required to find and print all hamiltonian paths and cycles starting from src. The cycles must end with "*" and paths with a "."

# Note -> A hamiltonian path is such which visits all vertices without visiting any twice. A hamiltonian path becomes a cycle if there is an edge between first and last vertex.
# Note -> Print in lexicographically increasing order.


# Sample Input
# 7
# 9
# 0 1 10
# 1 2 10
# 2 3 10
# 0 3 10
# 3 4 10
# 4 5 10
# 5 6 10
# 4 6 10
# 2 5 10
# 0

# Sample Output
# 0123456.
# 0123465.
# 0125643*
# 0346521*

class Graph:
    def __init__(self,vertex):
        self.V = vertex
        self.edge = [[]for i in range(self.V)]
    def addEdge(self,vertex,edge):
        self.edge[vertex].append(edge)
        self.edge[edge].append(vertex)
    def get_path(self,init_pos,node,visited,path):
        if len(visited)+1==self.V:
            if init_pos in self.edge[node]:
                print(f"{path}*")
            else:
                print(f"{path}.")
            return 
        visited.append(node)
        for each in self.edge[node]:
            if each not in visited:
                self.get_path(init_pos,each,visited,path+str(each))
        visited.remove(node)
         
    def get_solution(self):
        visited = []
        self.get_path(0,0,visited,"0")

if __name__ == '__main__':
    vertex=7
    g = Graph(vertex)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(3, 0)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 6)


    cc = g.get_solution()
    