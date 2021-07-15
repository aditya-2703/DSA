def duplicate_para(string):
    stack=[]
    for i in string:
        if i==")":
            if stack[-1]=="(":
                return True
            else:
                while stack and stack[-1]!="(":
                    stack.pop()
                stack.pop()
        else:
            stack.append(i)
    return False





    
if __name__=='__main__':
    string = "((a+b))+((c+d)))"
    if duplicate_para(string):  
        print("yes duplicate")
    else:
        print("no duplicate")