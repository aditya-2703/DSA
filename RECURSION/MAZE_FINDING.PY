# n n n n n
# m
# m
# m
# m
# m
# m
# INPUT - matrix = [["s",0,0],[0,0,0],[0,0,"d"]] ,source = 0,0 ,destination = len(matrix)-1,len(matrix[0])-1 
# OUTPUT -  return all possible paths to reach to destination from source
def find_maze(maze,sm,sn,dm,dn):
    if maze[sm][sn]=="d":
        return [" "]
    down_path=[]
    right_path=[]
    if sm<dm:
        down_path = find_maze(maze,sm+1,sn,dm,dn)
    if sn<dn:
        right_path = find_maze(maze,sm,sn+1,dm,dn)
    result = []
    for i in down_path:
        result.append("down-"+i)
    for i in right_path:
        result.append("right-"+i)

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
    print(result)