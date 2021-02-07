# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i

def Method_1(s):#locha
    newlist=[]
    ns=""
    for i in range(len(s)):
        while s[i]!=".":
            ns+=s[i]
        print(ns)
    # return newlist
if __name__ == '__main__':
    s="i.like.this.program.very.much"
    print(Method_1(s))
    