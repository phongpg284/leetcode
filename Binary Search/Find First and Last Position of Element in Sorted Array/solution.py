class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        start = 0
        end = len(nums) - 1
        while start <= end:
            temp = (start + end) // 2
            if nums[temp] == target:
                result[0] = temp
                end = temp -1
            elif nums[temp] < target:
                start = temp + 1
            else:
                end = temp - 1
        
        start = 0
        end = len(nums) - 1
        while start <= end: 
            temp = (start + end) // 2
            if nums[temp] == target:
                result[1] = temp
                start = temp + 1
            elif nums[temp] <= target:
                start = temp + 1
            else:
                end = temp - 1
        return result