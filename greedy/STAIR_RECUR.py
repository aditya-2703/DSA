def func(stairs):
    if stairs==0:
        return 1
    if stairs<0:
        return 0
    else:
        return func(stairs-1)+func(stairs-2)

if __name__ == '__main__':
    stairs=6
    print(func(stairs))
    