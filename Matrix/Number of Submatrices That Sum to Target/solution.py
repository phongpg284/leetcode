class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i - 1][j - 1] + \
                    dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        res = 0

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                store = {0: 1}
                temp = 0
                for k in range(1, m + 1):
                    temp = dp[k][j] - dp[k][i - 1]
                    if temp - target in store:
                        res += store[temp - target]
                    if temp in store:
                        store[temp] += 1
                    else:
                        store[temp] = 1

        return res
