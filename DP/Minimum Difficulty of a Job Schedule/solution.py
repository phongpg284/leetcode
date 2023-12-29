class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[-1] * n for _ in range(d + 1)]
        a = self.helper(jobDifficulty, n - 1, d, dp)
        return a if a < 10 ** 9 else -1

    def helper(self, jobs, n, d, dp):
        if n < 0:
            return 0 if d == 0 else -1
        if d == 0:
            return -1 if n > -1 else 0

        if dp[d][n] > -1:
            return dp[d][n]

        temp = 10 ** 9
        max_val = 0
        for i in range(n + 1):
            max_val = max(max_val, jobs[n - i])
            a = self.helper(jobs, n - 1 - i, d - 1, dp)
            if a > -1:
                temp = min(temp, a + max_val)
        dp[d][n] = temp
        return temp
