class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        result = 0
        for i in range(1, high + 1):
            if i >= zero and i >= one:
                dp[i] = dp[i - zero] + dp[i - one]
            elif i >= zero:
                dp[i] = dp[i - zero]
            elif i >= one:
                dp[i] = dp[i - one]

            if i >= low and i <= high:
                result += dp[i]
        return result % (10 ** 9 + 7)