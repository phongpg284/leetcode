class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        res = 0
        t = 0

        for num in nums:
            t += num
            if t - goal in count:
                res += count[t - goal]
            count[t] = count.get(t, 0) + 1

        return res
