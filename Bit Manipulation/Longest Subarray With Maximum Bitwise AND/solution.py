class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        res = 0
        temp = 0
        
        for num in nums:
            if num == max_val:
                temp += 1
                res = max(res, temp)
            else:
                temp = 0
        
        return res