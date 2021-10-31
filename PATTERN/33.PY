# 33.    a
#        B c
#        D e F
#        g H i J
#        k L m N o
     
n = 5
counter = 1
for row in range(n+1):


    for i in range(row):
        if row==1:
            print("a",end=" ")
        else:
            char = chr(counter+65)
            print(char,end=" ")
            counter+=1

    print()