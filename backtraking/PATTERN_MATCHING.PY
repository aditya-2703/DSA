# Match a pattern and String without using regular expressions

# https://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/
# Given a string, find out if string follows a given pattern or not without using any regular expressions. 
# Examples: 
# Input: 
# string - GraphTreesGraph
# pattern - aba
# Output: 
# a->Graph
# b->Trees
# Input: 
# string - GraphGraphGraph
# pattern - aaa
# Output: 
# a->Graph


def get_solution(i,para,pattern,dictionary):
    if not pattern:
        if not para:
            for key in dictionary:
                print(f"{key}->{dictionary[key]} ",end="")
        return 

    char = pattern[0]
    rest= pattern[1:]
    for ind in range(len(para)):
        prefix = para[:ind+1]
        rest_para = para[ind+1:]
        if char in dictionary:
            if dictionary[char] == prefix:
                get_solution(i+1,rest_para,rest,dictionary)
        else:
            dictionary[char] = prefix
            get_solution(i+1,rest_para,rest,dictionary)
            del dictionary[char] 


if __name__ == '__main__':
    para = "graphtreesgraph"
    pattern = "pep"
    get_solution(0,para,pattern,{})
    