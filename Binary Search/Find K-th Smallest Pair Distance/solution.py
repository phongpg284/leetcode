class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if self.count_pairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

    def count_pairs(self, nums, target):
        count = left = 0
        for right in range(1, len(nums)):
            while nums[right] - nums[left] > target:
                left += 1
            count += right - left
        return count
