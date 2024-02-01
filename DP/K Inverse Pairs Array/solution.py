class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j] -
                                (dp[i - 1][j - i] if j - i >= 0 else 0)) % mod

        return (dp[n][k] - (dp[n][k - 1] if k > 0 else 0)) % mod
