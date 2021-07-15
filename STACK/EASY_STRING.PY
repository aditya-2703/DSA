

def is_same(stack,value):
    if not stack:
        stack.append(value)
        return True
    else:
        if stack[-1]==value or abs(ord(stack[-1])-ord(value))==32:
            return True
    return False

def get_distinct(string):
    mystack=[]
    mystack.append(string[0])
    for i in string[1:]:
        if not is_same(mystack,i):
            mystack.append(i)
    return "".join(mystack)

def main(string):
    stack=[]
    count=0  
    array_count=[]
    for i in string:
        if is_same(stack,i):
            count+=1
        else:
            array_count.append(count)
            count=1
            stack.append(i)
    result=get_distinct(string)
    array_count.append(count)
    answer=""
    for i in range(len(array_count)):
        answer += str(array_count[i]) + result[i].lower() 
    print(answer)
    

if __name__ == '__main__':
    S = "aaacca"
    # S="aaABBb"
    main(S)