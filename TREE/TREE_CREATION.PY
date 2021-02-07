class TREE:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertion(self,data,k):
        nn=TREE(data)
        if k=="l":
            if self.left==None:
                self.left=nn
            else:
                while self.left:
                    self.left=self.left.next
                self.left=nn
        else:
            if self.right==None:
                self.right=nn
            else:
                while self.right:
                    self.right=self.right.next
                self.right=nn
    def PrintTree(self):
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

if __name__ == '__main__':
    root=TREE(0)
    root.insertion(1,"l")
    root.insertion(2,"r")
    root.PrintTree()

    