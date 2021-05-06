# input string="racecar"
# output YES PALINDROME 
# explanation: 
    # racecar == racecar(reverse of string)
def reverse(string):
    result=""
    for i in range(len(string)-1,-1,-1):
        result+=string[i]
    return result

# METHOD 1 -- TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_1(string):
    if reverse(string)==string:
        return "YES PALINDROME"
    return "NO NOT PALINDROME"

# METHOD 2 -- TAKES O(N) TIME AND O(1) SPACE COMPLEXITY
def Method_2(string,l,r):
    if l>=r:
        return "YES PALINDROME"
    elif string[l]!=string[r]:
        return 'NO NOT PALINDROME'
    return Method_2(string,l+1,r-1)
# -------------------------------RECURSION-----------------------------------

# METHOD 3 
def Method_3(string):
    pass
if __name__ == "__main__":
    string="racecar"
    print(Method_1(string))
    print(Method_2(string,0,len(string)-1))
    print(Method_3(string))