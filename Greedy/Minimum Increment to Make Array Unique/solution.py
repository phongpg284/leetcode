class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        temp = nums[0] - 1
        res = 0
        
        for num in nums:
            if num > temp:
                temp = num
            else:
                res += temp + 1 - num 
                temp += 1
        return res