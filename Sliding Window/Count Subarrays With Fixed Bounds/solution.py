class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left, right = 0, 0
        min_index, max_index = -1, -1
        mark = -1
        res = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                mark = i

            if nums[i] == minK:
                min_index = i

            if nums[i] == maxK:
                max_index = i

            res += max(0, min(min_index, max_index) - mark)
        return res
