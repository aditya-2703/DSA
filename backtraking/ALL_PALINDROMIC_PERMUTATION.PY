# Print all the palindromic permutations of given string in alphabetic order

# Given a string str of size n. The problem is to print all the palindromic permutations of str in alphabetic order if possible else print “-1”.
# Input : str = "aabb"
# Output :
# abba
# baab

# Input : malayalam
# Output :
# aalmymlaa
# aamlylmaa
# alamymala
# almayamla
# amalylama
# amlayalma
# laamymaal
# lamayamal
# lmaayaaml
# maalylaam
# malayalam
# mlaayaalm



#  main method for work
def get_all_permutation(ii,n,hashmap,odd_char,ans):
    # if index goes beyong length base case : print ans which is half of string so 
    # palindrome is nothing but half string + half reverse string
    # if there is some odd length then half string + single char + half reverse string
    if ii >= n:
        # if there is odd character 
        if odd_char:
            print(f"{ans}{odd_char}{ans[::-1]}")
        # if there is no odd character 
        else:
            print(f"{ans}{ans[::-1]}")
        return 
    # iterate through all keys in hashmap  
    for i in hashmap:
        # take freq of character  
        freq = hashmap[i]
        # if freq greater than 0
        if freq>0:
            # mark that character by reduce the freq in hashmap
            hashmap[i]-=1
            get_all_permutation(ii+1,n,hashmap,odd_char,ans+i)
            # unmark that character by increasing the freq in hashmap : backtrack
            hashmap[i]+=1


if __name__ == '__main__':
    string = "malayalam"
    hashmap = {}
    length = 0
    # building hashmap with unique character - int (freq)
    for i in string:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    odd_char = ""
    odd_char_freq = 0
    for i in hashmap:
        if hashmap[i]%2!=0:
            odd_char = i
            odd_char_freq +=1
        hashmap[i] = hashmap[i]//2
        length += hashmap[i]
    # if there is more than one odd character then ans does not exist think by yourself
    if odd_char_freq>1:
        print(f"not possible")
    # if there is only one or not odd character then 
    else:
        get_all_permutation(0,length,hashmap,odd_char,"")
    