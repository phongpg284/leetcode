class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * n for _ in range(m)]
        return self.solve(word1, word2, len(word1) - 1, len(word2) - 1, dp)

    def solve(self, word1, word2, i , j, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        
        if dp[i][j] > -1:
            return dp[i][j]
        if word1[i] == word2[j]:
            res = self.solve(word1, word2, i - 1, j - 1, dp)
            dp[i][j] = res
            return res
        else:
            a = self.solve(word1, word2, i - 1, j, dp) + 1
            b = self.solve(word1, word2, i, j - 1, dp) + 1
            c = self.solve(word1, word2, i - 1, j - 1, dp) + 1  
            dp[i][j] = min(a, b, c)
            return dp[i][j]