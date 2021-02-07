# TAKES O(N*M) TIME AND O(1) SPACE COMPLEXITY
def string_matching(text,pattern):
    n=len(text)
    m=len(pattern)
    for i in range(n-m+1):
        j=0
        while j<m:
            if text[i+j]!=pattern[j]:
                break
            j+=1
        if j==m:
            print(f"MATCHING INDEX AT {i}")
if __name__ == '__main__':
    text="abcabcabcasityachauhanstiong"
    pattern="chauhan"
    string_matching(text,pattern)