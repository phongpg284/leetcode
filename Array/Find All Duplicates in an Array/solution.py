class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            num = abs(nums[i])
            index = num - 1
            if nums[index] < 0:
                res.append(num)
            nums[index] *= -1
        return res
