# Crossword Puzzle
# A  Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.

# The following shows an example crossword from the input  grid and the list of words to fit, :

# Input 	   		Output

# ++++++++++ 		++++++++++
# +------+++ 		+POLAND+++
# +++-++++++ 		+++H++++++
# +++-++++++ 		+++A++++++
# +++-----++ 		+++SPAIN++
# +++-++-+++ 		+++A++N+++
# ++++++-+++ 		++++++D+++
# ++++++-+++ 		++++++I+++
# ++++++-+++ 		++++++A+++
# ++++++++++ 		++++++++++
# POLAND;LHASA;SPAIN;INDIA




def is_placed_hori(crossword,word,row,col):
    if col-1>0 and crossword[row][col-1]!="+":
        return False
    elif col+len(word)<len(crossword[0]) and crossword[row][col+len(word)]!="+":
        return False

    for char in range(len(word)):
        if col+char>=len(crossword[0]):
            return False
        if (word[char] == crossword[row][col+char]) or (crossword[row][col+char]=="-"):
            continue
        else:
            return False
    return True
def place_hori(crossword,word,i,j):
    visited = [False]*len(word)
    for col in range(len(word)):
        if crossword[i][col+j]=="-":
            char = word[col]
            crossword[i][col+j] = char
            visited[col] = True
    return visited
def unplace_hori(crossword,row,col,visited):
    for j in range(len(visited)):
        if visited[j]==True:
            crossword[row][col+j] = "-"
    
def is_placed_verti(crossword,word,row,col):
    if row-1>0 and crossword[row-1][col]!="+":
        return False
    elif row+len(word)<len(crossword) and crossword[row+len(word)][col]!="+":
        return False

    for char in range(len(word)):
        if row+char>=len(crossword):
            return False
        if (word[char] == crossword[row+char][col]) or (crossword[row+char][col]=="-"):
            continue
        else:
            return False
    return True
def place_verti(crossword,word,i,j):
    visited = [False]*len(word)
    for row in range(len(word)):
        if crossword[i+row][j]=="-":
            char = word[row]
            crossword[row+i][j] = char
            visited[row] = True
    return visited
def unplace_verti(crossword,i,col,visited):
    for row in range(len(visited)):
        if visited[row]==True:
            crossword[row+i][col] = "-"
 

def crosswordPuzzle(crossword,words,index):
    if index==len(words):
        for i in crossword:
            for j in i:
                print(j,end="")
            print()
        return 

    word = words[index]
    for i in range(len(crossword)):
        for j in range(len(crossword[0])):
            if crossword[i][j]=="-" or crossword[i][j]==word[0]:
                if is_placed_hori(crossword,word,i,j):
                    visited = place_hori(crossword,word,i,j)
                    crosswordPuzzle(crossword,words,index+1)
                    unplace_hori(crossword,i,j,visited)
                elif is_placed_verti(crossword,word,i,j):
                    visited = place_verti(crossword,word,i,j)
                    crosswordPuzzle(crossword,words,index+1)
                    unplace_verti(crossword,i,j,visited)




if __name__ == '__main__':
    crossword = [list("+-++++++++"),
                list("+-++++++++"),
                list("+-++++++++"),
                list("+-----++++"),
                list("+-+++-++++"),
                list("+-+++-++++"),
                list("+++++-++++"),
                list("++------++"),
                list("+++++-++++"),
                list("+++++-++++")]
    words = ["LONDON","DELHI" ,"ICELAND" ,"ANKARA"] 
    crosswordPuzzle(crossword, words, 0)
    
    