def karastuba(x,y):
    if len(x)<10  and  len(y)<10:
        return int(x)*int(y)
    if len(x) < len(y):
        x.zfill(len(str(y))-len(x))
    if len(y) < len(x):
        y.zfill(len(str(x))-len(y))
    else:
        m=len(x)//2
        a=x[:m]
        b=x[m:]
        c=y[:m]
        d=y[m:]

        ac=karastuba(a,c)
        bd=karastuba(b,d)
        ac_plus_bd= karastuba(a+b,c+d)-ac-bd

        return pow(10,len(str(x)))*ac + pow(10,len(str(x)//2))*ac_plus_bd+bd

if __name__ == "__main__":
    num1=2345
    num2=4535
    x=str(num1)
    y=str(num2)
    result=karastuba(x,y)
    print(result)
