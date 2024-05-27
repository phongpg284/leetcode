class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        l_once = [0] * n
        l_twice = [0] * n
        p = [0] * n
        total = [0] * n

        l_once[0] = 1
        p[0] = 1
        total[0] = 2

        for i in range(1, n):
            l_once[i] = p[i - 1]
            l_twice[i] = l_once[i - 1]
            p[i] = (l_once[i - 1] + l_twice[i - 1] + p[i - 1]) % mod
            total[i] = (l_once[i] + l_twice[i] + p[i]) % mod

        res = total[n - 1]

        for i in range(n):
            left = total[i - 1] if i > 0 else 1
            right = total[n - i - 2] if i < n - 1 else 1
            res += (left * right) % mod

        return res % mod
