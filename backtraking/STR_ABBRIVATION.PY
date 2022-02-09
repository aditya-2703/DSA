# Alphanumeric Abbreviations of a String


# https://www.geeksforgeeks.org/alphanumeric-abbreviations-of-a-string
# Given a string of characters of length less than 10. We need to print all the alpha-numeric abbreviation of the string.
# The alpha-numeric abbreviation is in the form of characters mixed with the digits which is equal to the number of skipped characters of a selected substring. So, whenever a substring of characters is skipped, you have to replace it with the digit denoting the number of characters in the substring. There may be any number of skipped substrings of a string. No two substrings should be adjacent to each other. Hence, no two digits are adjacent in the result. For a clearer idea, see the example.

# Examples:
# Input : ANKS 
# Output :
# ANKS (nothing is replaced)
# ANK1 (S is replaced) 
# AN1S (K is replaced)
# AN2  (KS is replaced)
# A1KS (N is replaced)
# A1K1 (N and S are replaced)
# A2S (NK is replaced)
# A3 (NKS is replaced)
# 1NKS (A is replaced)
# 1NK1 (A and S are replaced)
# 1N1S (A and N is replaced)
# 1N2 (A and KS are replaced)
# 2KS (AN is replaced)
# 2K1 (AN and S is replaced)
# 3S (ANK is replaced)
# 4 (ANKS is replaced)



# 2*n time complexity
# here we need the abbrivation 
# so will do is take the char else increment count 
def get_abbrivation(string,count,temp):
    if not string:
        if count>0:
            print(f"{temp}{count}")
        else:
            print(temp)
        return 

    first =string[0]
    rest = string[1:]
    if count>0:
        get_abbrivation(rest,0,temp+str(count)+first)
    else:
        get_abbrivation(rest,0,temp+first)
    get_abbrivation(rest,count+1,temp)



if __name__ == '__main__':
    string = "pep"
    get_abbrivation(string,0,"")
    