# RECURSION 
# BIG PROBLEM = SUBPROBLEM + SUBPROBLEM
# THREE STEPS:
#            1.FIND THE BASE CASE
#            2.FIND THE RELATION BETWEEN BIG PROBLEM AND SMALL PROBLEM 
#            3.GENERALIZE THE RELATION

# PROBLEM N=10
# OUTPUT  55=10+9+8+7+6+5+4+3+2+1

# FIRST STEP N=0 BASE CASE
# RELATION N=N+(N-1)  
# GENERALIZE RELATION 

# METHOD -1 TAKES O(N) TIME AND O(N)(recursion uses stack frames)AUXILIARY SPACE COMPLEXITY
def Method_1(n):
    if n==0:
        return 0
    return n+Method_1(n-1)

if __name__ == "__main__":
    n=10
    print(Method_1(n))


#  we also solve this problem in o(1) time complexity but this is about to understand recursion so.