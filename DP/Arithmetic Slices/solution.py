class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        start = 0
        current_step = 0
        result = 0

        if len(nums) > 1:
            current_step = nums[1] - nums[0]
        for i in range(1, len(nums) - 1): 
            if nums[i + 1] - nums[i] != current_step: 
                sub_len = i - start + 1
                result = result + (sub_len - 2) * (sub_len - 1) // 2
                start = i
                current_step = nums[i + 1] - nums[i]
        sub_len = len(nums) - start
        result = result + (sub_len - 2) * (sub_len - 1) // 2
        return result
