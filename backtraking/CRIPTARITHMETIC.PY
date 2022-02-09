# Solving Cryptarithmetic Puzzles 

# Newspapers and magazines often have crypt-arithmetic puzzles of the form:

#   SEND
# + MORE
# --------
#  MONEY
# -------- 

# Sample Input

# team
# pep
# toppr

# Sample Output
# a-3 e-9 m-4 o-1 p-2 r-6 t-0 
# a-3 e-9 m-5 o-1 p-2 r-7 t-0 
# a-3 e-9 m-6 o-1 p-2 r-8 t-0 
# a-4 e-9 m-2 o-1 p-3 r-5 t-0 
# a-4 e-9 m-5 o-1 p-3 r-8 t-0 
# a-5 e-9 m-2 o-1 p-4 r-6 t-0 
# a-5 e-9 m-3 o-1 p-4 r-7 t-0 
# a-6 e-9 m-2 o-1 p-5 r-7 t-0 
# a-6 e-9 m-3 o-1 p-5 r-8 t-0 
# a-7 e-9 m-2 o-1 p-6 r-8 t-0 

# check is sum of a and b is equal to c
def is_valid_sum(a,b,c,digit_arr):
    a_sum = ""
    b_sum = ""
    c_sum = ""
    for i in a:
        a_sum+=str(digit_arr[i])
    for j in b:
        b_sum+=str(digit_arr[j])
    for k in c:
        c_sum+=str(digit_arr[k])
    # print(f"for a {a} sum is {a_sum}")
    # print(f"for b {b} sum is {b_sum}")
    # print(f"for c {c} sum is {c_sum}")
    curr_output = int(a_sum) + int(b_sum)
    goal_output = int(c_sum)
    # print(f"curr_sum = {curr_output} goal = {goal_output} result {curr_output == goal_output}")
    # print()
    if curr_output - goal_output==0:
        return True

    return False

# main method to solve this puzzle 
def get_psbl_combi(a,b,c,visited,ans,digit_arr,total_words,index):
    # base case when all numbers assign to some char
    if index == len(total_words):
        # find is sum valid or not
        if is_valid_sum(a,b,c,digit_arr):
            # sum is valid so print ans
            print(ans)
        return 
    
    # take word
    word = total_words[index]
    # for that word explore all numbers
    for i in range(10):
        # if number is not visited
        if visited[i] == False:
            # visit the word
            visited[i] = True
            # take the word as dictionary with map of the digit
            digit_arr[word] = i
            # make call for other char
            get_psbl_combi(a,b,c,visited,ans+word+"-"+str(i)+" ",digit_arr,total_words,index+1)
            # unmark the word for backtracking
            visited[i] = False
            # remove word from dictionary
            digit_arr.pop(word)

# sort the array of words
def get_sorted_total_words(arr):
    ans = []
    for i in range(26):
        if chr(i+97) in arr:
            ans.append(chr(i+97))
    return ans

if __name__ == '__main__':
    a = "send"
    b = "more"
    c = "money"
    # unique word list 
    total_words = list(set(a+b+c))
    # list in sorted order becase qn ask to print in increasing char order 
    total_words  = get_sorted_total_words(total_words)
    # make visited array for unique digit
    visited = [False]*10
    get_psbl_combi(a,b,c,visited,"",{},total_words,0)