# INPUT : "abcabcabcaa"
# OUTPUT : "abcabcabca"
# EXPLANATION : remove consiqutive duplicates elemenet in this case aa is consicutive duplicate element so we remove it and only add one"a" to outptu



# METHOD -1 TAKES O(N) TIME AND O(1)(n for recursion stack frames) SPACE COMPLEXITY 
def Method_1(string,index,output):
    if index==len(string):
        return output
    if string[index]==string[index-1]:
        return Method_1(string,index+1,output)
    else:
        output+=string[index]
        return Method_1(string,index+1,output)
    
if __name__ == '__main__':
    string = "abcabcabcaa "
    output = Method_1(string,0,"")
    print(output)

    