class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        mark = [False] * (n + 1)
        for num in nums:
            if mark[num]:
                return num
            else:
                mark[num] = True