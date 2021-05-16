"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
例：
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""


class NumMatrix:

    def __init__(self, matrix):
        l = len(matrix)
        self.new_matrix = [0] * l
        for i in range(l):
            l_1 = len(matrix[i])
            self.new_matrix[i] = [0] * (l_1 + 1)
        for m in range(l):
            for n in range(len(matrix[i])):
                self.new_matrix[m][n + 1] = self.new_matrix[m][n] + matrix[m][n]

    def sumRegion(self, row1, col1, row2, col2):
        s = 0
        for r in range(row1, row2+1):
            s += self.new_matrix[r][col2+1] - self.new_matrix[r][col1]
        return s


matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
          ]
n = NumMatrix(matrix)
n.sumRegion(1, 2, 2, 4)
