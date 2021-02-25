


# HERE WILL USE CONCEPT OF HISTOGRAM IT WILL FIND THE MAX RACTENGLE 
# THE HISTOGRAM CONCEPT IS :[2,3,4,5,2,1] so this is array and here histogram is as follows
#   2    3    4     5    2   1
#                 ---- 
#            ----l    l
#       ----l    l    l
#  ----l    l    l    l----
# l 2 l  2  l 2  l  2 l 2 l----                    
# l_._l_..__l__._l__._l_._l____l_
# from all combinations
# 2*5=10
# 3*3=0
# 4*2=8
# 5*1=5
# 2*5=10
# 1*6=6
# so here max ractangle is 2*5=10
# will use same algo here


def get_width(arr):
    stack=list()
    max_area=0
    index=0
    
    while index<len(arr):

        # if stack is not empty or the curr element is greater than previos then store it in stack
        if (not stack) or (arr[stack[-1]]<=arr[index]):
            stack.append(index)
            index+=1        
        else:
            # if will get curr element lower than previos will pop element and calculater area
            # by doing that element * (if stack is not empty then (index-that ele-1))else(index) 
            top_ele=stack.pop()
            area=( arr[top_ele] * ((index-stack[-1]-1)if stack else index))

            # will substitute in max area if that area is max

            max_area=max(max_area,area)
    # now there will be some bar is present in stack so for that 
    while stack:
        top_ele=stack.pop()
        
        # calculate area
        area=arr[top_ele]*((index-stack[-1]-1)if stack else index)  

        max_area=max(max_area,area)
    return max_area

        
if __name__ == '__main__':
    #  1 1 1 1 1 1 1 0
    
    histogram=[2,3,4,5,6,7,8,1,1,2,2]
    
    # here we make this matrix in terms of histogram
    # now will caclulate the area of histogram
    # area=width*height
    # we have our height 
    # for width will calculate so for that
    print(get_width(histogram))