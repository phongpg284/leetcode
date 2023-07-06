class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        total = nums[0]
        res = float('inf')
        while right < n:
            if total < target:
                right += 1
                if right >= n: 
                    break
                total += nums[right]
            else:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        return res