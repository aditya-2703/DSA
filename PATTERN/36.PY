#       * * *   * 
#           *   * 
#       * * * * * 
#       *   *     
#       *   * * *




n = 5

first = n//2 + 1 
second = n//2 

for i in range(first):
    
    if i==0 or i==second:
        print("* "*second,end="")
    else:
        print("  "*(second),end="")

    if i==second:
        print("* ",end="")
    else:
        print("* ",end="")
    space = second-1
    if i!=second:
        print("  "*space,end="")
    else:
        print("* "*(second-1),end="")

    print("* ",end="")
    
    print()


for i in range(second):
    
    print("* ",end="")

    print("  "*(second-1),end="")

    print("* ",end="")
    

    if i==second-1:
        print("* "*second,end="")
    else:
        print("  "*second,end="")
    print()    