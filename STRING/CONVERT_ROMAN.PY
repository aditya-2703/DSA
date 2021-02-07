# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# Input:
# n = 3
# Output: III

def Method_1(n):#locha
    nlist=['M','D','C','L','X','V','I']
    dictionary={0:1000,
                1:500,
                2:100,
                3:50,
                4:10,
                5:5,
                6:1}
    string=""
    for i in range(7):
        if n==dictionary[i]:
            return nlist[i]

    temp=n
    i=0
    while temp!=0 or i<7:
        if dictionary[i]<=temp:
            temp-=dictionary[i]
            string+=nlist[i]
        else:
            i+=1
    return string



if __name__ == '__main__':
    print(Method_1(916))
    