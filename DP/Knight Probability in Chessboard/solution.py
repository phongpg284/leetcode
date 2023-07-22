class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[ [0] * (k+1) for _ in range(n)] for _ in range(n)]
        directions = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
        res = self.move(row, column, k, n, dp, row, column, directions)
        return res / (8 ** k)

    def move(self, r, c, k, n, dp, row, col, directions):
        if r < 0 or c < 0 or r >= n or c >= n:
            return 0
        if k == 0:
            return 1
        if dp[r][c][k] > 0:
            return dp[r][c][k]

        res = 0
        for x, y in directions:
            res += self.move(r + x, c + y, k - 1, n, dp, row, col, directions)
        dp[r][c][k] = res
        return res
