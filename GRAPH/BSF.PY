from collections import defaultdict as d

class BFS:

    def __init__(self,graph):
        self.graph=graph
    def bfs(self,start):
        check=[False]*len(self.graph)
        queue=[]

        queue.append(start)
        check[start]=True

        while queue:

            start=queue.pop(0)
            print(start,end=" ")

            for i in self.graph[start]:
                i=int(i)
                if check[i]==False:
                    queue.append(i)
                    check[i]=True
                
if __name__ == '__main__':
    graph = {0: set(['1', '2','3']),
        1: set(['0', '2', '4']),
        2: set(['0','1']),
        3: set(['0']),
        4: set(['1'])}
    obj=BFS(graph)

   

    obj.bfs(0)    