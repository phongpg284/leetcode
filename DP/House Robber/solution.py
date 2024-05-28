# top down
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.helper(dp, nums, n - 1)

    def helper(self, dp, nums, n):
        if n < 0:
            return 0
        if n == 0:
            return nums[0]
        if dp[n] > -1:
            return dp[n]

        res = max(self.helper(dp, nums, n - 1),
                  self.helper(dp, nums, n - 2) + nums[n])
        dp[n] = res
        return res


# bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = nums[0] 
        for i in range(1, n):
            prev = dp[i - 2] if i >= 2 else 0
            dp[i] = max(dp[i - 1], nums[i] + prev)
        return dp[n - 1]
