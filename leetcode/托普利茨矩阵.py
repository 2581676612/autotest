"""
给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
"""
test_list = [[1,2],[2,2]]


def isToeplitzMatrix(matrix):
    matrix_len = len(matrix)
    zi_list_len = len(matrix[0])
    for zi_list_index in range(1, matrix_len):
        if len(matrix[zi_list_index]) != zi_list_len:
            return False
    step = 0
    for current_list_index in range(matrix_len):
        for num_index, num_val in enumerate(matrix[current_list_index]):
            current_index = num_index + 1
            for next_list_index in range(step + 1, matrix_len):
                if current_index > zi_list_len - 1:
                    break
                if matrix[next_list_index][current_index] != num_val:
                    return False
                current_index += 1
        step += 1
    return True


def isToeplitzMatrix_1(matrix):
    for list_index in range(len(matrix) - 1):
        if matrix[list_index][:-1] != matrix[list_index + 1][1:]:
            return False
    return True


print(isToeplitzMatrix_1(test_list))
