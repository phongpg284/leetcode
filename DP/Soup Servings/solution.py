class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4451: 
            return 1.0
        n = (n + 24) // 25
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        
        def recur(i, j):
            if i <= 0 and j <= 0: 
                return 0.5
            if i <= 0: 
                return 1.0
            if j <= 0: 
                return 0.0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 0.25 * (recur(i - 4, j) + recur(i - 3, j - 1) + recur(i - 2, j - 2) + recur(i - 1, j - 3))
            return dp[i][j]
        
        return recur(n, n)