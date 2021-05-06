# INPUT N=3 M=4
# OUTPUT 10
# EXPLANATION:
# ___ ___ ___ ___    MOVE -----> RIGHT 
#|_X_|___|___|___|      |
#|___|___|___|___|      |          only
#|___|___|___|___|      |
#|___|___|___|_Y_|      V BOTTOM

# WE HAVE TO FIND HOW MANY NUMBER OF WAYS THAT 'X' REACH TO THE 'Y' BUT HERE WE ONLY GO BOTTOM OR RIGHT 

# base case : 
        #  ________________________
        # |_x_|___|___|___|___|_y_| move ---> right 
        # 1.if only  one row ans - 1
        # ____  move
        #|_x_|    |   
        #|___|    | 
        #|___|    | 
        #|_y_|    V  bottom 
        # 2.if only one column ans -1
#relation : 
        # so here we conclude that m,n-->m-1,n
        #                            |__>m,n-1           
# generalize
        # m,n = (m-1,n)+(m,n-1)
def Method_1(m,n):
    if m==1 or n==1:
        return 1
    return Method_1(m-1,n)+Method_1(m,n-1)

if __name__ == "__main__":
    m=3
    n=4
    print(Method_1(m,n))