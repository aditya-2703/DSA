# INPUT
# ABCDEFG
# GFEABCD
# OUTPUT
# TRUE

# METHOD 1 -- O(N*LOGN) TIME AND O(1) SPACE COMPLEXITY
def Method_1(s1,s2):
    s1="".join(sorted(s1))
    s2="".join(sorted(s2))
    if s1==s2:
        return True
    else:
        return False

# METHOD 2 -- O(N) TIME AND O(N+N) SPACE COMPLEXITY
def Method_2(s1,s2):
    hash_table_s1=dict()
    hash_table_s2=dict()
    for i in range(len(s1)):
        hash_table_s1[s1[i]]=0
    for i in range(len(s2)):
        hash_table_s2[s2[i]]=0
    for i in range(len(s1)):
        hash_table_s1[s1[i]]+=1
    for i in range(len(s2)):
        hash_table_s2[s2[i]]+=1
    for i in s1:
        if hash_table_s1[i]==hash_table_s2[i]:
            continue
        else:
            return False
    return True
    






if __name__ == '__main__':
    s1="ABCDEFGA"
    s2="GFEABCDA"
    print(Method_2(s1,s2))

    