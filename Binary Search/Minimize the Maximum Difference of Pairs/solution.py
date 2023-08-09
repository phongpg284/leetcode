class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        start, end = 0, nums[-1] - nums[0]

        while start <= end:
            mid = (start + end) // 2

            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            if count >= p:
                end = mid - 1
            else:
                start = mid + 1
        return start