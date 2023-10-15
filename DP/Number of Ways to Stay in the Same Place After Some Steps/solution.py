class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        max_len = min(arrLen, 1 + steps // 2)
        res = [0] * (max_len + 1)
        res[0] = 1

        for i in range(steps):
            left = 0
            for j in range(min(max_len, i + 2, steps - i + 3)):
                left, res[j] = res[j], (res[j] + left + res[j + 1]) % mod
        return res[0]