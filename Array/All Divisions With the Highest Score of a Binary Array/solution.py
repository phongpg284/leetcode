class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]
        max_val = 0
        temp = 0

        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                temp += 1
                if temp > max_val:
                    res = [i]
                    max_val = temp
                elif temp == max_val:
                    res.append(i)
            else: 
                temp -= 1
        return res