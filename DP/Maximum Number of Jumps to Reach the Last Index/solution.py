class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if i > 0 and dp[i] == 0:
                    continue
                if abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        if dp[n - 1] == 0:
            return -1
        return dp[n - 1]