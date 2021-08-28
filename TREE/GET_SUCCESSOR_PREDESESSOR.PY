# INPUT  - Tree1() , node=30
# OUTPUT - 60,70
# Explanation - print successor and predesessor
# -----------------------------------------------------------------------------------
# this is just for understanding you don't have to print 
#                  10                   
#         /         |         \         
#       20        [30]        40        
#     /  \       / | \         \        
#   50   [60] [70] 80  90       100      
#                / \                    
#              110 120                  
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

# Here what we do is we know the recursion that it runs and returns something and value changes after each steps
# so for saving value what we do is make states
# if state ==0 we save the predecessor and after finding data increase state to 1 so will get last node as predecessor
# if state ==1 then will find predecessor so there is one thing one is successor so will save successor that's it 
# notice will not perform any operation after will match data with node because we don't want that we only want node after that and before that 
def get_successor_predecessor(tree,node):
    global successor,predecessor,state

    if state==0:
        if tree.data == node:
            state = 1
        else:
            predecessor = tree
    elif state==1:
        successor = tree
        state = 2
    for child in tree.childrens:
        get_successor_predecessor(child,node)    


if __name__ == '__main__':
    arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,200,-1,-1]
    successor = 0
    predecessor = 0 
    state = 0
    tree = build_tree(arr)
    lsit = get_successor_predecessor(tree,30)
    print("pre",predecessor.data,"suc",successor.data)
    