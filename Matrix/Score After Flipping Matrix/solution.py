class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        res = (1 << n - 1) * m

        for i in range(1, n):
            total = sum([grid[j][i] for j in range(m)])
            total = max(total, m - total)
            res += (1 << n - i - 1) * total
        return res
