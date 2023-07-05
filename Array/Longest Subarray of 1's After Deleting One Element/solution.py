class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        before = 0
        curr = 0
        zero = False
        # before and curr represents length of sequence of 1
        for num in nums:
            if num == 1:
                curr += 1
            else:
                zero = True
                res = max(res, before + curr)
                before = curr
                curr = 0
        res = max(res, before + curr)
        if not zero:
            return res - 1
        return res 