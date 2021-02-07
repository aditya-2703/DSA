def total_ways(string,k):
    result=0
    if k==0 or k==1:
        return 1
    if string[k-1]>='0':
        result+=total_ways(string,k-1)
    if 10<=int(string[k-2:k])<=26:
            result+=total_ways(string,k-2)
    return result


if __name__ == '__main__':
    print(total_ways("1234",len("1234")))
    