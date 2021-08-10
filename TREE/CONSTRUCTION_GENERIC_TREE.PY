# OUTPUT - make a tree construction like this
# electronics
# |__ tv
#     |__ samsung
#     |__ oneplus
# |__ mobile
#     |__ iphone
#     |__ samsung
#          |__s9
#          |__a7
#     |__ vivo
# |__ laptop
#     |__ macbook


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
            space = self.get_level()*4
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
# Here this is only for understanding tree property so that this function add child and parent and build tree
def get_tree():
    
    root = TreeNode("Electronics")
    tv = TreeNode("Tv")
    phone = TreeNode("Mobile")
    laptop = TreeNode("Laptop")
    
    root.add_child(tv)
    root.add_child(phone)
    root.add_child(laptop)
    
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Oneplus"))
    
    samsung = TreeNode("Samsung")
    phone.add_child(TreeNode("Iphone"))
    phone.add_child(samsung)
    phone.add_child(TreeNode("Vivo"))
    samsung.add_child(TreeNode("s9"))
    samsung.add_child(TreeNode("a7"))

    laptop.add_child(TreeNode("Macbook"))

    
    return root
     
if __name__ == '__main__':
    tree = get_tree()
    tree.print_tree()
    print(tree.total_nodes(0))

# -----------------------------------------------------------------------------------
# this is just for understanding you don't have to print 
#                                    electronics 
#                   /                   |            \ 
#                 tv                 mobile          laptop
#               /  \                  / | \             \ 
#          samsung  oneplus  iphone samsung vivo       macbook
#                                      / \  
#                                     s9 a7
# -----------------------------------------------------------------------------------
