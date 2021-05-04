# Input:
# S = geeksforgeeks
# Output: 7
# Explanation: The longest substring
# without repeated characters is "ksforge".


def repet(string):    
    i=0
    j=0
    maxi=0
    hashset=[]
    newlist=[]
    while j<len(string):
        if string[j] not in hashset:
            hashset.append(string[j])
            j+=1
            maxi=max(len(hashset),maxi)
        else:
            hashset.remove(string[i])
            i+=1
    print(maxi)
    print(max(newlist))
if __name__ == '__main__':
    string="geeksforgeeks"
    repet(string)
    