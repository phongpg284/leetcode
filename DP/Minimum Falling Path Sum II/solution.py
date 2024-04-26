class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return min(grid[0])

        dp = [grid[0], grid[1]]

        for i in range(1, n):
            for j in range(n):
                temp = float('inf')
                for k in range(n):
                    if j != k:
                        temp = min(temp, dp[(i - 1) % 2][k])
                dp[i % 2][j] = temp + grid[i][j]
        return min(dp[(n - 1) % 2])
