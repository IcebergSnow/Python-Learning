class Node:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.key = key
class Hash:
    def __init__(self):
        self.list = [None]*10
    def set(self, key, val):
        current_node = self.list[hash("Hello")%10]
        while current_node != None:
            if key  == current_node.key:
                current_node.val = val
                return
            current_node = current_node.next
        new_node = Node(key, val)
        new_node.next = self.list[hash(key) % 10]
        self.list[hash(key) % 10] = new_node
    def get(self, key):
        current_node = self.list[hash(key)%10]
        while current_node != None:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next
        raise Exception("Key cannot be found")
