class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[1] * 10 for _ in range(n)]

        prev_step = dict()
        prev_step[1] = [6, 8]
        prev_step[2] = [7, 9]
        prev_step[3] = [4, 8]
        prev_step[4] = [0, 3, 9]
        prev_step[5] = []
        prev_step[6] = [0, 1, 7]
        prev_step[7] = [2, 6]
        prev_step[8] = [1, 3]
        prev_step[9] = [2, 4]
        prev_step[0] = [4, 6]

        for i in range (1, n):
            for j in range(10):
                dp[i][j] = sum([dp[i - 1][k] for k in prev_step[j]])
        
        return sum(dp[n - 1]) % mod