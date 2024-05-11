class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if j + 1 < n and grid[i][j + 1] == grid[i][j]:
                    return False
                if i + 1 < m and grid[i + 1][j] != grid[i][j]:
                    return False
        return True
