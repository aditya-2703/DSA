# Input:
# ip = 222.111.111.111
# Output: 1
def Method_1(s):
    a,b,c,d=(s.split("."))
    if (a=="" or int(a)<=255) and (b=="" or int(b)<=255)  and (c=="" or int(c)<=255) and (d=="" or int(d)<=255):
        return 1 
    return 0

def Method_2(s):
    counter=0
    for i in range(0,len(s)):
        if(s[i]=='.'):
            counter=counter+1
    if(counter!=3):
        return 0
    st=set()
    for i in range(0,256):
        st.add(str(i))
    counter=0
    temp=""
    for i in range(0,len(s)):
        if(s[i]!='.'):
            temp=temp+s[i]
        else:
            if(temp in st):
                counter=counter+1
            temp=""
    if(temp in st):
        counter=counter+1
    if(counter==4):
        return 1
    else:
        return 0
    
if __name__ == '__main__':
    s="67.53.56.29"
    print(Method_1(s))
    print(Method_2(s))

