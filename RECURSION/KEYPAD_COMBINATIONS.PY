# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = ""
# Output: []
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]


def keypad(code,maping,result):
    if len(code)==0:
        return [" "]
    
    first_char  = int(code[0])
    rest_str = code[1:]
    result = keypad(rest_str,maping,result)    
    new_list = []
    for i in maping[first_char]:
        for j in result:
            new_list.append(i+j)
    return new_list


if __name__ == '__main__':
    mapping = {1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl",
             6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    key =  "23"
    result=keypad(key,mapping,"")
    print(result)