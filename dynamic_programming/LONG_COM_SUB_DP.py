def optimal_longcomsub(s1,s2):
    s1=" "+s1
    s2=" "+s2
    matrix=[[0 for i in range(len(s1)+1)]for i in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[i-1]==s2[j-1]:
                matrix[i][j]=1+matrix[i-1][j-1]
            else:
                matrix[i][j]=max(matrix[i][j-1],matrix[i-1][j])

    return matrix[len(s1)-1][len(s2)-1]
if __name__ == '__main__':
    s1="aab"
    s2="azb"
    print(optimal_longcomsub(s1,s2))