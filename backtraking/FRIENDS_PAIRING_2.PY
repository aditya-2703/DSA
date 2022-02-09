# Friends Pairing - 2

# 1. You are given an integer n, which represents n friends numbered from 1 to n.
# 2. Each one can remain single or can pair up with some other friend.
# 3. You have to print all the configurations in which friends can remain single or can be paired up.

# Note -> Check out the question video and write the recursive code as it is intended without changing signature. The judge can't force you but intends you to teach a concept.

# Sample Input
# 3

# Sample Output
# 1.(1) (2) (3) 
# 2.(1) (2,3) 
# 3.(1,2) (3) 
# 4.(1,3) (2) 

counter = 0
def get_solution(i,n,ans,visited): 
    # counter for indexing
    global counter
    if i>n:
        # base case when i reach to n and print the ans
        counter+=1
        print(f"{counter}. {ans}")
        return 
    # if number visited then leave the number and go for next 
    if visited[i]:
        get_solution(i+1,n,ans,visited)
    else:
        # mark the number
        visited[i] = True
        # call for single i
        get_solution(i+1,n,ans+f"({i}) ",visited)

        for other_digit in range(i+1,n+1):
            if visited[other_digit]==False:
                # mark for edge digit
                visited[other_digit] = True
                # call for i with other digit 
                get_solution(i+1,n,ans+f"({i},{other_digit}) ",visited)    
                # unmark for edge digit
                visited[other_digit] = False
        # unmark the number
        visited[i] = False
    


if __name__ == '__main__':
    n = 3
    get_solution(1,n,"",[False]*(n+1))
    