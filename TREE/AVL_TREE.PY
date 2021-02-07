# WE DONE WITH OUR TREE INITIALIZATION WITH LEFT RIGHT ROOT NODES AND HEIGHT
class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.h=1
class AVL_tree:
    # FIRST WE INSERTING OUR ELEMENT IN THIS TREE LIKE NORMAL BST
    def get_height(self,root):#THESE FUNCTION RETURN HEIGHT 
        if not root:
            return 0
        return root.h
    def get_balanced(self,root):#THESE FUNCTION RETURN BALANCE
        # BY THESE FORMULA 
        # BALANCE=H(left child)-H(right child)
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)
    def ll(self,a):
        b=a.right
        t2=b.left
        # before
        #  a
        #   \
        #    b
        #   / \
        # t2   c     
        # rotation
        b.left=a
        a.right=t2
        # after
        #           b
        #         /  \
        #       a     c 
        #       \
        #        t2   
        # updatet h
        a.h=1+max(self.get_height(a.left),self.get_height(a.right))
        b.h=1+max(self.get_height(b.left),self.get_height(b.right))
        # now root becomes b return it
        return b
    def rr(self,c):
        b=c.left
        t3=b.right
        ## before
        #      c
        #     /
        #    b
        #   / \
        # a    t3     
        # rotation
        b.right=c
        c.left=t3
        # after
        #           b
        #         /  \
        #       a     c 
        #            /   
        #          t2
        # updatet h
        b.h=1+max(self.get_height(b.left),self.get_height(b.right))
        c.h=1+max(self.get_height(c.left),self.get_height(c.right))
        # return new root
        return b
    def insert(self,root,data):
        # NORMAL BST
        nn=Tree(data)
        if root is None:
            return nn
        elif root.data<data:
            root.right=self.insert(root.right,data)
        else:
            root.left=self.insert(root.left,data)
        # UPDATE OUR HEIGHT OF PARENT NODES WITH FORMULA
        # HEIGHT=1+MAX(H(left child),H(right child))
        root.h=1+max(self.get_height(root.left),self.get_height(root.right))
        # WE UPDATE OUR HEIGHT 
        # NOW WE WANT OR WE NEED OUR BALANCE FACTOR SO FIND IT BY MAKING FUNCTION ABOVE
        balance=self.get_balanced(root)
        # NOW WE GET OUR BASIC THINGS 
        # LET'S STEP INTO OUR FOUR CASES
        # ------------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------

        # 1.L-->if left is heavy means balance >=1 like 2,3,5,6,7,
        # 2.R-->if right is heavy means balance <=1 like -2,-3,-5,-43
        # 3.LR-->if left is heavy means balance >=1 like 3,4,3,5,435,
        # 4.RL-->if right is heavy means balance <=1 like -34,-4,-6,-46,-5

        # SO FOUR THESE CASES WE HAVE TO MAKE OUR FUNCTION WHICH ROTATES LEFT AND RIGHT ACC TO NEEDS WHICH IS ABOVE
        if balance>1 and data<root.left.data:#L
            return self.rr(root)
        if balance<-1 and data>root.right.data:#R
            return self.ll(root)
        if balance>1 and data>root.left.data:#lR
            root.left=self.ll(root.left)
            return self.rr(root)
        if balance<-1 and data<root.right.data:#RL
            root.right=self.rr(root.right)
            return self.ll(root)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

if __name__ == '__main__':
    tree=AVL_tree()
    # BCZ IT CHANGE ACC TO REQUIREMENT
    root=None
    
    root=tree.insert(root,14)
    root=tree.insert(root,15)
    root=tree.insert(root,16)
    root=tree.insert(root,12)
    root=tree.insert(root,13)
    root=tree.insert(root,11)
    root=tree.insert(root,10)
    root=tree.insert(root,1)
    root=tree.insert(root,2)
    root=tree.insert(root,3)
    root=tree.insert(root,4)
    root=tree.insert(root,5)
    root=tree.insert(root,7)
    root=tree.insert(root,6)
    root=tree.insert(root,9)
    root=tree.insert(root,8)
    
    #             10 
    #         /       \ 
    #        4         13  
    #      /   \     /    \
    #    2      6   11     15
    #  /  \   /  \   \    /  \
    # 1   3  5   8    12  14  16
    #          /  \
    #         7   9
    tree.inorder(root)