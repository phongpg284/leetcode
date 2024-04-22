class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * 10 for _ in range(n)]
        count = [[0] * 10 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                count[j][val] += 1

        for i in range(n):
            for j in range(10):
                if i == 0:
                    dp[i][j] = m - count[i][j]
                else:
                    min_val = float('inf')
                    for k in range(10):
                        if k != j:
                            min_val = min(dp[i - 1][k], min_val)
                    dp[i][j] = min_val + m - count[i][j]

        return min(dp[i])
