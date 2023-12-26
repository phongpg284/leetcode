class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[-1] * (n + 1) for _ in range(target + 1)]

        return self.helper(n, k, target, dp) % mod

    def helper(self, n, k, target, dp):
        if dp[target][n] > -1:
            return dp[target][n]

        if n == 0:
            if target == 0:
                return 1
            else:
                return -1

        temp = 0
        for i in range(1, k + 1):
            if target - i < 0:
                break
            p = self.helper(n - 1, k, target - i, dp)
            if p > 0:
                temp += p

        dp[target][n] = temp
        return temp
