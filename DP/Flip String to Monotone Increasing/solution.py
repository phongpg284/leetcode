class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cur_zero = 0
        res = 0

        for i in range(len(s)):
            cur_zero += s[i] == '0'
            res = min(res, (i + 1) - 2 * cur_zero)

        return res + cur_zero
