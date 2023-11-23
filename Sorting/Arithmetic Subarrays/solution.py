class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []

        for i in range(len(l)):
            temp = sorted(nums[l[i]:r[i] + 1])
            res.append(self.isArithmetic(temp))
        return res

    def isArithmetic(self, arr):
        if len(arr) < 2:
            return False

        step = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != step:
                return False
        return True