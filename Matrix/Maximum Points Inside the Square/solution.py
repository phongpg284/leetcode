class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        store = defaultdict(list)
        n = len(s)
        for i in range(n):
            x, y = points[i]
            store[s[i]].append(max(abs(x), abs(y)))

        max_r = float('inf')
        for key, value in store.items():
            tags = sorted(value)
            if len(tags) >= 2:
                limit_r = tags[1] - 1
                max_r = min(max_r, limit_r)

            store[key] = tags

        res = 0
        for x, y in points:
            if abs(x) <= max_r and abs(y) <= max_r:
                res += 1
        return res
