class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        store = {}
        nums = sorted(nums)
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in store:
                store[num] = store[sqrt] + 1
                res = max(res, store[num])
            else:
                store[num] = 1

        return res
