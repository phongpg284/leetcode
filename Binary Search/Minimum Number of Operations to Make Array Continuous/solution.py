class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        res = float('inf')
        
        for i, num in enumerate(nums):
            start, end = 0, len(nums) - 1
            target = num + n - 1
            target_index = 0
            
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] <= target:
                    target_index = mid
                    start = mid + 1
                else:
                    end = mid - 1
            res = min(res, n - (target_index - i + 1))
        return res 
