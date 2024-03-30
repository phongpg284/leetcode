class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)

    def subarraysWithAtMostKDistinct(self, nums, k):
        res = 0
        store = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            store[nums[right]] += 1
            if store[nums[right]] == 1:
                k -= 1
            while k == -1:
                store[nums[left]] -= 1
                if store[nums[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
        return res
