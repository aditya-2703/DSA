class TREE:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def insertion_binary_search_tree(root,data):
    nn=TREE(data)
    if root is None:
        return TREE(data)
    else:
        if root.data==data:
            return root
        elif root.data>data:
            root.left=insertion_binary_search_tree(root.left,data)
        else:
            root.right=insertion_binary_search_tree(root.right,data)
        return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
def search(root,element):
    if root.data==element:
        return True
    elif root.data>element:
        return search(root.left,element)
    return search(root.right,element)
def find_max(root):
    temp=root
    while temp.right:
        temp=temp.right
    return temp
def deletion_binary_search_tree(root,data):
    if root is None:
        return "TREE IS EMPTY"
    if root.data<data:
        root.right=deletion_binary_search_tree(root.right,data)
    elif root.data>data:
        root.left=deletion_binary_search_tree(root.left,data)
    else:
        if  root.left is None:
            temp=root.right
            root=None
            return temp
        if root.right is None :
            temp=root.left
            root=None
            return temp
        temp=find_max(root.left)
        root.data=temp.data
        root.left=deletion_binary_search_tree(root.left,temp)
    return root
root=TREE(10)
root=insertion_binary_search_tree(root,1)
root=insertion_binary_search_tree(root,2)
root=insertion_binary_search_tree(root,3)
root=insertion_binary_search_tree(root,40)
root=insertion_binary_search_tree(root,50)
root=insertion_binary_search_tree(root,60)
root=deletion_binary_search_tree(root,60)
print(f"inorder : : ")
inorder(root)
# print(f"preorder: : ")
# preorder(root)
# print(f"postorder: : ")
# postorder(root)

# print ("YES ELEMENT FOUND IN THIS TREE") if search(root,1) else print("ELEMENT NOT FOUND IN THIS TREE")