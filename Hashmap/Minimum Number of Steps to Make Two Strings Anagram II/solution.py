class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        res = 0
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            res += abs(count_s[c] - count_t[c])
        return res
