class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        res = 0

        for c in count_t.keys():
            if c in count_s:
                if count_t[c] > count_s[c]:
                    res += count_t[c] - count_s[c]
            else:
                res += count_t[c]

        return res
