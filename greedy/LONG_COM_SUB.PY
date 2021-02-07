def longest_common_sub(s1,s2,n,m):
    if n==0 or m == 0:
        return 0
    elif s1[n-1]==s2[m-1]:
        return 1+longest_common_sub(s1,s2,n-1,m-1)
    else:
        return max(longest_common_sub(s1,s2,n,m-1),longest_common_sub(s1,s2,n-1,m))

if __name__ == '__main__':
    s1="abcxyzgxa"
    s2="kmnxymnoa"
    print(longest_common_sub(s1,s2,len(s1),len(s2)))
    