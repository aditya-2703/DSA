# INPUT  - Tree1()
# OUTPUT - 5
# Explanation - return diameter which is longest distance between any two nodes
# -----------------------------------------------------------------------------------
# this is just for understanding you don't have to print 
#                  10                                     
#        //         ||         \        
#       20         30         40        
#     //  \       / || \         \      
#  [50]    60   70 80  90       100      
#                / \\                   
#              110 [120]                  
#                  
#                   5
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
# Here what we do is we find maximum depth of tree and second max depth of tree and add  2 to it 
# because that's how we find diameter just think about it visually 
def get_diameter(tree):
    global diameter     
    max_child = -1
    second_max_child = -1
    for child in tree.childrens:
        value = get_diameter(child)
        if value>max_child:
            second_max_child = max_child
            max_child = value
        elif value>second_max_child:
            second_max_child=value

    diameter = max(max_child+second_max_child+2,diameter)
    max_child +=1
    return max_child
if __name__ == '__main__':
    arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    # arr=['A','B','K',-1,'J','N',-1,'M',-1,-1,-1,'F',-1,'D','G',-1,-1,'E','C',-1,'H',-1,'I','L']
    # arr = [2,3,-1,1]
    tree = build_tree(arr)
    # tree.print_tree()
    diameter=0
    result = get_diameter(tree)
    print(diameter)