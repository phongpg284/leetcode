class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums = sorted(nums)
        res = 0
        temp = 0
        for i in range(1, len(nums)):
            temp += nums[i] - nums[i - 1]
            res += temp
        return res

# Math solution
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)