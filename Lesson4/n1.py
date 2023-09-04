matrix = [[1,2], [3,4], [5,6], [7,8]]

def trans_matrix():
    tm = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tm[j][i] = matrix[i][j]
    return tm

print(trans_matrix())
