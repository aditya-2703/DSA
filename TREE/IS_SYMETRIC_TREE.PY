# INPUT  - Tree1 , Tree2
# OUTPUT - True
# Explanation - here input given as two tree and if they are symetric tree then returns true else false
# symetric is when you draw line in middle of anything it's left part and right parts looks exectly same
# -----------------------------------------------------------------------------------
# this is just for understanding you don't have to print 
#                  10                   |                   a                  
#         /         |         \         |           /       |      \         
#       20         30         40        |         k        e        b        
#     /  \       / | \       / \        |       /        / | \    /  \          
#   50    60   70 80  90  200  100      |     l        j  g  f    c  d
#                / \                    |                / \                    
#              110 120                  |               h   i                    
#              True                     |               False
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
def is_symetric(tree1,tree2):
    size1 = len(tree1.childrens)
    size2 = len(tree2.childrens)
    if size1!=size2:
        return False
    for child in range(size1):
        if not is_symetric(tree1.childrens[size1-child-1],tree2.childrens[child]):
            return False
    return True
if __name__ == '__main__':
    arr1 = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,200,-1,-1]
    tree1 = build_tree(arr1)
    tree1.print_tree()
    print(is_symetric(tree1,tree1))
    