class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        i, j, total, res = 0, 0, 0, 0

        for i in range(len(nums)):
            total += nums[i]

            while (i - j + 1) * nums[i] - total > k:
                total -= nums[j]
                j += 1

            res = max(res, i - j + 1)

        return res
        