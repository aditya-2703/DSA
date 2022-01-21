class Neighbor:
    def __init__(self,vertex):
        self.vertex=vertex
        self.next = None
    
class Graph:
    def __init__(self,vertex):
        self.V = vertex 
        self.edge = [None]*self.V

    def add_edge(self,vertex,edge):
        node = Neighbor(edge)
        node.next = self.edge[vertex]
        self.edge[vertex] = node

        node = Neighbor(vertex)
        node.next = self.edge[edge]
        self.edge[edge]=node
        
    def get_edge(self,vertex):
        temp = self.edge[vertex]
        string = ""
        while temp:
            string+=str(temp.vertex)+"->"
            temp=temp.next
        return string

    def is_consists(self,value):
        temp = self.edge
        for i in temp:
            if i==value:
                return True
        return False
    
    def get_path(self,start,end,path):
        if start==end:
            # print(path)
            return [path]
        if start not in range(self.V):
            return []
            
        temp = self.edge[start]
        all_paths=[]
        while temp:
            value = temp.vertex
            if value not in path:
                old_paths = self.get_path(value,end,path+[temp.vertex])
                for each in old_paths:
                    all_paths.append(each)
            temp=temp.next
        return all_paths

if __name__ == '__main__':
    vertex = 5
    obj = Graph(vertex)
    obj.add_edge(0, 1)
    obj.add_edge(0, 4)
    obj.add_edge(1, 2)
    obj.add_edge(1, 3)
    obj.add_edge(1, 4)
    obj.add_edge(2, 3)
    obj.add_edge(3, 4)
    
    for i in range(vertex):
        print(f"vertex {i} edge {obj.get_edge(i)}")
    all_paths = obj.get_path(0,2,[0])
    print(all_paths)
