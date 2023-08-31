class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[-1]
        res = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                step = nums[i] // prev
                if nums[i] % prev:
                    step += 1
                prev = nums[i] // step
                res += step - 1
            else:
                prev = nums[i]
        return res
            