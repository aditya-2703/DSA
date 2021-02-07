INF = 9999999
V = 5

G = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 



selected = [0, 0, 0, 0, 0]

selected[0] = True

print("Edge : Weight\n")
for k in range(V-1):

    
    minimum = INF
    source = 0
    destination = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  

                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        source = i
                        destination = j
    print(str(source) + "-" + str(destination) + ":" + str(G[source][destination]))
    selected[destination] = True
