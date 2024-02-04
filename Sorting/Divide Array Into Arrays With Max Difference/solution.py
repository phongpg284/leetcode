class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums) // 3):
            if nums[3 * i] + k < nums[3 * i + 2]:
                return []
            res.append([nums[3 * i], nums[3 * i + 1], nums[3 * i + 2]])
        return res
