class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        first = colors[0]
        last = colors[-1]
        colors = [last] + colors + [first]
        res = 0
        for i in range(1, len(colors) - 1):
            if colors[i + 1] == colors[i - 1] and colors[i - 1] != colors[i]:
                res += 1

        return res
