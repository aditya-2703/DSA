# input string="ABC"
# output ABC ACB BAC BCA CBA CAB
# explanation:  
#                                    abc        
#                             /       |       \   
#                        a(bc)     b(ac)    c(ab)    
#                        /  \      /  \      /   \
#                   ab(c) ac(b) ba(c) bc(a) ca(b) cb(a)

def swap(string,l,i):
    result=""
    for s in range(len(string)):
        if s==l:
            result+=string[i]
        elif s==i:
            result+=string[l]
        else:
            result+=string[s]
    return result
        
def Method_1(string,l,r):
    if l==r:
        print(string)
        return 
    for i in range(l,r+1):
        string=swap(string,l,i)
        Method_1(string,l+1,r)
        string=swap(string,l,i)
if __name__ == "__main__":
    string="ABC"
    Method_1(string,0,len(string)-1)