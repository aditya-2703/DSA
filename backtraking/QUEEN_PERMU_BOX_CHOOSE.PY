# Queens Permutations - 2d As 2d - Queen Chooses

# 1. You are given a number n, representing the size of a n * n chess board.
# 2. You are required to calculate and print the permutations in which n queens can be placed on the 
#      n * n chess-board. 

# Note -> Use the code snippet and follow the algorithm discussed in question video. The judge can't 
#                force you but the intention is to teach a concept. Play in spirit of the question.

# Sample Input

# 2

# Sample Output
# q1	q2	
# -	-	

# q1	-	
# q2	-	

# q1	-	
# -	q2	

# q2	q1	
# -	-	

# -	q1	
# q2	-	

# -	q1	
# -	q2	

# q2	-	
# q1	-	

# -	q2	
# q1	-	

# -	-	
# q1	q2	

# q2	-	
# -	q1	

# -	q2	
# -	q1	

# -	-	
# q2	q1	



def get_solution(chess,box,q_count):
    if q_count==box:
        if q_count == box:
            for i in chess:
                for j in i:
                    print(j+"\t",end="")
                print()
            print()
        return 

    for i in range(len(chess)):
        for j in range(len(chess[0])):
            if chess[i][j]=="-":
                chess[i][j] = "q" + str(q_count+1)
                get_solution(chess,box,q_count+1)
                chess[i][j] = "-"

if __name__ == '__main__':
    box = 2
    chess = [["-" for i in range(box)]for i in range(box)]
    get_solution(chess,box,0)
    