# INPUT  - Tree1 k=4
# OUTPUT - 90
# Explanation - finding largest kth element like for k=1,element = 120 for 2 -> 110 like that
# -----------------------------------------------------------------------------------
# this is just for understanding you don't have to print 
#                  10                   |                  10
#         /         |         \         |           /       |      \         
#       20         30         40        |        20        30       40        
#     /  \       / | \         \        |       /  \      / | \      \          
#   50    60   70 80  90       100      |     50   60   70 80 [90]    100      
#                / \                    |                / \                    
#              110 [120]                |              110 120                
#               k=1                                     k=4
# -----------------------------------------------------------------------------------


# This is node class which have data children and parent as instance
class TreeNode:
    def __init__(self,data=None):
        self.data  = data
        self.childrens = []
        self.parent = None
    # here in this function will add child 
    def add_child(self,child):
        # make me parent of my child
        child.parent = self
        # add my child 
        self.childrens.append(child)
    def get_level(self):
        # if there is not parent return 0
        if not self.parent:
            return 0
        # add 1 to it so at last will get our ans
        return 1+self.parent.get_level()
    def print_tree(self):
        if self:
            # here this is only for decoration
            space = self.get_level()*2
            if self.parent:
                patterns = space*" " + "|_"
            else:
            # if there is root then it does not have any parent so there is no need to add space and other styling
                patterns = ""
            print(patterns + str(self.data))
            for children in self.childrens:
                children.print_tree()
    # for finding total nodes present in tree 
    def total_nodes(self,sum_node):
        if not self.childrens:
            return sum_node
        else:
            for children in self.childrens:
                sum_node = 1+children.total_nodes(sum_node)
        return sum_node
def build_tree(arr):
    
    stack = []
    root=TreeNode()
    for i in arr:
        if i==-1:
            stack.pop()
        else:
            if stack:
                new_node = TreeNode(i)
                parent_node = stack[-1]
                parent_node.add_child(new_node)
                stack.append(new_node)
            else:
                root = TreeNode(i)
                stack.append(root)
    return root
def get_floor(tree,value,floor):

    
    for child in tree.childrens:
        floor = get_floor(child,value,floor)
    if tree.data<value:
        floor = max(tree.data,floor)
    
    return floor
def get_k_largest_value(tree,k):
    floor = -999999
    factor = 99999
    for i in range(k):
        nn=get_floor(tree,factor,floor)
        factor = nn
    return nn
    
    
if __name__ == '__main__':
    arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    maxelement= -99999
    
    tree = build_tree(arr)
    # tree.print_tree()
    k=1
    result = get_k_largest_value(tree,k)
    print(result)