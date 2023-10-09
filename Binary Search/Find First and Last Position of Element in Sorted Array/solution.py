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
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                last = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1
                while last < len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                return [first, last]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [first, last]