#PROBLEM
#If a robot starts at (1,1) and can only move right and down, how many different ways are there for this robot to reach a certain coordinate.

def ways(x, y):
    graph = [[0]*y for i in range(x)]
    graph[0][0] = 1
    for i in range(0, x):
        for j in range(0, y):
            graph[i][j] += (graph[i-1][j] if i>0 else 0) + \
                           (graph[i][j-1] if j > 0 else 0)
    return graph[x-1][y-1]

