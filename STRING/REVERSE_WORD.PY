# Input:
# S = i like this program very much
# Output: much very program this like i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much very program this like i

def Method_1(s):
    string_list = s.split(" ")
    string_list.reverse()
    return " ".join(string_list)
if __name__ == '__main__':
    s="i like this program very much"
    print(Method_1(s))
    
