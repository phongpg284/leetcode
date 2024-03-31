class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        res = 0

        while right < n - 1:
            if nums[right + 1] != nums[right]:
                right += 1
            else:
                res += (right - left + 1) * (right - left + 2) // 2
                right += 1
                left = right
        if right > left:
            res += (right - left + 1) * (right - left + 2) // 2
        else:
            res += 1
        return res
