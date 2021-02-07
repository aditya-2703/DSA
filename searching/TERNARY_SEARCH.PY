# mid1 = l + (r-l)/3
# mid2 = r – (r-l)/3
# HERE THERE IS TWO MID ELEMENT 
# TAKES LOG N BASE 3 WHICH IS LESS TIME TAKEN COMPARE TO BINARY SEARCH
def Ternary_search(arr,element):
    l=0
    r=len(arr)-1
    while l<r:
        mid1=l+(r-l)//3
        mid2=r-(r-l)//3
        if element==arr[mid1] or element==arr[mid2]:
            return True
        elif element<arr[mid1]:
            r=mid1-1
        elif element>arr[mid2]:
            l=mid2+1
        elif element>arr[mid1] and element<[mid2]:
            l=mid1+1
            r=mid2-1
    return False


if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9,10]
    if Ternary_search(arr,11):
        print('ELEMENT EXIST IN THIS ARRAY')
    else:
        print('ELEMENT NOT EXISTS IN THIS ARRAY')
    