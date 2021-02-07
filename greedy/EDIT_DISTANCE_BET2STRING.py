def func(string1_from, string2_to,i,j):
    if i==0:
        return j
    if j==0:
        return i
    if string1_from[i-1]==string2_to[j-1]:
        return func(string1_from,string2_to,i-1,j-1)
    
    return 1+min(func(string1_from,string2_to,i-1,j),func(string1_from,string2_to,i,j-1),func(string1_from,string2_to,i-1,j-1))
if __name__ == '__main__':
    str2="cut"
    str1="cat"
    print(func(str1,str2,len(str1),len(str2)))