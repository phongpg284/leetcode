class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2: 
            return True
        mono_type = 0
        for i in range(1, n):
            temp = 0
            if nums[i] > nums[i - 1]:
                temp = 1
            if nums[i] < nums[i - 1]:
                temp = -1
            if mono_type != temp and temp != 0:
                if mono_type == 0:
                    mono_type = temp
                else:
                    return False
        return True

        