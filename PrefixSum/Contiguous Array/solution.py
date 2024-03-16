class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        cur_sum = 0
        res = 0
        for i, num in enumerate(nums):
            cur_sum += 1 if num == 1 else -1

            if cur_sum not in count:
                count[cur_sum] = i
            else:
                res = max(res, i - count[cur_sum])

        return res
