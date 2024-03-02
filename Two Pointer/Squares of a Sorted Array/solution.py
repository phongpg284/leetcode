class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mark = n - 1
        for i in range(n):
            if nums[i] >= 0:
                mark = i
                break

        nums = [num ** 2 for num in nums]

        i = mark
        j = mark - 1
        res = []

        while len(res) < n:
            if (i < n and nums[i] <= nums[j]) or (j < 0):
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j -= 1
        return res
