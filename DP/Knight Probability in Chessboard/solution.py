class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # dp[n][n][k] represent number of way standing on location i, j with k moves left
        dp = [[ [0] * (k+1) for _ in range(n)] for _ in range(n)]
        
        # knight move directions
        directions = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

        # start call recursive with k moves and initial location
        res = self.move(row, column, k, n, dp, row, column, directions)
        return res / (8 ** k)

    def move(self, r, c, k, n, dp, row, col, directions):
        # if knight step of chessboard
        if r < 0 or c < 0 or r >= n or c >= n:
            return 0

        # if knight finish k moves
        if k == 0:
            return 1
        
        # if already reach this state
        if dp[r][c][k] > 0:
            return dp[r][c][k]

        res = 0

        # move all directions 
        for x, y in directions:
            res += self.move(r + x, c + y, k - 1, n, dp, row, col, directions)
        
        # store result to dp
        dp[r][c][k] = res

        return res
