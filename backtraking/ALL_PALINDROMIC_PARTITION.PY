# All Palindromic Partitions

# https://leetcode.com/problems/palindrome-partitioning/
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
 
# Sample Input
# pep
# Sample Output
# (p) (e) (p) 
# (pep) 



# check is string palindrome
def is_valid_palindrome(ans):
    if len(ans)>0:
        if ans != ans[::-1]:
            return False
        else:
            return True
    else:
        return False

def get_palindrome_substring(string,ans):
    # if string is empty then return or print ans
    if not string:
        print(ans)
        return 
    
    # loop for checking palindrome string
    for i in range(len(string)):
        # prefix
        char = string[:i+1]
        # rest
        rest = string[i+1:]
        # check is prefix palindrome
        if is_valid_palindrome(char):
            # if is palindrome make a call
            get_palindrome_substring(rest,ans+f" ({char})")


if __name__ == '__main__':
    string = "ababa"
    get_palindrome_substring(string,"")