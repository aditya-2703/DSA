def fibonacci(n):
    dic_fib=dict()
    # if n in dic_fib:return dic_fib[n]
    # if n<2:
    #     return n
    # # else:
    #     f=fibonacci(n-1)+fibonacci(n-2)
    #     dic_fib[n]=f
    #     print(dic_fib,dic_fib[n])
    #     return dic_fib[n]
    for i in range(1,n):
        if i in dic_fib:
            return dic_fib[i]
        if i<2:
            return n
        else:
            f=fibonacci(i-1)+fibonacci(i-2)
            dic_fib[i]=i
if __name__ == '__main__':
    print(fibonacci(5))