#You are given a matrix. If a path from the top left corner to the bottom right corner is possible, you must label this path (the integer "2"). 
#You may only move down and right
#Some sections of the matrix are blocked and cannot be moved through (the integer "5")


matrix = [[0, 0, 0, 0, 0],
          [0, 5, 0, 5, 0],
          [0, 5, 0, 5, 0],
          [0, 5, 0, 0, 0],
          [0, 5, 0, 5, 0]]

def path(matrix):
    m = len(matrix)
    n = len(matrix[0])
    block = 5
    path = 2
    def path_helper(i, j)->bool:
        if i == m-1 and j == n-1:
            matrix[i][j] = path
            return True
        if i >= m or j >= n or matrix[i][j] == block:
            return False
        if not path_helper(i + 1, j) and not path_helper(i, j + 1):
            return False
        matrix[i][j] = path
        return True

    path_helper(0,0)

    for i in matrix:
        print(i)
