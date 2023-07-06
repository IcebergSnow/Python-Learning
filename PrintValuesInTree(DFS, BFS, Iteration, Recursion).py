from collections import deque
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Tree(1)
tree2 = Tree(2)
tree3 = Tree(3)
leaf4 = Tree(4)
leaf5 = Tree(5)
leaf6 = Tree(6)
leaf7 = Tree(7)

root.left = tree2
root.right = tree3
tree2.left = leaf4
tree2.right = leaf5
tree3.left = leaf6
tree3.right = leaf7

def pre_order (node):
#Self, Left, Right
    if node == None:
        return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)


def pre_order_iteration (node):
    current_node = None
    stack= [node]
    while len(stack) != 0:
        current_node = stack.pop()
        print(current_node.val)
        if current_node.right != None:
            stack.append(current_node.right)
        if current_node.left != None:
            stack.append(current_node.left)



def in_order(node):
#Left, Self, Right
    if node == None:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)

def in_order_iteration(node): #My code
    current_node = node
    stack = []
    while len(stack) != 0 or current_node != None:
        if current_node != None:
            stack.append(current_node)
            current_node = current_node.left

        if current_node == None:
            parent_node = stack.pop()
            print(parent_node.val)
            current_node = parent_node.right
def in_order_iteration_sample(node): #Code that my mentor wrote
    stack = []

    def push_left(root):
        while root != None:
            stack.append(root)
            root = root.left

    push_left(node)

    while len(stack) != 0:
        current = stack.pop()
        print(current.val)
        push_left(current.right)

def post_order_iteration(root):
    stack = []
    def backbone (root):
        while root != None:
            stack.append(root)
            if root.left != None:
                root = root.left
            else:
                root = root.right
    backbone(root)

    while len(stack) != 0:
        last_node = stack.pop()
        print(last_node.val)
        if len(stack) != 0 and stack[-1].left == last_node:
            backbone(stack[-1].right)



def post_order(node):
#Left, Right, Self
    if node == None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val)


def BFS(list_of_nodes): #Must input root as a list
    if len(list_of_nodes) == 0:
        return
    next_list = []
    for i in list_of_nodes:
        print(i.val)
        if i.left != None:
            next_list.append(i.left)
        if i.right != None:
            next_list.append(i.right)
    BFS(next_list)

def BFS_iteration(root):
    deque1 = deque()
    deque1.append(root)
    while len(deque1) != 0:
        if deque1[0].left != None:
            deque1.append(deque1[0].left)
        if deque1[0].right != None:
            deque1.append(deque1[0].right)
        print(deque1.popleft().val)

