class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        top_row = [0] * n
        top_col = [0] * n
        res = 0

        for i in range(n):
            for j in range(n):
                top_row[i] = max(top_row[i], grid[i][j])
                top_col[j] = max(top_col[j], grid[i][j])

        for i in range(n):
            for j in range(n):
                res += min(top_row[i], top_col[j]) - grid[i][j]

        return res
