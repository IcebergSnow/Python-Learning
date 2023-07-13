from collections import deque
class Graph:
    def __init__(self, val):
        self.val = val
        self.edges = []
graph1 = Graph(1)
graph2 = Graph(2)
graph3 = Graph(3)
graph4 = Graph(4)
graph5 = Graph(5)

graph1.edges = [graph2, graph4]
graph2.edges = [graph3]
graph4.edges = [graph3, graph5]
graph5.edges = [graph3]

def BFS_iteration(start):
    dq = deque()
    duplicates = set()
    dq.append(start)
    while len(dq) != 0:
        current_node = dq.popleft()
        if current_node in duplicates:
            continue
        print(current_node.val)
        duplicates.add(current_node)
        for i in current_node.edges:
            dq.append(i)



def DFS_recursion(start):
    duplicates = set()
    def DFS_recursion_helper(node):
        if node in duplicates:
            return
        print(node.val)
        duplicates.add(node)
        for i in node.edges:
            DFS_recursion_helper(i)
    DFS_recursion_helper(start)

