class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        nums = sorted(nums)
        
        for i in range(n - 1, 0, -1):
            if nums[i] != nums[i - 1]:
                res += (n - i)
        return res
