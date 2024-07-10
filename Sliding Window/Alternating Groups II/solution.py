class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        start = 0
        end = 0
        n = len(colors)
        res = 0
        colors += colors[:k + 1]

        while start < n:
            if end < start + k - 1:
                c = colors[end]
                while end < start + k - 1:
                    end += 1
                    if colors[end] == c:
                        start = end
                        break
                    c = colors[end]
                if end == start + k - 1:
                    res += 1
                    start += 1

        return res
