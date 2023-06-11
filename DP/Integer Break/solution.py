class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * 59
        return self.breakNum(n, dp)
        
    def breakNum(self, n, dp):
        if n <= 2:
            return 1
        res = 0
        for i in range(2, n):
            if dp[n - i] > 0:
                res = max(res, i * dp[n - i], i * (n - i))
            else:
                res = max(res, i * self.breakNum(n - i, dp), i * (n - i))
        dp[n] = res
        return res
