# input - BINARY TREE([50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]) node=70
# output - [70,62,75,50]
# -----------------------------------------------------------------------------------
# Here input tree tree is given as 
#                                      50
#                                   /     \\ 
#                                 25       75 
#                               /  \      //  \         
#                             12    37   62  87 
#                                  /     \\   
#                                  30     70
#
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# This class represent node and state
class State:
    def __init__(self,node,state):
        self.node = node
        self.state= state
# tree creation function 
def build_tree(arr):
    stack = []
    root = Node(arr[0])
    stack.append(State(root,1))
    # if none then increase 
    # if state = 3 pop
    # else increment state of top make new node connect then push
    i=0
    while stack:
        top = stack[-1]
        if top.state==1:
            i+=1
            if arr[i]!=None:
                nn = Node(arr[i])
                top.node.left = nn
                stack.append(State(top.node.left,1))
            else:
                top.node.left=None
            top.state+=1
        elif top.state==2:
            i+=1
            if arr[i]!=None:
                nn = Node(arr[i])
                top.node.right= nn
                stack.append(State(top.node.right,1))
            else:
                top.node.right=None
            top.state+=1
        else:
            stack.pop()
    return root
# this function returns level of node
def get_level(tree):
        level = 0 
        if not tree:
            return 0
        level = 1+get_level(tree.left)
        level = 1+get_level(tree.right)
        return level

def node_to_root_path(tree,node,arr):
    if tree:
        if tree.data == node:
            arr.append(tree.data)
            return True
        flag = node_to_root_path(tree.left,node,arr)
        if flag:
            arr.append(tree.data)
            return True
        flag = node_to_root_path(tree.right,node,arr)
        if flag:
            arr.append(tree.data)
            return True
    return False
if __name__ == '__main__':
    arr = [50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    tree = build_tree(arr)
    
    level = get_level(tree)
    arr=[]
    node_to_root_path(tree,70,arr)
    print(arr)
    