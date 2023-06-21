class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        res = 2
        dp = [[1] * 1000 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                temp = nums[i] - nums[j]
                dp[i][temp] = dp[j][temp] + 1
                res = max(res, dp[i][temp])
        return res
