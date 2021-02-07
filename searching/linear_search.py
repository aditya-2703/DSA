def search_linear(element,array):
    flag=False
    for i in array:
        if i==element:
            flag=True
    return flag

if __name__ == "__main__":
    array=[43,4,3214,4,1,4,32,4,1,4,34,1,4,43,4]
    print(f"your list {array}")
    element=int(input())
    search_linear(element,array)
    if search_linear(element,array):
        print("element found : : successfully")
    else:    
        print("element does not exist in this array")