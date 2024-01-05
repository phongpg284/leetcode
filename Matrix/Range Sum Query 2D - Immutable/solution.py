class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sumRect = [[0] * n for _ in range(m)]

        for i in range(m):
            t = 0
            for j in range(n):
                t += matrix[i][j]
                self.sumRect[i][j] = (
                    self.sumRect[i - 1][j] if i > 0 else 0) + t

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.sumRect[row1 - 1][col2] if row1 > 0 else 0
        b = self.sumRect[row2][col1 - 1] if col1 > 0 else 0
        c = self.sumRect[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.sumRect[row2][col2] - a - b + c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
