class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = [[0] * len(nums) for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if i == j:
                    result[i][j] = nums[i]
                else:
                    left = nums[i] - result[i+1][j] 
                    right = nums[j] - result[i][j-1] 
                    result[i][j] = max(left, right)
        return result[0][len(nums) - 1] >= 0
