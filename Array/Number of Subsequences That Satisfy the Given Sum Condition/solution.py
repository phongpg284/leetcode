class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] * 2 <= target:
                return nums[0]
            else:
                return 0
        nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        total = 0
        turn = 1
        while start < end:
            if turn == 1:
                while end >= 0 and nums[start] + nums[end] > target:
                    end = end - 1
                total += 2 ** (end - start + 1) - 1
            else:
                while start < len(nums) and nums[start] + nums[end] <= target:
                    start = start + 1                
                total -= 2 ** (end - start + 1) - 1

            turn *= -1
        return total % (10**9 + 7)