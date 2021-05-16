"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
"""

matrix = [[1, 2], [4, 5, 6], [1]]


def transpose(matrix):
    max_length = max(len(s) for s in matrix)
    new_matrix = [[] for i in range(max_length)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j].append(matrix[i][j])
    # new_matrix = [[].append(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i]))]
    print(new_matrix)
    return new_matrix


# transpose(matrix)

maxlength = max(len(s) for s in matrix)

