# INPUT  - TREE([10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1])
# OUTPUT - 10-
#          20-30-40-
#          50-60-70-80-90-100-
#          110-120-

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
# Here in this function will use two queue one will take care of nodes and other will take cares of childrens of the nodes which is in main queue
# steps - remove print add
def Method_1(tree):
    child_queue=[]
    main_queue=[]
    # we add root to main queue
    main_queue.append(tree)
    # this loop runs until main queue is empty
    while main_queue:
        # remove node
        node = main_queue.pop(0)
        # print node
        print(node.data,end="-")
        # add childrens to child queue
        for child in node.childrens:
            child_queue.append(child) 
        # if main queue is empty then will simply copy child queue to main queue and make child queue empty then print new line   
        if not main_queue:
            main_queue = child_queue
            child_queue=[]
            print()

# Here in this function will use only one queue and in this queue will add null or None so that it act as marker that if we found null or NOne then we print new line else will add nodes and child into one queue with separation of null
# steps - remove print add
def Method_2(tree):
    main_queue=[]
    # we add root to main queue
    main_queue.append(tree)
    # we also add None as well
    main_queue.append(None) 
    # this loop runs until main queue is empty
    while main_queue:
        # remove node
        node = main_queue.pop(0)
        # if node is empty then will print and add null into queue
        if not node:
            # we also take care of if the queue is not empty 
            if main_queue:
                main_queue.append(None)
                print()
        # if node is not none will do same operation but this time we add in main queue only
        else:
            # print node
            print(node.data,end="-")
            # add childrens to queue
            for child in node.childrens:
                main_queue.append(child) 
            
    print()


# Here in this function will use only one queue and in this queue and in this we not add null or use second queue will first add node print it and remove all nodes and when size is empty of queue will print new line
# steps - remove print add
def Method_3(tree):
    main_queue=[]
    # we add root to main queue
    main_queue.append(tree)
    # this loop runs until main queue is empty
    while main_queue:
        # we take care of size of queue
        size = len(main_queue)
        # remove all parent nodes and add childs
        while size!=0:
            node = main_queue.pop(0)
            print(node.data,end="-")
            # add childrens to queue
            for child in node.childrens:
                main_queue.append(child) 
            size-=1
        print()
        
if __name__ == '__main__':
    arr1 = [10,20,50,-1,60,-1,-1,30,70,-1,80,110,-1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1]
    arr2 = [10,20,-1,40,-1,30,50,-1,60]
    tree = build_tree(arr1)
    # tree.print_tree()
    Method_1(tree)
    print("-------------\n")
    Method_2(tree)
    print("-------------\n")
    Method_3(tree)

    