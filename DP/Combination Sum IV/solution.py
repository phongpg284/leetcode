class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        dp = {0: 1}
        return self.helper(nums, target, dp)

    def helper(self, nums, val, dp):
        if val in dp:
            return dp[val]
        temp = 0    
        for num in nums:
            if (num <= val):
                val -= num
                temp += self.helper(nums, val, dp)
                val += num
            else:
                break
        dp[val] = temp
        return temp