class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * n for _ in range(m)]
        
        def recur(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            
            if dp[i][j] > -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                res = recur(i - 1, j - 1)
                dp[i][j] = res
                return res
            
            a = recur(i - 1, j) + 1
            b = recur(i, j - 1) + 1
            res = min(a, b)
            dp[i][j] = res
            return res
        
        recur(m - 1, n - 1)
        return dp[m - 1][n - 1]

        

