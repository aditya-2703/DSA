# Input : abc
# Output : a, b, c, ab, bc, ac, abc
# Input : aaa
# Output : a, aa, aaa
# explanation:  
#         i=0                 abc       
#                          /      \   
#         i=1             a       " "   
#                       /  \      /  \ 
#         i=2         ab    a    b   " "
#                    / \   / \  / \  / \ 
#         i=3      abc ab ac a bc b c  " "

# METHOD 1 -- TAKES O(2**N) TIME AND O(1)(EXCEPT RECURSION STACK FRAME) SPACE COMPLEXITY 
def Method_1(string,i,curr_str,result_list):
    if i==len(string):
        result_list.append(curr_str)
        return result_list
    Method_1(string,i+1,curr_str+string[i],result_list)
    Method_1(string,i+1,curr_str,result_list)
if __name__ == '__main__':
    string="abc"
    result_list=[]
    Method_1(string,0,"",result_list)
    print(result_list)
    