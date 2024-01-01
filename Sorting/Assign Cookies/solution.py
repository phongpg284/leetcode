class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(s)
        m = len(g)

        if n == 0:
            return 0

        g.sort()
        s.sort()

        res = 0
        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if s[i] >= g[j]:
                res += 1
                i -= 1
            j -= 1

        return res
