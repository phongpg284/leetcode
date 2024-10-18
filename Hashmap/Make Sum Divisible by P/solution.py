class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        res = n
        store = {0: -1}

        total = 0
        target = sum(nums) % p

        if target == 0:
            return 0

        for i in range(n):
            total += nums[i]
            mod = total % p

            target_mod = (mod + p - target) % p

            if target_mod in store:
                res = min(res, i - store[target_mod])

            store[mod] = i

        return res if res < n else -1
