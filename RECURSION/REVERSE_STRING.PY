# Write a recursive function that, given a string s, prints the characters of s in reverse order
# input : "hey kiddo"
# output: "oddik yeh"


def reverse(string,curr,n):
    if n==0:
        return curr
    curr+=string[n-1]
    return reverse(string,curr,n-1)

def Method_1(string):
    curr=""
    result=reverse(string,curr,len(string))
    return result
if __name__ == '__main__':
    string="hey kiddo"
    print(Method_1(string))