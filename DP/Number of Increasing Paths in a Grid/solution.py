class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        for i in range(m):
            for j in range(n):
                res += self.dfs(i, j, grid, dp, m, n, directions)
        return res % (10 ** 9 + 7)

    def dfs(self, row, col, grid, dp, m, n, directions):
        if dp[row][col] != -1:
            return dp[row][col]

        temp = 1
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and grid[new_row][new_col] > grid[row][col]:
                temp += self.dfs(new_row, new_col, grid, dp, m, n, directions)
        temp %= (10 ** 9 + 7)
        dp[row][col] = temp
        return temp