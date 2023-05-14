class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp =[ [0] * n for _ in range(m)]
        result = 0
        for j in range(n):
            is_moveable = False
            for i in range(m):
                if j == 0:
                    dp[i][j] = 1
                else:
                    low = high = i
                    if i - 1 >= 0:
                        low = i -1
                    if i + 1 < m:
                        high = i + 1

                    if grid[i][j] > grid[low][j - 1]:
                        dp[i][j] = dp[low][j - 1]

                    if grid[i][j] > grid[i][j - 1]:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])

                    if grid[i][j] > grid[high][j - 1]:
                        dp[i][j] = max(dp[i][j], dp[high][j - 1])
                
                if dp[i][j] == 1:
                    is_moveable = True
            if is_moveable is True:
                result = j
            else: 
                break
        return result