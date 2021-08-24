# input - BINARY TREE([50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None])
# output - convert this to left clone tree(like below second tree) and back to normal tree
# -----------------------------------------------------------------------------------
# Here input tree tree is given as 
#                                      50
#                                   /     \ 
#                                 25       75 
#                               /  \      /  \         
#                             12    37   62  87 
#                                  /     \   
#                                  30     70
#                                 
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# output has to be like 
#                                      50
#                                   /     \ 
#                                  50      75
#                                 /       /  \
#                                25      75  87    
#                               /  \     /   /       
#                              25   37  62   87
#                             /   /     / \
#                            12  37    62  70
#                           /   /          /
#                         12   30         70
#                              /
#                             30      
#                                 
# -----------------------------------------------------------------------------------


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
# In this class there is basics of tree like creation of tree and height , size ,total nodes  etc.
class Tree:
    # print tree in some good manner
    def print_tree(self,tree):
        if tree:
            if tree.left and tree.right:
                print(f"   {tree.data}")
                print(f"   |")
                print(f"{tree.left.data}<-->{tree.right.data}")
            elif tree.left and not tree.right:
                print(f"   {tree.data}")
                print(f"   |")
                print(f"{tree.left.data}<-->None")
            elif tree.right and not tree.left:
                print(f"   {tree.data}")
                print(f"   |")
                print(f"None<-->{tree.right.data}")
            self.print_tree(tree.left)
            self.print_tree(tree.right)
    # get total node from left and return to right and calculate total nodes
    def Method_1_no_of_node(self,tree,Total_node):
        if tree:
            Total_node = self.Method_1_no_of_node(tree.left,Total_node+1)
            Total_node = self.Method_1_no_of_node(tree.right,Total_node)
            return Total_node
        return Total_node
    # get nodes from left 
    # get nodes from right
    # add 1 and return 
    def Method_2_no_of_node(self,tree):
        if tree:
            left_node_size =  self.Method_2_no_of_node(tree.left)
            right_node_size = self.Method_2_no_of_node(tree.right)
            return left_node_size+right_node_size+1

        return 0
    # get height of left 
    # get height of right
    # get maximum outof return (left,right)+1
    def Method_1_get_height(self,tree):
        if tree:
            return 1+max(self.Method_1_get_height(tree.left),self.Method_1_get_height(tree.right))
        return 0
    def Method_2_get_height(self,tree):
        if tree:
            left_height = self.Method_2_get_height(tree.left)
            right_height = self.Method_2_get_height(tree.right)
            return max(left_height,right_height)+1
        return 0
   
    # travel all nodes and all it's value and return it   
    def Method_1_total_sum(self,tree,total_sum):
        if tree:
            total_sum = self.Method_1_total_sum(tree.left,total_sum+tree.data)
            total_sum = self.Method_1_total_sum(tree.right,total_sum)
            return total_sum
        return total_sum
    def Method_2_total_sum(self,tree):
        if tree:
            left_sum = self.Method_2_total_sum(tree.left)
            right_sum = self.Method_2_total_sum(tree.right)
            total_sum = left_sum+right_sum+tree.data
            return total_sum
        return 0
    
    # travel all nodes and return maximum out of it
    def Method_1_max_node(self,tree,max_node):
        if tree:
            max_node = max(tree.data,max_node)
            max_node = self.Method_1_max_node(tree.left,max_node)
            max_node = self.Method_1_max_node(tree.right,max_node)
            return max_node

        return max_node
    # first find max out of left
    # then find max out of right
    # return maximum out of both left and right
    def Method_2_max_node(self,tree):
        if tree:
            left_max =  self.Method_2_max_node(tree.left)
            right_max = self.Method_2_max_node(tree.right)
            return max(left_max,right_max,tree.data)
        return -9999999


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

def normal_to_left_clone_tree(tree):
    if not tree:
        return 
    
        
    left_clone =normal_to_left_clone_tree(tree.left)
    right_clone=normal_to_left_clone_tree(tree.right)
    
    temp_tree =Node(tree.data)
    tree.left = temp_tree
    temp_tree.left = left_clone
    tree.right = right_clone



    return tree

def left_clone_tree_to_normal(tree):
    if not tree:
        return 
    
    left_tree = left_clone_tree_to_normal(tree.left.left)
    right_tree = left_clone_tree_to_normal(tree.right)

    tree.left =left_tree
    tree.right = right_tree
    return tree

if __name__ == '__main__':
    arr = [50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]
    tree = build_tree(arr)
    obj = Tree()
    left_clone_tree=normal_to_left_clone_tree(tree)
    obj.print_tree(left_clone_tree)
    normal_tree = left_clone_tree_to_normal(tree)
    obj.print_tree(normal_tree)

  
   