class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        res = 0
        temp = 0
        prev = ''

        for c in s:
            if c == prev:
                res += temp
                temp += 1
            else:
                prev = c
                temp = 1
            res += 1
        return res % mod