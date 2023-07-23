class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        i = len(nums) - 1
        temp = nums[i]
        res = temp
        while i > 0:
            if temp >= nums[i - 1]:
                temp += nums[i - 1]
            else: 
                temp = nums[i - 1] 
            i -= 1
        res = max(temp, res)
        return res
