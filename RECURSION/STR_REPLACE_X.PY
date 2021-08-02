# INPUT : "ABCXBCAXXXABC " c1=x c2=y
# OUTPUT :"ABCYBCAYYYABC"
# EXPLANATION : YOU JUST HAVE TO REMOVE ALL THE X FROM STRING


# METHOD -1 TAKES O(N) TIME AND O(1)(n for recursion stack frames) SPACE COMPLEXITY 
def Method_1(string,index,output,c1,c2):
    if index==len(string):
        return output
    if string[index] != c1:
        output += string[index]
        return Method_1(string,index+1,output,c1,c2)
    else:
        output += c2
        return Method_1(string,index+1,output,c1,c2)

if __name__ == '__main__':
    string = "ABCXBCAXXXABC "
    c1="X"
    c2="Y"
    output = Method_1(string,0,"",c1,c2)
    print(output)

    