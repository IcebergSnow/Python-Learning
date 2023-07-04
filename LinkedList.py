class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



def linked_list_recursion(a):
    if a is None:
        return
    else:
        print(a.val)
        linked_list_recursion(a.next)


def insert(location, value, head_node):
    pos_node = head_node
    node = None

    node = Node(value)
    if location == 1:
        node.next = head_node
        return node
    if location == 2:
        node.next = head_node.next
        head_node.next = node
        return head_node
    for i in range(0, location - 2):
        if pos_node.next ==None:
            raise Exception("Attempted to place node greater than 1 more than max")
        pos_node = pos_node.next
    node.next = pos_node.next
    pos_node.next = node
    return head_node



def delete(location, start):
    pos_node = start
    if location == 1:
        return pos_node.next
    for i in range(0, location - 2):
        pos_node = pos_node.next
        if pos_node.next == None:
            raise Exception("Cannot delete non existent node")
        if i == location - 3:  
            pos_node.next = pos_node.next.next
            return start



def reverse(next_node_destination, current_node):
    if current_node == None:
        return next_node_destination
    next_stored = current_node.next
    current_node.next = next_node_destination
    return reverse(current_node, next_stored)
