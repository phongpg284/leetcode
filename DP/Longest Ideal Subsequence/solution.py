class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(
                [dp[i + j] + 1 for j in range(-k, k + 1) if 0 <= i + j < 26])
        return max(dp)
