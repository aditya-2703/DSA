# 1178. Number of Valid Words for Each Puzzle

# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
# invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].

# Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation: 
# 1 valid word for "aboveyz" : "aaaa" 
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.



def get_set(string):
    ans = ""
    for i in string:
        if i not in ans:
            ans+=i
    return ans
def get_code(string):
    curr_str = get_set(string)
    curr_code = 0
    for char in curr_str:
        pos = 26 - (97 - ord(char))
        curr_code = curr_code | (1<<pos)
    return curr_code
def get_map_words(word):
    ans = {}
    for i in word:
        curr_str = get_set(i)
        curr_code = 0
        for char in curr_str:
            pos = 26 - (97 - ord(char))
            curr_code = curr_code | (1<<pos)
        string = "".join(curr_str)
        ans[string] = curr_code
    
    result = {}
    for i in range(0,26):
        char = chr(i+97)
        result[char] = []
    
    for i in result:
        for char in ans:
            if i in char:
                if char not in result[i]:
                    result[i] += [ans[char]]
    
    # for i in result:
    #     print(f"{i} -> {result[i]}")
    return result

def get_solution(map_words,puzzles):
    
    for puzzle in puzzles:
        count = 0
        size_of_char_bucket =  len(map_words[puzzle[0]])
        if size_of_char_bucket>0:
            for bucket in map_words[puzzle[0]]:
                code = get_code(get_set(puzzle))
                if bucket & code  == bucket:
                    count+=1
        print(count,end=" ")


if __name__ == '__main__':
    words = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    map_words = get_map_words(words)
    get_solution(map_words,puzzles)