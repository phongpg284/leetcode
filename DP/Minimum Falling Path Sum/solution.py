class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] if j > 0 else float('inf'), dp[i - 1]
                                   [j], dp[i - 1][j + 1] if j + 1 < n else float('inf')) + matrix[i][j]
        return min(dp[i])
