# INPUT : "ABCXBCAXXXABC "
# OUTPUT : "ABCBCAABC"
# EXPLANATION : YOU JUST HAVE TO REMOVE ALL THE X FROM STRING


# METHOD -1 TAKES O(N) TIME AND O(1)(n for recursion stack frames) SPACE COMPLEXITY 
def Method_1(string,index,output,key):
    if index==len(string):
        return output
    if string[index] not in key:
        output += string[index]
        return Method_1(string,index+1,output,key)
    else:
        return Method_1(string,index+1,output,key)

if __name__ == '__main__':
    string = "ABCXBCAXXXABC "
    output = Method_1(string,0,"","Xx")
    print(output)

    