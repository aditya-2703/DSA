# 23.    *       * 
#        * *   * * 
#        *   *   * 
#        *       * 
#        *       * 





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
    


