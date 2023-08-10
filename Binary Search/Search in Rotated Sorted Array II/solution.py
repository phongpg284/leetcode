class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1

        while start <= end:
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            while start < end and nums[end] == nums[end - 1]:
                end -= 1

            mid = (start + end) //2

            if nums[mid] == target:
                return True
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else: 
                    end = mid - 1

        return False