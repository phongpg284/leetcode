class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = [0]
        visited = set()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                self.dfs(grid, m, n, i, j, res, 0, visited)
        return res[0]

    def dfs(self, grid, m, n, row, col, res, gold, visited):
        if (row, col) in visited:
            return None

        if (
            row >= m
            or row < 0
            or col >= n
            or col < 0
            or grid[row][col] == 0
        ):
            return None

        visited.add((row, col))

        gold += grid[row][col]
        r1 = self.dfs(grid, m, n, row + 1, col, res, gold, visited)
        r2 = self.dfs(grid, m, n, row - 1, col, res, gold, visited)
        r3 = self.dfs(grid, m, n, row, col + 1, res, gold, visited)
        r4 = self.dfs(grid, m, n, row, col - 1, res, gold, visited)
        if not r1 and not r2 and not r3 and not r4:
            res[0] = max(res[0], gold)

        visited.remove((row, col))
