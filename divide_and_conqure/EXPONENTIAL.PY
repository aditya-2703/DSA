# input x,y
# calculate x^y 

 
# METHOD 1 -- TAKES O(Y) TIME ANS O(Y) SPACE COMPLEXITY 
# HERE SPACE COMPLEXITY BECAME O(1) BUT IF WE GO IN THE DEEP IT USES Y TIMES STACK BECAUSE OF CALLING FUNCTION Y TIMES 
def Method_1(x,y):
    if y==0:
        return 1
    elif y%2==0:
        return Method_1(x,y//2)*Method_1(x,y//2)
    else:
        # if y>0:
        return x*Method_1(x,y//2)*Method_1(x,y//2)
        # else:
        #     return (Method_1(x,y//2)*Method_1(x,y//2))/x


# ===========================OR==========================


def Method_1(x,y):
    if y==0:
        return 1
    else:
        return x*Method_1(x,y-1)



# METHOD 2 -- TAKES O(LOGN) TIME AND O(1) SPACE COMPLEXTY(not going to deep about stack frames)
def Method_2(x,y):
    if y==0:
        return 1
#    here we store and value for optimization 
    temp=Method_2(x,int(y/2))
    if y%2==0:
        return temp*temp
    else:
        if y>0:
            return x*temp*temp
        else:
            return (temp*temp)/x



if __name__ == '__main__':
    print(Method_1(2,3))
    print(Method_2(2,3))
    