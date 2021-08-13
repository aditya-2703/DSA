# INPUT  - TREE([10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1])
# OUTPUT - 10->20->50->60->30->70->80->110->120->90->40->100
# explanation - 
# -----------------------------------------------------------------------------------
# input
#                                      10
#                             /         |         \ 
#                           20         30         40 
#                         /  \       / | \         \         
#                       50    60   70 80  90       100 
#                                    / \
#                                  110 120
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# output
#                             10
#                             |                   
#                             20                   
#                             |       
#                             50        
#                             |       
#                             60       
#                             |
#                             30 
#                             | 
#                             70
#                             |
#                             80   
#                             |
#                             110
#                             |
#                             120
#                             |
#                             40   
#                             |
#                             100 
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
            print(patterns + self.data)
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
    root=0
    for i in arr:
        if i==-1:
            stack.pop()
        else:
            i=str(i)
            if stack:
                new_node = TreeNode(i)
                parent_node = stack[-1]
                parent_node.add_child(new_node)
                stack.append(new_node)
            else:
                root = TreeNode(i)
                stack.append(root)
    return root
# this function will return tail of given tree
def getTail(tree):
    if tree:
        while tree.childrens:
            tree = tree.childrens[0]
    return tree
# Method - 1 takes O(n**2) time and O(1) space complexity
def Method_1(tree):
    for child in tree.childrens:
        Method_1(child)
    while len(tree.childrens)>1:
        last_node = tree.childrens.pop()
        second_last_node = tree.childrens[-1]
        tail = getTail(second_last_node)
        tail.add_child(last_node)

# Method - 2 takes O(n) time and O(1) space complexity
def Method_2(tree):
    if tree.childrens :
        Tail_node = Method_2(tree.childrens[-1])
        while len(tree.childrens)>1:
            last_node = tree.childrens.pop()
            second_last_node = tree.childrens[-1] 
            second_last_node_tail =  Method_2(second_last_node)
            second_last_node_tail.add_child(last_node) 
        return Tail_node
    return tree
        
if __name__ == '__main__':
    arr = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    tree = build_tree(arr)
    tree.print_tree()
    print()
    Method_1(tree)
    tree.print_tree()
    print()
    Method_2(tree)
    tree.print_tree()
