def open_parenthesis(n):
    left=right=n
    openpar,closepar="{","}"
    result=[]
    def backtrack(left=n,right=n,string=""):
        if not left and not right:
            result.append(string)
        if left:
            backtrack(left-1,right,string+openpar)
        if right and right>left:
            backtrack(left,right-1,string+closepar)

    backtrack()
    return result
if __name__ == '__main__':
    print(*open_parenthesis(4),sep="\n")
    