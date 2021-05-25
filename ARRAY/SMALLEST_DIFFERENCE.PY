# Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

# Examples : 
# Input : A[] = {l, 3, 15, 11, 2}
#         B[] = {23, 127, 235, 19, 8} 
# Output : 3  
# That is, the pair (11, 8) 

# Input : A[] = {l0, 5, 40}
#         B[] = {50, 90, 80} 
# Output : 10
# That is, the pair (40, 50)

# METHOD  1 -- TAKES O(N*M) TIME AND O(1) SPACE COMPLEXITY
# WE USE TWO FOR LOOPS AND ITERATE THROUGH EVERY SINGLE PAIR
def Method_1(arrOne,arrTwo):
    minDifference=999
    pair=[]
    arrOneLen=len(arrOne)
    arrTwoLen=len(arrTwo)
    for i in range(arrOneLen):
        for j in range(arrTwoLen):
            if abs(arrOne[i]-arrTwo[j])<minDifference:
                minDifference=abs(arrOne[i]-arrTwo[j])
                pair=[arrOne[i],arrTwo[j]]
    return pair,minDifference

# METHOD 2 -- TAKES O(NLOGN + MLOGN) TIME AND O(1) SPACE COMPLEXITY
# HERE WILL USE SORTING WHAT WE DOES IS 
# i for arrOne 
# j for arrTwo
# if i<j then we calculate difference and save it then will increment i because difference will be have to smaller
# if i>j then we calculate difference and save it then will increment j because difference will be have to smaller
# if i==j then we get smallest possible pair which has smaller difference of 0
def Method_2(arrOne,arrTwo):
    # SORTING BOTH ARRAY
    arrOne.sort()
    arrTwo.sort()
    arrOneLen=len(arrOne)
    arrTwoLen=len(arrTwo)
    indexForOne=0
    indexForTwo=0
    pair=[]
    smallest_difference=999
    currentDiff=9999

    # BASE CONDITION WHEN BOTH REACHES TO END
    while indexForOne<arrOneLen and indexForTwo<arrTwoLen:
        # FIRST NUMBER OF FIRST ARRAY
        num_of_One=arrOne[indexForOne]
        # FIRST NUMBER OF SECOND ARRAY
        num_of_Two=arrTwo[indexForTwo]
        # DIFFERENCE OF BOTH NUMBERS
        currentDiff=abs(num_of_One-num_of_Two)
        
        # IF I<J 
        # WE HAVE FOUR POSIBLE CONDITIONS
        # WE INCREMENT I THE DIFFERENCE BECAME SMALLER WE CAN PICK
        # WE INCREMENT J THE DIFFERENCE BECAME LARGER
        # WE DECREMENT I THE DIFFERENCE BECAME LARGER
        # WE DECREMENT J THE DIFFERENCE BECAME SMALLER WE CAN PICK
        if num_of_One<num_of_Two:
            indexForOne+=1

        # IF I>J 
        # WE HAVE FOUR POSIBLE CONDITIONS
        # WE INCREMENT I THE DIFFERENCE BECAME LARGER 
        # WE INCREMENT J THE DIFFERENCE BECAME SMALLER WE CAN PICK
        # WE DECREMENT I THE DIFFERENCE BECAME SMALLER WE CAN PICK
        # WE DECREMENT J THE DIFFERENCE BECAME LARGER 
        
        elif num_of_One>num_of_Two:
            indexForTwo+=1

        # IF I==J
        # SO DIFFERENCE IS 0 SO WE GOT OUR MINIMUM DIFFERENCE SO WE RETURN OUR ANSWER
        else:
            pair=[num_of_One,num_of_Two]
            smallest_difference=0
            return pair,smallest_difference
        
        # HERE WE TAKE CARE OF OUR SMALLEST DIFFERENCE BY STORING IT 
        if currentDiff<smallest_difference:
            smallest_difference=currentDiff
            pair=[num_of_One,num_of_Two]
    return pair,smallest_difference

if __name__ == '__main__':  
    arrOne=[1, 3, 15, 11, 2]
    # arrOne=[10,5,40]
    arrTwo=[23, 127, 235, 19, 8]
    # arrTwo=[50,90,80]
    print(f"Pair {Method_1(arrOne,arrTwo)[0]} is having Min difference of {Method_1(arrOne,arrTwo)[1]}")
    print(f"Pair {Method_2(arrOne,arrTwo)[0]} is having Min difference of {Method_2(arrOne,arrTwo)[1]}")