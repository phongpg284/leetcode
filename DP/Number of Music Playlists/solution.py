class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            dp[i][0] = 0
            for j in range(1, min(i, n) + 1):
                # add new song to playlist
                dp[i][j] = dp[i - 1][j - 1] * (n - (j - 1)) % mod
                if j > k:
                    # add old song to playlist
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod
        return dp[goal][n]  