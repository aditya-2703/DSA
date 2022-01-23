# Perfect Friends

# 1. You are given a number n (representing the number of students). Each student will have an id 
#      from 0 to n - 1.
# 2. You are given a number k (representing the number of clubs)
# 3. In the next k lines, two numbers are given separated by a space. The numbers are ids of 
#      students belonging to same club.
# 4. You have to find in how many ways can we select a pair of students such that both students are 
#      from different clubs.

# Sample Input
# 7
# 5
# 0 1
# 2 3
# 4 5
# 5 6
# 4 6
# Sample Output
# 16

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
    vertex=7
    g = Graph(vertex)
    g.addEdge(0 ,1)
    g.addEdge(2 ,3)
    g.addEdge(4 ,5)
    g.addEdge(5 ,6)
    g.addEdge(4 ,6)
    cc = g.connectedComponents([False]*vertex)
    result=0
    for i in range(len(cc)):
        for j in range(i+1,len(cc)):
            result+= len(cc[i]) * len(cc[j])
    print(result)