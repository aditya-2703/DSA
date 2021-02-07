# Input:
# str1 = aab
# str2 = xxy
# Output: 1
# Explanation: There are two different
# charactersin aab and xxy, i.e a and b
# with frequency 2and 1 respectively.

# METHOD 1 -- TAKES O(N+M) TIME AND O(N+M) SPACE COMPLEXITY
def Method_1(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        dict1=dict()
        dict2=dict()
        for i in range(len(str1)):
            dict1[str1[i]]=0
            dict2[str2[i]]=0
        for i in range(len(str1)):
            dict1[str1[i]]+=1
            dict2[str2[i]]+=1
        for i in range(len(str1)):
            if dict1[str1[i]]==dict2[str2[i]]:
                continue
            else:
                return False
        return True 

if __name__ == '__main__':
    s1="aab"
    s2="xxy"
    print(Method_1(s1,s2))
    