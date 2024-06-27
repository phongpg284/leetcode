class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        res = 0
        temp = 0

        for num in nums:
            temp += num & 1
            if temp - k >= 0:
                res += dp[temp - k]
            dp[temp] += 1
        return res
