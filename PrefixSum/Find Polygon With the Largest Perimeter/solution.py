class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        prefix_sum = [0] * n
        t = 0
        for i in range(n):
            t += nums[i]
            prefix_sum[i] = t

        for i in range(n - 1, 1, -1):
            if nums[i] < prefix_sum[i - 1]:
                return prefix_sum[i]
        return -1
