# n n n n n
# m
# m
# m
# m
# m
# m
# INPUT - matrix = [["s",0,0],[0,0,0],[0,0,"d"]] ,source = 0,0 ,destination = len(matrix)-1,len(matrix[0])-1 
# OUTPUT -  return all possible paths to reach to destination from source with jumps also here u can also take jump 1,2,3 so return arr of paths acc to steps

def find_maze(maze,sm,sn,dm,dn):
    if maze[sm][sn]=="d":
        return [" "]
        
    result=[]
    for right in range(1,dn-sn+1):
        path = find_maze(maze,sm,sn+right,dm,dn)
        for i in path:
            result.append(f"Right->{right}->{i}")
    for down in range(1,dm-sm+1):
        path = find_maze(maze,sm+down,sn,dm,dn)
        for i in path:
            result.append(f"Down->{down}->{i}")
    for diag_row in range(1,dm-sm+1):
        for diag_col in range(1,dn-sn+1):
            path = find_maze(maze,sm+diag_row,sn+diag_col,dm,dn)
            for i in path:
                result.append(f"Diag->{diag_col}->{i}")
        
    
    return result

if __name__ == '__main__':
    matrix = [["s",0,0],
                [0,0,0],
                [0,0,"d"]]
    source = [0,0]
    sm,sn=source
    destination = [2,2] 
    dm,dn = destination
    result = find_maze(matrix,sm,sn,dm,dn)
    for i in result:
        print(i)