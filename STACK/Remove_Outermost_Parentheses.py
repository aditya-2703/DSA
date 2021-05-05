# Example 1:
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# METHOD 1 -- TAKES O(N) TIME AND O(N) SPACE COMPLEXITY
# here we ignore outer paranthesis and check the inner one 
# (()())(()) count=0
# (          count=1
# ((         count=2 result=(
# (()        count=1 result=()
# (()(       count=2 result=()(
# (()()      count=1 result=()()
# (()())     count=0 result=()()
# (()())(    count=1 result=()()
# (()())((   count=2 result=()()(
# (()())(()  count=1 result=()()()
# (()())(()) count=0 result=()()()

def Method_1(string):
    result=""
    para={"left":"(","right":")"}
    count=0
    for i in string:
        if (count>0 and i==para["left"]):
            result+=i
        if (i==para["left"]):
            count+=1
        if (count>1 and i==para["right"]):
            result+=i
        if (i==para["right"]):
            count-=1
    return result




if __name__ == '__main__':
    string="(()())(())(()(()))"
    print(Method_1(string))
