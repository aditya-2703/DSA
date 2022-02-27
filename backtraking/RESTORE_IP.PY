# Restore IP Addresses

# https://nados.io/question/restore-ip-addresses
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# Sample Input

# 101023

# Sample Output
# [1.0.10.23, 1.0.102.3, 10.1.0.23, 10.10.2.3, 101.0.2.3]

# return valid ip for string len 2 and 3
def is_valid(string):
    # if leading 0 false
    if string[0]=="0":
        return False
    # if value <= 255 true else false
    return int(string)<=255

def get_solution(i,string,ans,partition):
    # if we explore all char
    if i==len(string):
        # if we found total 4 partition _ . _ . _ . _ 
        if partition==4:
            # return ans
            return [ans[:-1]]
        return []
    result = []
    # call for taking 1st string
    one = get_solution(i+1,string,ans+string[i]+".",partition+1)
    two = []
    three= []
    # call for taking 1st two sub string
    if i+2<=len(string) and is_valid(string[i:i+2]):
        two = get_solution(i+2,string,ans+string[i:i+2]+".",partition+1)
    # call for taking 1st three sub string
    if i+3<=len(string) and is_valid(string[i:i+3]):
        three = get_solution(i+3,string,ans+string[i:i+3]+".",partition+1)
    # take all non repeated value fill in arr
    for i in one+two+three:
        if i not in result:
            result.append(i)
    # return arr
    return result
if __name__ == '__main__':
    string = "101023"
    ans = get_solution(0,string,"",0)
    print(ans)