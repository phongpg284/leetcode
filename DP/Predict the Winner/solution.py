class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        result = [[0] * n for _ in range(n)]    
        '''
            points difference player go first will get with nums from i to j =>  
            => if result[i][j] > 0 means player 1 win
        '''
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    result[i][j] = nums[i]
                else:
                    left = nums[i] - result[i+1][j]     # case where player pick nums[i]
                    right = nums[j] - result[i][j-1]    # case where player pick nums[j]
                    result[i][j] = max(left, right)
        return result[0][n - 1] >= 0
