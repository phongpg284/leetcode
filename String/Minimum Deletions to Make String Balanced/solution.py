class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        total = 0

        res = float('inf')
        for i in range(n):
            if s[i] == 'a':
                total += 1
                res = min(res, i + 1 - total * 2)

        res = min(res + total, n - total, total)

        return res
