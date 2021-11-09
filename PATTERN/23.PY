# 23.    *       * 
#        * *   * * 
#        *   *   * 
#        *       * 
#        *       * 


# n=3
# row no  = 0 1 2 
# outspace= 4 2 0  
# col no  = 2 1 0 1 2 1 0 1 2 (3*n)
# outspace= 2 1 0


n = 5

first = n//2 + 1  
second = n//2 
for i in range(first):
    
    print("* ",end="")
    
    f_inner_space = i-1
    print("  "*f_inner_space,end="")
    
    if i!=0:
        print("* ",end="")
    
    s_inner_space = (n-1) - 2*i -1 
    print("  "*s_inner_space,end="")
    
    if i!=first-1:
        print("* ",end="")
    
    print("  "*f_inner_space,end="")
    
    if i!=0:
        print("* ",end="")
    print()
    
    
for i in range(second):
    print("* ",end="")
    
    inner_space = n-2
    print("  "*inner_space,end="")
    
    
    print("* ",end="")
    
    print()
    


