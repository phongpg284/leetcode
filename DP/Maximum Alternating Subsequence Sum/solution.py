class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        odd = [0, 0]
        even = [0, 0]
        for i in range(n):
            odd[i % 2] = max(even[(i - 1) % 2] - nums[i], odd[(i - 1) % 2])
            even[i % 2] = max(odd[(i - 1) % 2] + nums[i], even[(i - 1) % 2])
        return max(even)
