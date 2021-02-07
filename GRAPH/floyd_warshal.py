def floyd_washel(graph,n):

    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[i][j]=min(graph[i][j],(graph[i][k]+graph[k][j]))
    return graph


if __name__=='__main__':
    INF=9999
    graph = [[0,5,INF,10], 
            [INF,0,3,INF], 
            [INF,INF,0,1], 
            [INF,INF,INF,0]] 
    new_graph=floyd_washel(graph,len(graph))
    for i in new_graph:
        print(i)