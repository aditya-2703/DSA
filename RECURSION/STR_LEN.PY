# INPUT : "ABCDabc  "
# OUTPUT: 7
# Explanation : in this problem you just have to return length of string 


# METHOD-1 TAKES O(N) TIME AND O(1)(n for recursion stack frames) SPACE COMPLEXITY
def Method_1(string,i):
    if string[i]==" ":
        return 0
    
    return 1+Method_1(string,i+1)

    

if __name__ == '__main__':
    string = "abcdefgh    "
    length = Method_1(string,0)
    print(length)
    