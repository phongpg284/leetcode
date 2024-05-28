class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start, end = 0, 0
        res = 0
        temp = 0

        while end < n:
            temp += abs(ord(s[end]) - ord(t[end]))

            while temp > maxCost:
                temp -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            res = max(res, end - start + 1)
            end += 1

        return res
