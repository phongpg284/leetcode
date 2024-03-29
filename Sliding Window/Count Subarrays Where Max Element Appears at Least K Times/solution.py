class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        max_num = max(nums)
        res = 0
        while right < n:
            if nums[right] == max_num:
                k -= 1
            right += 1
            while k == 0:
                if nums[left] == max_num:
                    k += 1
                left += 1
            res += left
        return res