class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[float('inf')] * n for _ in range(n)]
        return self.solve(piles, 0, n - 1, dp)

    def solve(self, piles, start, end, dp):
        if start == end:
            return piles[start]
        take_left = piles[start]
        take_right = piles[end]
        
        if dp[start + 1][end] != float('inf'):
            take_left -= dp[start + 1][end]
        else:
            take_right -= self.solve(piles, start + 1, end, dp)
        if dp[start][end - 1] != float('inf'):
            take_right -= dp[start][end - 1]
        else:
            take_right -= self.solve(piles, start, end - 1, dp)
        
        result = max(take_left, take_right)
        dp[start][end] = result
        return result
    
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): 
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0