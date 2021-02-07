def DFS(graph,visited,node):
    if node not in visited:
        print(node)
        visited.add(node)

        for n in graph[node]:
            DFS(graph,visited,n)


if __name__ == '__main__':
    graph = {'0': set(['1', '2','3']),
        '1': set(['0', '2', '4']),
        '2': set(['0','1']),
        '3': set(['0']),
        '4': set(['1'])}
    visited=set()
    DFS(graph,visited,'0')