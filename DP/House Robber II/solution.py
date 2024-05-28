class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        prev, cur = 0, nums[0]
        prev2, cur2 = 0, 0

        for i in range(1, n):
            prev, cur = cur, max(prev + nums[i], cur)
            prev2, cur2 = cur2, max(prev2 + nums[i], cur2)
        return max(prev, cur2)
