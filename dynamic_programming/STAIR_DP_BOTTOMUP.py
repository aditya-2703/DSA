def stair(cd):
    f=[0]*cd
    f[0]=1
    f[1]=1
    for i in range(2,cd):
        f[i]=f[i-2]+f[i-1]
    return f[cd-1]

if __name__ == '__main__':
    print(stair(9+1))
    
    