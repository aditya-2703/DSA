def HASH(data):
    k=0
    for i in data:
        k+=ord(i)
    return k%100
if __name__ == '__main__':
    arr=[]
    arr.insert(HASH("ADITYA"),"ADITYA")
    arr.insert(HASH("CHAUHAN"),"CHAUHAN")
    print(HASH("ADITYA"),HASH("CHAUHAN"),*arr)
    