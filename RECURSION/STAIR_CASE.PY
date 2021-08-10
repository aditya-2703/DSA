# INPUT - N=4
# OUTPUT - ['1111', '112', '121', '13', '211', '22', '31']
# Explanation - here we have n stairs so the options are 1,2,3 steps
# so we have to print all the possible steps like if we choose 1 then for 4 stairs we have 1111 option likewise for 2 we have 22
def stair_case(n):
    if n==0:
        return [""]
    elif n<0:
        return []
    path1 = stair_case(n-1)
    path2 = stair_case(n-2)
    path3 = stair_case(n-3)
    result=[]
    for i in path1:
        result.append("1"+i)
    for i in path2:
        result.append("2"+i)
    for i in path3:
        result.append("3"+i)

    return result

if __name__ == '__main__':
    n=4
    result = stair_case(n)
    print(result)