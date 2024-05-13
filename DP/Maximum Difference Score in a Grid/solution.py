class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_grid = [[-1] * n for _ in range(m)]
        res = float('-inf')

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    min_grid[i][j] = grid[i][j]
                elif i == 0:
                    min_grid[i][j] = min(min_grid[i][j - 1], grid[i][j - 1])
                elif j == 0:
                    min_grid[i][j] = min(min_grid[i - 1][j], grid[i - 1][j])
                else:
                    min_grid[i][j] = min(
                        min_grid[i - 1][j], min_grid[i][j - 1], grid[i - 1][j], grid[i][j - 1])

                if i + j != 0:
                    res = max(res, grid[i][j] - min_grid[i][j])
        return res
