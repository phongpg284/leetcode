class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0

        nums = sorted(nums)

        res = float('inf')
        for i in range(4):
            res = min(res, nums[i - 4] - nums[i])
        return res
