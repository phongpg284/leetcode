class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 0
        res = 0
        store = defaultdict(int)

        while right < n:
            store[nums[right]] += 1
            while store[nums[right]] > k:
                store[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1

        return res
