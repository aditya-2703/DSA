# Remove Invalid Parentheses

# https://leetcode.com/problems/remove-invalid-parentheses/
# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
# Return all the possible results. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: "(())()"
#         "()()()"

# this function is able to give you minimum invalid paranthesis 
# by canceling pair of para () it store remaining invalid paranthesis
def get_min_invalid_para_count(string):
    stack = []
    for i in string:
        if i=="(":
            stack.append(i)
        else:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(i)
    return len(stack)


def get_solution(min_para_count,string,ans):
    # when you remove all minimum number of invalid paranthesis
    if min_para_count==0:
        curr_min_count = get_min_invalid_para_count(string)
        # check is this string valid and not includ in ans previously
        if curr_min_count == 0:
            if string not in ans:
                print(string)
                ans.add(string)
        return 
    # for all string remove that char 
    for i in range(len(string)):
        char = string[i]
        left = string[:i]
        right = string[i+1:]
        rest = left+right
        get_solution(min_para_count-1,rest,ans)

if __name__ == '__main__':
    string = "()())()"
    min_para_count = get_min_invalid_para_count(string)
    get_solution(min_para_count,string,set())    